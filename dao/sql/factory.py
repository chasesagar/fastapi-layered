from functools import lru_cache

from dao.sql.student_sql_dao import StudentSQLDAO


@lru_cache
def get_students_sql_dao(session) -> StudentSQLDAO:
    """
    Factory to provide StudentDDBDAO with a database session.

    Args:
        session (Session): A SQLAlchemy session.

    Returns:
        StudentSQLDAO: An instance of the StudentDDBDAO.
    """
    return StudentSQLDAO()
