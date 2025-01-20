from apis.v1.schemas.students import StudentRequestSchema, StudentResponseSchema
from models.students import Student
from transformers.schema.student_transformers import StudentSchemaTransformer


class StudentService:
    def __init__(
            self,
            schema_transformer: StudentSchemaTransformer[StudentRequestSchema, Student] = StudentSchemaTransformer(),
            sql_transformer: StudentSchemaTransformer[StudentRequestSchema, Student] = StudentSchemaTransformer(),
            # TODO: Implement SQL Transformer
            ddb_transformer: StudentSchemaTransformer[StudentRequestSchema, Student] = StudentSchemaTransformer(),
            # TODO: Implement DDB Transformer
    ):
        self.schema_transformer = schema_transformer
        self.sql_transformer = sql_transformer
        self.ddb_transformer = ddb_transformer
        self.sql_dao = None  # StudentSQLDAO() # TODO: Implement SQL DAO
        self.ddb_dao = None  # StudentDDBDAO() # TODO: Implement DDB DAO

    async def create_student(self, schema: StudentRequestSchema) -> StudentResponseSchema:
        # Schema -> Business Model
        business_model = self.schema_transformer.to_business_model(schema)

        # Business Model -> SQL DAO
        sql_model = self.sql_transformer.to_dao_model(business_model)
        await self.sql_dao.create(sql_model)

        # Business Model -> DDB DAO
        ddb_model = self.ddb_transformer.to_dao_model(business_model)
        await self.ddb_dao.create(ddb_model)

        # Business Model -> Schema
        return self.schema_transformer.to_schema(business_model)
