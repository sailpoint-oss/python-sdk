# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import warnings

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NativeChangeDetectionConfig(BaseModel):
    """
    Source configuration information for Native Change Detection that is read and used by account aggregation process.
    """ # noqa: E501
    enabled: Optional[StrictBool] = Field(default=False, description="A flag indicating if Native Change Detection is enabled for a source.")
    operations: Optional[List[StrictStr]] = Field(default=None, description="Operation types for which Native Change Detection is enabled for a source.")
    all_entitlements: Optional[StrictBool] = Field(default=False, description="A flag indicating that all entitlements participate in Native Change Detection.", alias="allEntitlements")
    all_non_entitlement_attributes: Optional[StrictBool] = Field(default=False, description="A flag indicating that all non-entitlement account attributes participate in Native Change Detection.", alias="allNonEntitlementAttributes")
    selected_entitlements: Optional[List[StrictStr]] = Field(default=None, description="If allEntitlements flag is off this field lists entitlements that participate in Native Change Detection.", alias="selectedEntitlements")
    selected_non_entitlement_attributes: Optional[List[StrictStr]] = Field(default=None, description="If allNonEntitlementAttributes flag is off this field lists non-entitlement account attributes that participate in Native Change Detection.", alias="selectedNonEntitlementAttributes")
    __properties: ClassVar[List[str]] = ["enabled", "operations", "allEntitlements", "allNonEntitlementAttributes", "selectedEntitlements", "selectedNonEntitlementAttributes"]

    @field_validator('operations')
    def operations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ACCOUNT_UPDATED', 'ACCOUNT_CREATED', 'ACCOUNT_DELETED']):
                warnings.warn(f"each list item must be one of ('ACCOUNT_UPDATED', 'ACCOUNT_CREATED', 'ACCOUNT_DELETED') unknown value: {i}")
        return value

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
        """Create an instance of NativeChangeDetectionConfig from a JSON string"""
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
        """Create an instance of NativeChangeDetectionConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "operations": obj.get("operations"),
            "allEntitlements": obj.get("allEntitlements") if obj.get("allEntitlements") is not None else False,
            "allNonEntitlementAttributes": obj.get("allNonEntitlementAttributes") if obj.get("allNonEntitlementAttributes") is not None else False,
            "selectedEntitlements": obj.get("selectedEntitlements"),
            "selectedNonEntitlementAttributes": obj.get("selectedNonEntitlementAttributes")
        })
        return _obj


