from enum import Enum


class GenderSchemaEnum(Enum):
    """
    Represents a Gender enumeration.

    This class defines an enumeration type for gender, with the possible values
    being 'male,' 'female,' and 'other.' It is intended to be used wherever
    gender representation is required, providing a clear and consistent way
    to handle gender values.

    Attributes:
        male (str): Represents the male gender.
        female (str): Represents the female gender.
        other (str): Represents any gender that does not fall under male or female.
    """
    male = "male"
    female = "female"
    other = "other"