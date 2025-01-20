from pydantic import BaseModel


class Location(BaseModel):
    """
    Represents a schema for a geographical location.

    Attributes:
        latitude (float): Latitude of the location in decimal degrees, ranging from -90.0 to
            +90.0. Positive values indicate the northern hemisphere, while
            negative values indicate the southern hemisphere.
        longitude (float): Longitude of the location in decimal degrees, ranging from -180.0
            to +180.0. Positive values indicate the eastern hemisphere, while
            negative values indicate the western hemisphere.
    """
    latitude: float
    longitude: float

    def __str__(self):
        """
        Return a string representation of the location.

        Returns:
            str: A string representation of the location.

        """
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    def to_list(self) -> list[float]:
        """
        Convert the location to a list of latitude and longitude.

        Returns:
            list[float]: A list containing the latitude and longitude of the location.

        """
        return [self.latitude, self.longitude]