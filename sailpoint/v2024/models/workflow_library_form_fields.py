# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowLibraryFormFields(BaseModel):
    """
    WorkflowLibraryFormFields
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the form field")
    help_text: Optional[StrictStr] = Field(default=None, description="Describes the form field in the UI", alias="helpText")
    label: Optional[StrictStr] = Field(default=None, description="A human readable name for this form field in the UI")
    name: Optional[StrictStr] = Field(default=None, description="The name of the input attribute")
    required: Optional[StrictBool] = Field(default=False, description="Denotes if this field is a required attribute")
    type: Optional[StrictStr] = Field(default=None, description="The type of the form field")
    __properties: ClassVar[List[str]] = ["description", "helpText", "label", "name", "required", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('text', 'textarea', 'boolean', 'email', 'url', 'number', 'json', 'checkbox', 'jsonpath', 'select', 'multiType', 'duration', 'toggle', 'formPicker', 'identityPicker', 'governanceGroupPicker', 'string', 'object', 'array', 'secret', 'keyValuePairs', 'emailPicker', 'advancedToggle', 'variableCreator', 'htmlEditor'):
            raise ValueError("must be one of enum values ('text', 'textarea', 'boolean', 'email', 'url', 'number', 'json', 'checkbox', 'jsonpath', 'select', 'multiType', 'duration', 'toggle', 'formPicker', 'identityPicker', 'governanceGroupPicker', 'string', 'object', 'array', 'secret', 'keyValuePairs', 'emailPicker', 'advancedToggle', 'variableCreator', 'htmlEditor')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WorkflowLibraryFormFields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkflowLibraryFormFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "helpText": obj.get("helpText"),
            "label": obj.get("label"),
            "name": obj.get("name"),
            "required": obj.get("required") if obj.get("required") is not None else False,
            "type": obj.get("type")
        })
        return _obj

