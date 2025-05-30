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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RoleInsightsSummary(BaseModel):
    """
    RoleInsightsSummary
    """ # noqa: E501
    number_of_updates: Optional[StrictInt] = Field(default=None, description="Total number of roles with updates", alias="numberOfUpdates")
    last_generated: Optional[datetime] = Field(default=None, description="The date-time role insights were last found.", alias="lastGenerated")
    entitlements_included_in_roles: Optional[StrictInt] = Field(default=None, description="The number of entitlements included in roles (vs free radicals).", alias="entitlementsIncludedInRoles")
    total_number_of_entitlements: Optional[StrictInt] = Field(default=None, description="The total number of entitlements.", alias="totalNumberOfEntitlements")
    identities_with_access_via_roles: Optional[StrictInt] = Field(default=None, description="The number of identities in roles vs. identities with just entitlements and not in roles.", alias="identitiesWithAccessViaRoles")
    total_number_of_identities: Optional[StrictInt] = Field(default=None, description="The total number of identities.", alias="totalNumberOfIdentities")
    __properties: ClassVar[List[str]] = ["numberOfUpdates", "lastGenerated", "entitlementsIncludedInRoles", "totalNumberOfEntitlements", "identitiesWithAccessViaRoles", "totalNumberOfIdentities"]

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
        """Create an instance of RoleInsightsSummary from a JSON string"""
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
        """Create an instance of RoleInsightsSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numberOfUpdates": obj.get("numberOfUpdates"),
            "lastGenerated": obj.get("lastGenerated"),
            "entitlementsIncludedInRoles": obj.get("entitlementsIncludedInRoles"),
            "totalNumberOfEntitlements": obj.get("totalNumberOfEntitlements"),
            "identitiesWithAccessViaRoles": obj.get("identitiesWithAccessViaRoles"),
            "totalNumberOfIdentities": obj.get("totalNumberOfIdentities")
        })
        return _obj


