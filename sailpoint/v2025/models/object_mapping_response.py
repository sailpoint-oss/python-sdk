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

class ObjectMappingResponse(BaseModel):
    """
    ObjectMappingResponse
    """ # noqa: E501
    object_mapping_id: Optional[StrictStr] = Field(default=None, description="Id of the object mapping", alias="objectMappingId")
    object_type: Optional[StrictStr] = Field(default=None, description="Type of the object the mapping value applies to", alias="objectType")
    json_path: Optional[StrictStr] = Field(default=None, description="JSONPath expression denoting the path within the object where the mapping value should be applied", alias="jsonPath")
    source_value: Optional[StrictStr] = Field(default=None, description="Original value at the jsonPath location within the object", alias="sourceValue")
    target_value: Optional[StrictStr] = Field(default=None, description="Value to be assigned at the jsonPath location within the object", alias="targetValue")
    enabled: Optional[StrictBool] = Field(default=False, description="Whether or not this object mapping is enabled")
    created: Optional[StrictStr] = Field(default=None, description="Object mapping creation timestamp")
    modified: Optional[StrictStr] = Field(default=None, description="Object mapping latest update timestamp")
    __properties: ClassVar[List[str]] = ["objectMappingId", "objectType", "jsonPath", "sourceValue", "targetValue", "enabled", "created", "modified"]

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACCESS_PROFILE', 'ACCESS_REQUEST_CONFIG', 'ATTR_SYNC_SOURCE_CONFIG', 'AUTH_ORG', 'CAMPAIGN_FILTER', 'ENTITLEMENT', 'FORM_DEFINITION', 'GOVERNANCE_GROUP', 'IDENTITY', 'IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'LIFECYCLE_STATE', 'NOTIFICATION_TEMPLATE', 'PASSWORD_POLICY', 'PASSWORD_SYNC_GROUP', 'PUBLIC_IDENTITIES_CONFIG', 'ROLE', 'RULE', 'SEGMENT', 'SERVICE_DESK_INTEGRATION', 'SOD_POLICY', 'SOURCE', 'TAG', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION', 'WORKFLOW']):
            warnings.warn(f"must be one of enum values ('ACCESS_PROFILE', 'ACCESS_REQUEST_CONFIG', 'ATTR_SYNC_SOURCE_CONFIG', 'AUTH_ORG', 'CAMPAIGN_FILTER', 'ENTITLEMENT', 'FORM_DEFINITION', 'GOVERNANCE_GROUP', 'IDENTITY', 'IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'LIFECYCLE_STATE', 'NOTIFICATION_TEMPLATE', 'PASSWORD_POLICY', 'PASSWORD_SYNC_GROUP', 'PUBLIC_IDENTITIES_CONFIG', 'ROLE', 'RULE', 'SEGMENT', 'SERVICE_DESK_INTEGRATION', 'SOD_POLICY', 'SOURCE', 'TAG', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION', 'WORKFLOW') unknown value: {value}")
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
        """Create an instance of ObjectMappingResponse from a JSON string"""
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
        """Create an instance of ObjectMappingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objectMappingId": obj.get("objectMappingId"),
            "objectType": obj.get("objectType"),
            "jsonPath": obj.get("jsonPath"),
            "sourceValue": obj.get("sourceValue"),
            "targetValue": obj.get("targetValue"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "created": obj.get("created"),
            "modified": obj.get("modified")
        })
        return _obj


