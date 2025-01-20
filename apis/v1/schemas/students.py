from pydantic import BaseModel, field_validator, Field

from apis.v1.schemas.common.address import AddressSchema
from apis.v1.schemas.common.phone import PhoneSchema
from apis.v1.schemas.enums.gender_enum import GenderSchemaEnum
from apis.v1.schemas.enums.grade_enum import StudentGradeSchemaEnum

class _StudentSpecialNeedsSchema(BaseModel):
    """
    Schema for representing a student special needs
    """
    has_special_needs: bool
    special_needs_type: str | None = None


class _StudentNotesSchema(BaseModel):
    """
    Schema for representing a student notes
    """
    school_notes: str | None = None
    driver_notes: str | None = None


class _StudentParentSchema(BaseModel):
    """
    Schema for representing a student parent
    """
    parent_id: str | None = None
    first_name: str
    last_name: str
    relation: str | None = None
    email: str | None = None
    phone: PhoneSchema | None = None

class _BaseStudentSchema(BaseModel):
    """
    Base schema for representing a student
    """
    school_id: str
    first_name: str
    last_name: str
    gender: GenderSchemaEnum
    grade: StudentGradeSchemaEnum
    birthdate: str
    special_needs: _StudentSpecialNeedsSchema
    age: int
    email: str | None = None
    phone: PhoneSchema | None = None
    addresses: list[AddressSchema | None] = Field(default_factory=[])
    parents: list[_StudentParentSchema]
    notes: _StudentNotesSchema | None = None

class StudentRequestSchema(_BaseStudentSchema):
    """
    Schema for creating a student
    """
    pass

class StudentResponseSchema(_BaseStudentSchema):
    """
    Schema for representing a student in response
    """
    student_id: str
