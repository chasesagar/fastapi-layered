from apis.v1.schemas.common.phone import PhoneSchema
from models.common.phone import Phone
from transformers.base_transformers import BaseSchemaTransformer


class PhoneSchemaTransformer(BaseSchemaTransformer[PhoneSchema, Phone]):
    """
    Transformer for converting between PhoneSchema Schema and Phone BLModel.
    """

    schema_class = PhoneSchema
    business_model_class = Phone