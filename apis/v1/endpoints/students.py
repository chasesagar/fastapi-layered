from fastapi import APIRouter, Depends
from starlette import status

from apis.v1.schemas.students import StudentResponseSchema, StudentRequestSchema
from core.logger import logger
from services.factory import get_student_service
from services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["students"])


@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=StudentResponseSchema
)
async def create_student(
    student_schema: StudentRequestSchema,
    service: StudentService = Depends(get_student_service),
) -> StudentResponseSchema:
    """
    Create a new student.

    Args:
        student_schema (StudentRequestSchema): The student data to create.
        service (StudentService): The service handling student creation.

    Returns:
        StudentResponseSchema: The created student's data.
    """
    logger.info(f"Creating a student with data: {student_schema}")

    return await service.create_student(student_schema)
