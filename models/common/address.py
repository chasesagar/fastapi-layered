from pydantic import BaseModel


class Address(BaseModel):
    """
    Represents an address schema.

    Attributes:
        house_number (str | None): The house or building number. Optional.
        street (str): The street name.
        city (str): The city name.
        state (str): The full name of the state or administrative region.
        state_code (str | None): The abbreviated code of the state. Optional.
        zip_code (str): The postal or ZIP code.
        postal_code (str | None): An alternative postal code format. Optional.
        country (str): The full name of the country.
        country_code (str | None): The abbreviated country code (e.g., ISO 3166). Optional.
    """
    house_number: str | None
    street: str
    city: str
    state: str
    state_code: str | None
    zip_code: str
    postal_code: str | None
    country: str
    country_code: str | None

    def short_address(self) -> str:
        """
        Generate a short address string with only the city, state, and country.

        Returns:
            str: The short address string.
        """
        return f"{self.street}, {self.city}, {self.country}"


