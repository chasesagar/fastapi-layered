from fastapi import APIRouter, Depends
from starlette import status

from apis.v1.schemas.students import StudentResponseSchema, StudentRequestSchema
from core.logger import logger
from services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=StudentResponseSchema)
def create_student(student_schema: StudentRequestSchema,
                   service: StudentService = Depends(StudentService)) -> StudentResponseSchema:
    logger.info(f"Creating a student with data: {student_schema}")

    service.create_student(student_schema)

    return {"message": "Student created successfully"}
