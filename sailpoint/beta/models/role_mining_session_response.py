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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.role_mining_role_type import RoleMiningRoleType
from sailpoint.beta.models.role_mining_session_response_created_by import RoleMiningSessionResponseCreatedBy
from sailpoint.beta.models.role_mining_session_scope import RoleMiningSessionScope
from sailpoint.beta.models.role_mining_session_status import RoleMiningSessionStatus
from typing import Optional, Set
from typing_extensions import Self

class RoleMiningSessionResponse(BaseModel):
    """
    RoleMiningSessionResponse
    """ # noqa: E501
    scope: Optional[RoleMiningSessionScope] = None
    min_num_identities_in_potential_role: Optional[StrictInt] = Field(default=None, description="Minimum number of identities in a potential role", alias="minNumIdentitiesInPotentialRole")
    scoping_method: Optional[StrictStr] = Field(default=None, description="The scoping method of the role mining session", alias="scopingMethod")
    prescribed_prune_threshold: Optional[StrictInt] = Field(default=None, description="The computed (or prescribed) prune threshold for this session", alias="prescribedPruneThreshold")
    prune_threshold: Optional[StrictInt] = Field(default=None, description="The prune threshold to be used for this role mining session", alias="pruneThreshold")
    potential_role_count: Optional[StrictInt] = Field(default=None, description="The number of potential roles", alias="potentialRoleCount")
    potential_roles_ready_count: Optional[StrictInt] = Field(default=None, description="The number of potential roles which have completed processing", alias="potentialRolesReadyCount")
    status: Optional[RoleMiningSessionStatus] = None
    email_recipient_id: Optional[StrictStr] = Field(default=None, description="The id of the user who will receive an email about the role mining session", alias="emailRecipientId")
    created_by: Optional[RoleMiningSessionResponseCreatedBy] = Field(default=None, alias="createdBy")
    identity_count: Optional[StrictInt] = Field(default=None, description="The number of identities", alias="identityCount")
    saved: Optional[StrictBool] = Field(default=False, description="The session's saved status")
    name: Optional[StrictStr] = Field(default=None, description="The session's saved name")
    data_file_path: Optional[StrictStr] = Field(default=None, description="The data file path of the role mining session", alias="dataFilePath")
    id: Optional[StrictStr] = Field(default=None, description="Session Id for this role mining session")
    created_date: Optional[datetime] = Field(default=None, description="The date-time when this role mining session was created.", alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, description="The date-time when this role mining session was completed.", alias="modifiedDate")
    type: Optional[RoleMiningRoleType] = None
    __properties: ClassVar[List[str]] = ["scope", "minNumIdentitiesInPotentialRole", "scopingMethod", "prescribedPruneThreshold", "pruneThreshold", "potentialRoleCount", "potentialRolesReadyCount", "status", "emailRecipientId", "createdBy", "identityCount", "saved", "name", "dataFilePath", "id", "createdDate", "modifiedDate", "type"]

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
        """Create an instance of RoleMiningSessionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # set to None if min_num_identities_in_potential_role (nullable) is None
        # and model_fields_set contains the field
        if self.min_num_identities_in_potential_role is None and "min_num_identities_in_potential_role" in self.model_fields_set:
            _dict['minNumIdentitiesInPotentialRole'] = None

        # set to None if scoping_method (nullable) is None
        # and model_fields_set contains the field
        if self.scoping_method is None and "scoping_method" in self.model_fields_set:
            _dict['scopingMethod'] = None

        # set to None if prescribed_prune_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.prescribed_prune_threshold is None and "prescribed_prune_threshold" in self.model_fields_set:
            _dict['prescribedPruneThreshold'] = None

        # set to None if prune_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.prune_threshold is None and "prune_threshold" in self.model_fields_set:
            _dict['pruneThreshold'] = None

        # set to None if email_recipient_id (nullable) is None
        # and model_fields_set contains the field
        if self.email_recipient_id is None and "email_recipient_id" in self.model_fields_set:
            _dict['emailRecipientId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if data_file_path (nullable) is None
        # and model_fields_set contains the field
        if self.data_file_path is None and "data_file_path" in self.model_fields_set:
            _dict['dataFilePath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoleMiningSessionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scope": RoleMiningSessionScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "minNumIdentitiesInPotentialRole": obj.get("minNumIdentitiesInPotentialRole"),
            "scopingMethod": obj.get("scopingMethod"),
            "prescribedPruneThreshold": obj.get("prescribedPruneThreshold"),
            "pruneThreshold": obj.get("pruneThreshold"),
            "potentialRoleCount": obj.get("potentialRoleCount"),
            "potentialRolesReadyCount": obj.get("potentialRolesReadyCount"),
            "status": RoleMiningSessionStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "emailRecipientId": obj.get("emailRecipientId"),
            "createdBy": RoleMiningSessionResponseCreatedBy.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "identityCount": obj.get("identityCount"),
            "saved": obj.get("saved") if obj.get("saved") is not None else False,
            "name": obj.get("name"),
            "dataFilePath": obj.get("dataFilePath"),
            "id": obj.get("id"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "type": obj.get("type")
        })
        return _obj


