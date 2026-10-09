"""Command-line interface for the Student Information System."""
import logging
from pathlib import Path

from src.models.student import Student
from src.services.student_service import StudentService
from src.utils.config import load_config, resolve_project_path
from src.utils.logger import configure_logging

logger = logging.getLogger(__name__)


def prompt_required(label: str) -> str:
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field is required.")


def prompt_int(label: str, minimum: int, maximum: int) -> int:
    while True:
        value = input(label).strip()
        try:
            number = int(value)
            if minimum <= number <= maximum:
                return number
        except ValueError:
            pass
        print(f"Enter a whole number from {minimum} to {maximum}.")


def prompt_student() -> Student:
    """Prompt for and validate a complete student record."""
    return Student(
        student_id=prompt_required("Student ID: "),
        first_name=prompt_required("First name: "),
        last_name=prompt_required("Last name: "),
        age=prompt_int("Age (1-120): ", 1, 120),
        course=prompt_required("Course/program: "),
        year_level=prompt_int("Year level (1-8): ", 1, 8),
        email=prompt_required("Email: "),
    )


def print_students(students: list[Student]) -> None:
    if not students:
        print("\nNo student records found.")
        return
    headers = ["ID", "First name", "Last name", "Age", "Course", "Year", "Email"]
    rows = [[s.student_id, s.first_name, s.last_name, str(s.age),
             s.course, str(s.year_level), s.email] for s in students]
    widths = [max(len(headers[i]), *(len(row[i]) for row in rows)) for i in range(len(headers))]
    print()
    print(" | ".join(headers[i].ljust(widths[i]) for i in range(len(headers))))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(row[i].ljust(widths[i]) for i in range(len(headers))))
    print(f"\nTotal: {len(students)}")


def main() -> None:
    config = load_config()
    configure_logging(
        resolve_project_path(config["log_file"]),
        config.get("log_level", "INFO"),
    )
    service = StudentService(resolve_project_path(config["data_file"]))

    while True:
        print(f"""
========================================
 {config.get('app_name', 'Student Information System')}
========================================
1. Add student
2. View all students
3. Find student by ID
4. Update student
5. Delete student
6. Search students
7. Export students to JSON
0. Exit
""")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                student = prompt_student()
                service.add_student(student)
                print("Student added successfully.")
            elif choice == "2":
                print_students(service.list_students())
            elif choice == "3":
                print_students([service.get_student(prompt_required("Student ID: "))])
            elif choice == "4":
                student_id = prompt_required("Student ID to update: ")
                current = service.get_student(student_id)
                print("Press Enter to keep the current value.")
                updates = {}
                for field, label in [
                    ("first_name", "First name"),
                    ("last_name", "Last name"),
                    ("age", "Age"),
                    ("course", "Course/program"),
                    ("year_level", "Year level"),
                    ("email", "Email"),
                ]:
                    value = input(f"{label} [{getattr(current, field)}]: ").strip()
                    if value:
                        if field in ("age", "year_level"):
                            try:
                                value = int(value)
                            except ValueError:
                                raise ValueError(f"{label} must be a whole number.")
                        updates[field] = value
                service.update_student(student_id, updates)
                print("Student updated successfully.")
            elif choice == "5":
                student_id = prompt_required("Student ID to delete: ")
                confirm = input(f"Delete student {student_id}? (y/N): ").strip().lower()
                if confirm == "y":
                    service.delete_student(student_id)
                    print("Student deleted.")
                else:
                    print("Deletion cancelled.")
            elif choice == "6":
                query = input("Search by ID, name, course, or email: ")
                print_students(service.search_students(query))
            elif choice == "7":
                destination = input("Export path [data/students_export.json]: ").strip()
                output = Path(destination) if destination else resolve_project_path("data/students_export.json")
                if not output.is_absolute():
                    output = resolve_project_path(str(output))
                print(f"Exported to: {service.export_students(output)}")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Choose one of the listed options.")
        except (ValueError, KeyError, OSError) as exc:
            logger.warning("Operation failed: %s", exc)
            print(f"Error: {exc}")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Student Information System.")
            break


if __name__ == "__main__":
    main()
