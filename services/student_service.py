from typing import TypeAlias

from fastapi import Depends

from apis.v1.schemas.students import StudentRequestSchema, StudentResponseSchema
from dao.ddb.factory import get_students_ddb_dao
from dao.ddb.student_ddb_dao import StudentDDBDAO
from dao.sql.factory import get_students_sql_dao
from dao.sql.student_sql_dao import StudentSQLDAO
from models.students import Student
from transformers.schema.student_transformers import StudentSchemaTransformer
from utils.id_utils import IDUtils

# Type alias for StudentSchemaTransformer
StudentSchemaTransformerType: TypeAlias = StudentSchemaTransformer[
    StudentRequestSchema, StudentResponseSchema, Student
]


class StudentService:
    """
    Handles the business logic related to student operations.

    The `StudentService` class is responsible for transforming data between
    schemas, business models, and database models. It facilitates creating and
    managing student records by coordinating with transformers and DAOs for
    different underlying data storage mechanisms like SQL and DynamoDB.

    Attributes:
        schema_transformer (StudentSchemaTransformerType): Handles transformations
            between schema and business model representations.
        sql_transformer (StudentSchemaTransformerType): Transforms business models
            into representations for SQL-based storage.
        ddb_transformer (StudentSchemaTransformerType): Transforms business models
            into representations for DynamoDB-based storage.
        student_sql_dao (StudentSQLDAO): Represents the data access layer for SQL-based student
            storage. Placeholder until implemented.
        student_ddb_dao (StudentDDBDAO): Represents the data access layer for DynamoDB-based
            student storage. Placeholder until implemented.
    """

    def __init__(
        self,
        schema_transformer: StudentSchemaTransformerType = StudentSchemaTransformer(),
        sql_transformer: StudentSchemaTransformerType = StudentSchemaTransformer(),
        # TODO: Implement SQL Transformer
        ddb_transformer: StudentSchemaTransformerType = StudentSchemaTransformer(),
        # TODO: Implement DDB Transformer
        student_sql_dao: StudentSQLDAO = Depends(get_students_sql_dao),
        student_ddb_dao: StudentDDBDAO = Depends(get_students_ddb_dao),
    ):
        self.schema_transformer = schema_transformer
        self.sql_transformer = sql_transformer
        self.ddb_transformer = ddb_transformer
        self.student_sql_dao = student_sql_dao
        self.student_ddb_dao = student_ddb_dao

    async def create_student(
        self, schema: StudentRequestSchema
    ) -> StudentResponseSchema:
        """
        Create a new student record
        Args:
            schema: StudentRequestSchema: Student request schema

        Returns:
            StudentResponseSchema: Student response schema

        """
        # Schema to Business Model
        student_bl_model = self.schema_transformer.to_business_model(schema)

        # Assigning unique ID to the student
        student_bl_model.student_id = IDUtils.generate_unique_id(prefix="STU")

        # Student business Model to student SQL DAO and create student
        sql_model = self.sql_transformer.to_dao_model(student_bl_model)
        await self.student_ddb_dao.create(sql_model)

        # Student business Model to student DDB DAO and create student
        ddb_model = self.ddb_transformer.to_dao_model(student_bl_model)
        await self.student_ddb_dao.create(ddb_model)

        # Convert student back from business Model to student response schema(DTL).
        return self.schema_transformer.to_schema(student_bl_model)
