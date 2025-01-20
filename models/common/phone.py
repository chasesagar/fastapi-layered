from pydantic import BaseModel


class Phone(BaseModel):
    """
    Represents a schema for phone-related information.

    Attributes:
        number (int): The phone number.
        country_code (str): The country code associated with the phone number.
        phone_type (str | None): An optional classification or type of the phone,
            such as "mobile" or "landline".
    """
    number: int
    country_code: str
    phone_type: str | None = None

    def to_string(self) -> str:
        """
        Convert the phone number to a string representation.

        Returns:
            str: The string representation of the phone number.
        """
        return f"+{self.country_code} {self.number}"


