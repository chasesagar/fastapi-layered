from pydantic import BaseModel


class PhoneSchema(BaseModel):
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