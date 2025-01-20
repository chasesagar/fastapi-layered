from apis.v1.schemas.common.location import LocationSchema
from models.common.location import Location
from transformers.base_transformers import BaseSchemaTransformer


class LocationSchemaTransformer(BaseSchemaTransformer[LocationSchema, Location]):
    """
    Transformer for converting between LocationSchema Schema and Location BLModel.
    """

    schema_class = LocationSchema
    business_model_class = Location
