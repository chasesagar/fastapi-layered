from apis.v1.schemas.common.address import AddressSchema
from models.common.address import Address
from transformers.base_transformers import BaseSchemaTransformer


class AddressSchemaTransformer(
    BaseSchemaTransformer[AddressSchema, AddressSchema, Address]
):
    """
    Transformer for converting between AddressSchema Schema and Address BLModel.
    """

    input_schema_class = AddressSchema
    output_schema_class = AddressSchema
    business_model_class = Address

    def __init__(self):
        """
        Initialize the transformer with optional field exclusions.
        """
        super().__init__(exclude_fields={"address_id"})
