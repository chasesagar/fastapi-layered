from dao.ddb.student_ddb_dao import StudentDDBDAO


def get_students_ddb_dao(session) -> StudentDDBDAO:
    """
    Factory to provide StudentDDBDAO with a database session.

    Args:
        session (Session): A SQLAlchemy session.

    Returns:
        StudentDDBDAO: An instance of the StudentDDBDAO.
    """
    return StudentDDBDAO()
