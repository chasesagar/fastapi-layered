from apis.v1.schemas.enums.gender_enum import GenderSchemaEnum
from apis.v1.schemas.enums.grade_enum import StudentGradeSchemaEnum
from apis.v1.schemas.students import (
    StudentResponseSchema,
    _StudentSpecialNeedsSchema,
    _StudentParentSchema,
    StudentRequestSchema,
)
from models.enums.gender_enum import GenderEnum
from models.enums.grade_enum import StudentGradeEnum
from models.students import Student, _StudentSpecialNeeds, _StudentParent
from transformers.base_transformers import BaseSchemaTransformer


class StudentSchemaTransformer(BaseSchemaTransformer[StudentResponseSchema, Student]):
    """
    Transformer for converting between Student BLModel and StudentSchema Schema.
    """

    schema_class = StudentResponseSchema
    business_model_class = Student

    def to_business_model(self, schema: StudentRequestSchema) -> Student:
        """
        Convert a StudentSchema Schema instance to a Student BLModel instance.

        Args:
            schema (StudentSchema): The StudentSchema Schema instance to transform.

        Returns:
            Student: The transformed Student BLModel instance.
        """
        return Student(
            first_name=schema.first_name,
            last_name=schema.last_name,
            email=schema.email,
            phone=schema.phone,
            addresses=schema.addresses,
            school_id=schema.school_id,
            grade=self.transform_enum(schema.grade.value, StudentGradeEnum),
            gender=self.transform_enum(schema.gender.value, GenderEnum),
            birthdate=schema.birthdate,
            special_needs=_StudentSpecialNeeds(
                **schema.special_needs.model_dump()
            ),  # TODO: Transformers to be added
            age=schema.age,
            parents=[
                _StudentParent(**parent.model_dump()) for parent in schema.parents
            ],
            # TODO: Transformers to be added
        )

    def to_schema(self, bl_model: Student) -> StudentResponseSchema:
        """
        Convert a Student BLModel instance to a StudentSchema Schema instance.

        Args:
            bl_model (Student): The Student BLModel instance to transform.

        Returns:
            StudentSchema: The transformed StudentSchema Schema instance.
        """
        return StudentResponseSchema(
            student_id=bl_model.student_id,
            first_name=bl_model.first_name,
            last_name=bl_model.last_name,
            email=bl_model.email,
            phone=bl_model.phone,
            addresses=bl_model.addresses,
            school_id=bl_model.school_id,
            grade=self.transform_enum(bl_model.grade.value, StudentGradeSchemaEnum),
            gender=self.transform_enum(bl_model.gender.value, GenderSchemaEnum),
            birthdate=bl_model.birthdate,
            special_needs=_StudentSpecialNeedsSchema(
                **bl_model.special_needs.model_dump()
            ),
            # TODO: Transformers to be added
            age=bl_model.age,
            parents=[
                _StudentParentSchema(**parent.model_dump())
                for parent in bl_model.parents
            ],
            # TODO: Transformers to be added
        )
