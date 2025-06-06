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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2025.models.access_summary_access import AccessSummaryAccess
from sailpoint.v2025.models.reviewable_access_profile import ReviewableAccessProfile
from sailpoint.v2025.models.reviewable_entitlement import ReviewableEntitlement
from sailpoint.v2025.models.reviewable_role import ReviewableRole
from typing import Optional, Set
from typing_extensions import Self

class AccessSummary(BaseModel):
    """
    An object holding the access that is being reviewed
    """ # noqa: E501
    access: Optional[AccessSummaryAccess] = None
    entitlement: Optional[ReviewableEntitlement] = None
    access_profile: Optional[ReviewableAccessProfile] = Field(default=None, alias="accessProfile")
    role: Optional[ReviewableRole] = None
    __properties: ClassVar[List[str]] = ["access", "entitlement", "accessProfile", "role"]

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
        """Create an instance of AccessSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access
        if self.access:
            _dict['access'] = self.access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entitlement
        if self.entitlement:
            _dict['entitlement'] = self.entitlement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of access_profile
        if self.access_profile:
            _dict['accessProfile'] = self.access_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        # set to None if entitlement (nullable) is None
        # and model_fields_set contains the field
        if self.entitlement is None and "entitlement" in self.model_fields_set:
            _dict['entitlement'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access": AccessSummaryAccess.from_dict(obj["access"]) if obj.get("access") is not None else None,
            "entitlement": ReviewableEntitlement.from_dict(obj["entitlement"]) if obj.get("entitlement") is not None else None,
            "accessProfile": ReviewableAccessProfile.from_dict(obj["accessProfile"]) if obj.get("accessProfile") is not None else None,
            "role": ReviewableRole.from_dict(obj["role"]) if obj.get("role") is not None else None
        })
        return _obj


