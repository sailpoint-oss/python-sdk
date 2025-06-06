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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2025.models.campaign_alert import CampaignAlert
from typing import Optional, Set
from typing_extensions import Self

class SlimCampaign(BaseModel):
    """
    SlimCampaign
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Id of the campaign")
    name: StrictStr = Field(description="The campaign name. If this object is part of a template, special formatting applies; see the `/campaign-templates/{id}/generate` endpoint documentation for details. ")
    description: Optional[StrictStr] = Field(description="The campaign description. If this object is part of a template, special formatting applies; see the `/campaign-templates/{id}/generate` endpoint documentation for details. ")
    deadline: Optional[datetime] = Field(default=None, description="The campaign's completion deadline.  This date must be in the future in order to activate the campaign.  If you try to activate a campaign with a deadline of today or in the past, you will receive a 400 error response.")
    type: StrictStr = Field(description="The type of campaign. Could be extended in the future.")
    email_notification_enabled: Optional[StrictBool] = Field(default=False, description="Enables email notification for this campaign", alias="emailNotificationEnabled")
    auto_revoke_allowed: Optional[StrictBool] = Field(default=False, description="Allows auto revoke for this campaign", alias="autoRevokeAllowed")
    recommendations_enabled: Optional[StrictBool] = Field(default=False, description="Enables IAI for this campaign. Accepts true even if the IAI product feature is off. If IAI is turned off then campaigns generated from this template will indicate false. The real value will then be returned if IAI is ever enabled for the org in the future.", alias="recommendationsEnabled")
    status: Optional[StrictStr] = Field(default=None, description="The campaign's current status.")
    correlated_status: Optional[StrictStr] = Field(default=None, description="The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source).", alias="correlatedStatus")
    created: Optional[datetime] = Field(default=None, description="Created time of the campaign")
    total_certifications: Optional[StrictInt] = Field(default=None, description="The total number of certifications in this campaign.", alias="totalCertifications")
    completed_certifications: Optional[StrictInt] = Field(default=None, description="The number of completed certifications in this campaign.", alias="completedCertifications")
    alerts: Optional[List[CampaignAlert]] = Field(default=None, description="A list of errors and warnings that have accumulated.")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "deadline", "type", "emailNotificationEnabled", "autoRevokeAllowed", "recommendationsEnabled", "status", "correlatedStatus", "created", "totalCertifications", "completedCertifications", "alerts"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MANAGER', 'SOURCE_OWNER', 'SEARCH', 'ROLE_COMPOSITION', 'MACHINE_ACCOUNT']):
            warnings.warn(f"must be one of enum values ('MANAGER', 'SOURCE_OWNER', 'SEARCH', 'ROLE_COMPOSITION', 'MACHINE_ACCOUNT') unknown value: {value}")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PENDING', 'STAGED', 'CANCELING', 'ACTIVATING', 'ACTIVE', 'COMPLETING', 'COMPLETED', 'ERROR', 'ARCHIVED']):
            warnings.warn(f"must be one of enum values ('PENDING', 'STAGED', 'CANCELING', 'ACTIVATING', 'ACTIVE', 'COMPLETING', 'COMPLETED', 'ERROR', 'ARCHIVED') unknown value: {value}")
        return value

    @field_validator('correlated_status')
    def correlated_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CORRELATED', 'UNCORRELATED']):
            warnings.warn(f"must be one of enum values ('CORRELATED', 'UNCORRELATED') unknown value: {value}")
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
        """Create an instance of SlimCampaign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "status",
            "created",
            "total_certifications",
            "completed_certifications",
            "alerts",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in alerts (list)
        _items = []
        if self.alerts:
            for _item_alerts in self.alerts:
                if _item_alerts:
                    _items.append(_item_alerts.to_dict())
            _dict['alerts'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if deadline (nullable) is None
        # and model_fields_set contains the field
        if self.deadline is None and "deadline" in self.model_fields_set:
            _dict['deadline'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if total_certifications (nullable) is None
        # and model_fields_set contains the field
        if self.total_certifications is None and "total_certifications" in self.model_fields_set:
            _dict['totalCertifications'] = None

        # set to None if completed_certifications (nullable) is None
        # and model_fields_set contains the field
        if self.completed_certifications is None and "completed_certifications" in self.model_fields_set:
            _dict['completedCertifications'] = None

        # set to None if alerts (nullable) is None
        # and model_fields_set contains the field
        if self.alerts is None and "alerts" in self.model_fields_set:
            _dict['alerts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlimCampaign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "deadline": obj.get("deadline"),
            "type": obj.get("type"),
            "emailNotificationEnabled": obj.get("emailNotificationEnabled") if obj.get("emailNotificationEnabled") is not None else False,
            "autoRevokeAllowed": obj.get("autoRevokeAllowed") if obj.get("autoRevokeAllowed") is not None else False,
            "recommendationsEnabled": obj.get("recommendationsEnabled") if obj.get("recommendationsEnabled") is not None else False,
            "status": obj.get("status"),
            "correlatedStatus": obj.get("correlatedStatus"),
            "created": obj.get("created"),
            "totalCertifications": obj.get("totalCertifications"),
            "completedCertifications": obj.get("completedCertifications"),
            "alerts": [CampaignAlert.from_dict(_item) for _item in obj["alerts"]] if obj.get("alerts") is not None else None
        })
        return _obj


