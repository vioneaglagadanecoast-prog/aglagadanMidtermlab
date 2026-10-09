from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class Student:
    student_id: str
    first_name: str
    last_name: str
    age: int
    course: str
    year_level: int
    email: str

    def __post_init__(self) -> None:
        self.student_id = str(self.student_id).strip()
        self.first_name = str(self.first_name).strip()
        self.last_name = str(self.last_name).strip()
        self.course = str(self.course).strip()
        self.email = str(self.email).strip().lower()

        if not self.student_id:
            raise ValueError("Student ID is required.")
        if not self.first_name or not self.last_name:
            raise ValueError("First name and last name are required.")
        if not 1 <= int(self.age) <= 120:
            raise ValueError("Age must be between 1 and 120.")
        if not 1 <= int(self.year_level) <= 8:
            raise ValueError("Year level must be between 1 and 8.")
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise ValueError("Enter a valid email address.")

        self.age = int(self.age)
        self.year_level = int(self.year_level)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Student":
        """Build a Student from a dictionary."""
        return cls(**data)
