from pydantic import BaseModel


class LocationSchema(BaseModel):
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