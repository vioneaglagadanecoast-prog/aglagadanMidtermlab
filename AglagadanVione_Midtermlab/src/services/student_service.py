import json
import logging
from pathlib import Path
from typing import Any

from src.models.student import Student

logger = logging.getLogger(__name__)


class StudentService:

    def __init__(self, data_file: Path):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self._write_students([])

    def _read_students(self) -> list[Student]:
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                raw: Any = json.load(file)
            if not isinstance(raw, list):
                raise ValueError("Student data file must contain a JSON list.")
            return [Student.from_dict(item) for item in raw]
        except json.JSONDecodeError as exc:
            logger.exception("Student JSON file is invalid.")
            raise ValueError("Student data file is corrupted or invalid JSON.") from exc
        except OSError:
            logger.exception("Unable to read student data.")
            raise

    def _write_students(self, students: list[Student]) -> None:
        temporary = self.data_file.with_suffix(self.data_file.suffix + ".tmp")
        try:
            with temporary.open("w", encoding="utf-8") as file:
                json.dump([student.to_dict() for student in students], file, indent=4)
                file.write("\n")
            temporary.replace(self.data_file)
        except OSError:
            logger.exception("Unable to save student data.")
            raise

    def list_students(self) -> list[Student]:
        return sorted(self._read_students(), key=lambda item: item.student_id.lower())

    def get_student(self, student_id: str) -> Student:
        wanted = student_id.strip().lower()
        for student in self._read_students():
            if student.student_id.lower() == wanted:
                return student
        raise KeyError(f"No student found with ID '{student_id}'.")

    def add_student(self, student: Student) -> Student:
        students = self._read_students()
        if any(item.student_id.lower() == student.student_id.lower() for item in students):
            raise ValueError(f"Student ID '{student.student_id}' already exists.")
        students.append(student)
        self._write_students(students)
        logger.info("Added student ID %s", student.student_id)
        return student

    def update_student(self, student_id: str, updates: dict[str, Any]) -> Student:
        allowed = {"first_name", "last_name", "age", "course", "year_level", "email"}
        unknown = set(updates) - allowed
        if unknown:
            raise ValueError(f"Unsupported field(s): {', '.join(sorted(unknown))}")
        students = self._read_students()
        for index, current in enumerate(students):
            if current.student_id.lower() == student_id.strip().lower():
                data = current.to_dict()
                data.update(updates)
                updated = Student.from_dict(data)  # validates all fields before saving
                students[index] = updated
                self._write_students(students)
                logger.info("Updated student ID %s", current.student_id)
                return updated
        raise KeyError(f"No student found with ID '{student_id}'.")

    def delete_student(self, student_id: str) -> None:
        students = self._read_students()
        remaining = [item for item in students if item.student_id.lower() != student_id.strip().lower()]
        if len(remaining) == len(students):
            raise KeyError(f"No student found with ID '{student_id}'.")
        self._write_students(remaining)
        logger.info("Deleted student ID %s", student_id)

    def search_students(self, query: str) -> list[Student]:
        term = query.strip().lower()
        if not term:
            return self.list_students()
        matches = []
        for student in self._read_students():
            searchable = " ".join([
                student.student_id, student.first_name, student.last_name,
                student.course, student.email,
            ]).lower()
            if term in searchable:
                matches.append(student)
        return sorted(matches, key=lambda item: item.student_id.lower())

    def export_students(self, output_file: Path) -> Path:
        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open("w", encoding="utf-8") as file:
            json.dump([s.to_dict() for s in self.list_students()], file, indent=4)
            file.write("\n")
        logger.info("Exported students to %s", output_file)
        return output_file
