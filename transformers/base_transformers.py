from enum import Enum
from typing import TypeVar, Generic, Type

from pydantic import BaseModel

BusinessT = TypeVar("BusinessT", bound=BaseModel)
DaoModelT = TypeVar("DaoModelT", bound=BaseModel)
InputSchemaT = TypeVar("InputSchemaT", bound=BaseModel)
OutputSchemaT = TypeVar("OutputSchemaT", bound=BaseModel)
EnumT = TypeVar("EnumT", bound=Enum)


class BaseDaoTransformer(Generic[BusinessT, DaoModelT]):
    """
    Base DAO Transformer with default implementations.
    Provides automatic transformation for simple cases while allowing overrides for complex ones.
    """

    business_model_class: Type[BusinessT]
    dao_model_class: Type[DaoModelT]

    @staticmethod
    def transform_enum(value: str, enum_class: Type[EnumT]) -> EnumT:
        """
        Transform a string value to an Enum instance.

        Args:
            value (str): The string value to transform.
            enum_class (Enum): The Enum type to transform to.

        Returns:
            Enum: The transformed Enum instance.
        """
        return enum_class(value)

    def __init__(self, *, exclude_fields: set[str] | None = None):
        """
        Initialize the transformer with optional field exclusions.

        Args:
            exclude_fields: Fields to exclude from automatic transformation
        """
        self.exclude_fields = exclude_fields or set()

    def to_dao_model(self, business_model: BusinessT) -> DaoModelT:
        """
        Default implementation for business model to DAO model transformation.
        Override this method for custom transformation logic.

        Args:
            business_model: The business model instance to transform.
        """
        if not self.dao_model_class:
            raise ValueError("`dao_model_class` must be defined in the transformer")

        data = business_model.model_dump(exclude=self.exclude_fields)
        return self.dao_model_class(**data)

    def to_business_model(self, dao_model: DaoModelT) -> BusinessT:
        """
        Default implementation for DAO model to business model transformation.
        Override this method for custom transformation logic.

        Args:
            dao_model: The DAO model instance to transform.
        """
        if not self.business_model_class:
            raise ValueError(
                "`business_model_class` must be defined in the transformer"
            )

        return self.business_model_class.model_validate(dao_model)


class BaseSchemaTransformer(Generic[InputSchemaT, OutputSchemaT, BusinessT]):
    """
    Base Schema Transformer with default implementations.
    Provides automatic transformation for simple cases while allowing overrides for complex ones.
    """

    input_schema_class: Type[InputSchemaT]
    output_schema_class: Type[OutputSchemaT]
    business_model_class: Type[BusinessT]

    @staticmethod
    def transform_enum(value: str, enum_class: Type[EnumT]) -> EnumT:
        """
        Transform a string value to an Enum instance.

        Args:
            value (str): The string value to transform.
            enum_class (Enum): The Enum type to transform to.

        Returns:
            Enum: The transformed Enum instance.
        """
        return enum_class(value)

    def __init__(self, *, exclude_fields: set[str] | None = None):
        """
        Initialize the transformer with optional field exclusions.

        Args:
            exclude_fields: Fields to exclude from automatic transformation
        """
        self.exclude_fields = exclude_fields or set()

    def to_business_model(self, input_schema: InputSchemaT) -> BusinessT:
        """
        Default implementation for schema to business model transformation.
        Override this method for custom transformation logic.

        Args:
            input_schema: The input schema instance to transform.
        """
        if not self.business_model_class:
            raise ValueError(
                "`business_model_class` must be defined in the transformer"
            )

        data = input_schema.model_dump(exclude=self.exclude_fields)
        return self.business_model_class(**data)

    def to_schema(self, business_model: BusinessT) -> OutputSchemaT:
        """
        Default implementation for business model to schema transformation.
        Override this method for custom transformation logic.

        Args:
            business_model: The business model instance to transform.
        """
        if not self.output_schema_class:
            raise ValueError("`output_schema_class` must be defined in the transformer")

        data = business_model.model_dump(exclude=self.exclude_fields)
        return self.output_schema_class(**data)
