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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2025.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail
from sailpoint.v2025.models.reviewable_entitlement import ReviewableEntitlement
from typing import Optional, Set
from typing_extensions import Self

class ReviewableAccessProfile(BaseModel):
    """
    ReviewableAccessProfile
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The id of the Access Profile")
    name: Optional[StrictStr] = Field(default=None, description="Name of the Access Profile")
    description: Optional[StrictStr] = Field(default=None, description="Information about the Access Profile")
    privileged: Optional[StrictBool] = Field(default=None, description="Indicates if the entitlement is a privileged entitlement")
    cloud_governed: Optional[StrictBool] = Field(default=None, description="True if the entitlement is cloud governed", alias="cloudGoverned")
    end_date: Optional[datetime] = Field(default=None, description="The date at which a user's access expires", alias="endDate")
    owner: Optional[IdentityReferenceWithNameAndEmail] = None
    entitlements: Optional[List[Optional[ReviewableEntitlement]]] = Field(default=None, description="A list of entitlements associated with this Access Profile")
    created: Optional[datetime] = Field(default=None, description="Date the Access Profile was created.")
    modified: Optional[datetime] = Field(default=None, description="Date the Access Profile was last modified.")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "privileged", "cloudGoverned", "endDate", "owner", "entitlements", "created", "modified"]

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
        """Create an instance of ReviewableAccessProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entitlements (list)
        _items = []
        if self.entitlements:
            for _item_entitlements in self.entitlements:
                if _item_entitlements:
                    _items.append(_item_entitlements.to_dict())
            _dict['entitlements'] = _items
        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReviewableAccessProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "privileged": obj.get("privileged"),
            "cloudGoverned": obj.get("cloudGoverned"),
            "endDate": obj.get("endDate"),
            "owner": IdentityReferenceWithNameAndEmail.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "entitlements": [ReviewableEntitlement.from_dict(_item) for _item in obj["entitlements"]] if obj.get("entitlements") is not None else None,
            "created": obj.get("created"),
            "modified": obj.get("modified")
        })
        return _obj


