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
import warnings

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2024.models.role_mining_role_type import RoleMiningRoleType
from sailpoint.v2024.models.role_mining_session_scope import RoleMiningSessionScope
from typing import Optional, Set
from typing_extensions import Self

class RoleMiningSessionDto(BaseModel):
    """
    RoleMiningSessionDto
    """ # noqa: E501
    scope: Optional[RoleMiningSessionScope] = None
    prune_threshold: Optional[StrictInt] = Field(default=None, description="The prune threshold to be used or null to calculate prescribedPruneThreshold", alias="pruneThreshold")
    prescribed_prune_threshold: Optional[StrictInt] = Field(default=None, description="The calculated prescribedPruneThreshold", alias="prescribedPruneThreshold")
    min_num_identities_in_potential_role: Optional[StrictInt] = Field(default=None, description="Minimum number of identities in a potential role", alias="minNumIdentitiesInPotentialRole")
    potential_role_count: Optional[StrictInt] = Field(default=None, description="Number of potential roles", alias="potentialRoleCount")
    potential_roles_ready_count: Optional[StrictInt] = Field(default=None, description="Number of potential roles ready", alias="potentialRolesReadyCount")
    type: Optional[RoleMiningRoleType] = None
    email_recipient_id: Optional[StrictStr] = Field(default=None, description="The id of the user who will receive an email about the role mining session", alias="emailRecipientId")
    identity_count: Optional[StrictInt] = Field(default=None, description="Number of identities in the population which meet the search criteria or identity list provided", alias="identityCount")
    saved: Optional[StrictBool] = Field(default=False, description="The session's saved status")
    name: Optional[StrictStr] = Field(default=None, description="The session's saved name")
    __properties: ClassVar[List[str]] = ["scope", "pruneThreshold", "prescribedPruneThreshold", "minNumIdentitiesInPotentialRole", "potentialRoleCount", "potentialRolesReadyCount", "type", "emailRecipientId", "identityCount", "saved", "name"]

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
        """Create an instance of RoleMiningSessionDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # set to None if prune_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.prune_threshold is None and "prune_threshold" in self.model_fields_set:
            _dict['pruneThreshold'] = None

        # set to None if prescribed_prune_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.prescribed_prune_threshold is None and "prescribed_prune_threshold" in self.model_fields_set:
            _dict['prescribedPruneThreshold'] = None

        # set to None if min_num_identities_in_potential_role (nullable) is None
        # and model_fields_set contains the field
        if self.min_num_identities_in_potential_role is None and "min_num_identities_in_potential_role" in self.model_fields_set:
            _dict['minNumIdentitiesInPotentialRole'] = None

        # set to None if email_recipient_id (nullable) is None
        # and model_fields_set contains the field
        if self.email_recipient_id is None and "email_recipient_id" in self.model_fields_set:
            _dict['emailRecipientId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoleMiningSessionDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scope": RoleMiningSessionScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "pruneThreshold": obj.get("pruneThreshold"),
            "prescribedPruneThreshold": obj.get("prescribedPruneThreshold"),
            "minNumIdentitiesInPotentialRole": obj.get("minNumIdentitiesInPotentialRole"),
            "potentialRoleCount": obj.get("potentialRoleCount"),
            "potentialRolesReadyCount": obj.get("potentialRolesReadyCount"),
            "type": obj.get("type"),
            "emailRecipientId": obj.get("emailRecipientId"),
            "identityCount": obj.get("identityCount"),
            "saved": obj.get("saved") if obj.get("saved") is not None else False,
            "name": obj.get("name")
        })
        return _obj


