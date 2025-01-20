from pydantic import BaseModel, Field

from models.common.address import Address
from models.common.phone import Phone
from models.enums.gender_enum import GenderEnum
from models.enums.grade_enum import StudentGradeEnum


class _StudentSpecialNeeds(BaseModel):
    """
    Schema for representing a student special needs
    """

    has_special_needs: bool = False
    special_needs_type: str | None = None

    def is_special_needs(self) -> bool:
        """
        Check if the student has special needs

        Returns:
            bool: True if the student has special needs, False otherwise
        """
        return self.has_special_needs


class _StudentNotes(BaseModel):
    """
    Schema for representing a student notes
    """

    school_notes: str | None = None
    driver_notes: str | None = None


class _StudentParent(BaseModel):
    """
    Schema for representing a student parent
    """

    parent_id: str | None = None
    first_name: str
    last_name: str
    relation: str | None = None
    email: str | None = None
    phone: Phone | None = None

    def full_name(self) -> str:
        """
        Retrieve the full name of the parent

        Returns:
            str: The full name of the parent
        """
        return f"{self.first_name} {self.last_name}"


class Student(BaseModel):
    """
    Base schema for representing a student
    """

    student_id: str | None = None
    school_id: str
    first_name: str
    last_name: str
    gender: GenderEnum
    grade: StudentGradeEnum
    birthdate: str
    special_needs: _StudentSpecialNeeds
    age: int
    email: str | None = None
    phone: Phone | None = None
    addresses: list[Address | None] = Field(default_factory=[])
    parents: list[_StudentParent]
    notes: _StudentNotes | None = None

    def full_name(self) -> str:
        """
        Retrieve the full name of the student

        Returns:
            str: The full name of the student
        """
        return f"{self.first_name} {self.last_name}"
