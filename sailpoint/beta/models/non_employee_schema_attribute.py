# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import warnings

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.non_employee_schema_attribute_type import NonEmployeeSchemaAttributeType
from typing import Optional, Set
from typing_extensions import Self

class NonEmployeeSchemaAttribute(BaseModel):
    """
    NonEmployeeSchemaAttribute
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Schema Attribute Id")
    system: Optional[StrictBool] = Field(default=False, description="True if this schema attribute is mandatory on all non-employees sources.")
    modified: Optional[datetime] = Field(default=None, description="When the schema attribute was last modified.")
    created: Optional[datetime] = Field(default=None, description="When the schema attribute was created.")
    type: NonEmployeeSchemaAttributeType
    label: StrictStr = Field(description="Label displayed on the UI for this schema attribute.")
    technical_name: StrictStr = Field(description="The technical name of the attribute. Must be unique per source.", alias="technicalName")
    help_text: Optional[StrictStr] = Field(default=None, description="help text displayed by UI.", alias="helpText")
    placeholder: Optional[StrictStr] = Field(default=None, description="Hint text that fills UI box.")
    required: Optional[StrictBool] = Field(default=False, description="If true, the schema attribute is required for all non-employees in the source")
    __properties: ClassVar[List[str]] = ["id", "system", "modified", "created", "type", "label", "technicalName", "helpText", "placeholder", "required"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NonEmployeeSchemaAttribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NonEmployeeSchemaAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "system": obj.get("system") if obj.get("system") is not None else False,
            "modified": obj.get("modified"),
            "created": obj.get("created"),
            "type": obj.get("type"),
            "label": obj.get("label"),
            "technicalName": obj.get("technicalName"),
            "helpText": obj.get("helpText"),
            "placeholder": obj.get("placeholder"),
            "required": obj.get("required") if obj.get("required") is not None else False
        })
        return _obj


