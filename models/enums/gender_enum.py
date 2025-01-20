from enum import Enum


class GenderEnum(Enum):
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

    def is_male(self) -> bool:
        """
        Determines the gender of the instance.

        This method compares the current instance with its 'male' attribute
        to determine if the instance is male. It returns a boolean value
        that represents the gender of the instance.

        Returns:
            bool: True if the instance is male, otherwise False.
        """
        return self == self.male