from functools import lru_cache

from services.student_service import StudentService


@lru_cache
def get_student_service():
    """
    Retrieves and caches an instance of the `StudentService` class.

    The `get_student_service` function is a memoized function that ensures the
    `StudentService` instance is created once and reused across subsequent calls.
    The usage of `@lru_cache` helps in resource efficiency by preserving the
    shared instance, avoiding multiple initializations, and improving performance
    when the service is repeatedly accessed.

    Returns:
        StudentService: A cached instance of the `StudentService` class.
    """
    return StudentService()
