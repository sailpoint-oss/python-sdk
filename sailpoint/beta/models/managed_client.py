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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.managed_client_status_enum import ManagedClientStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class ManagedClient(BaseModel):
    """
    Managed Client
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ManagedClient ID")
    alert_key: Optional[StrictStr] = Field(default=None, description="ManagedClient alert key", alias="alertKey")
    api_gateway_base_url: Optional[StrictStr] = Field(default=None, description="ManagedClient gateway base url", alias="apiGatewayBaseUrl")
    cc_id: Optional[StrictInt] = Field(default=None, description="Previous CC ID to be used in data migration. (This field will be deleted after CC migration!)", alias="ccId")
    client_id: StrictStr = Field(description="The client ID used in API management", alias="clientId")
    cluster_id: StrictStr = Field(description="Cluster ID that the ManagedClient is linked to", alias="clusterId")
    cookbook: Optional[StrictStr] = Field(default=None, description="VA cookbook")
    description: StrictStr = Field(description="ManagedClient description")
    ip_address: Optional[StrictStr] = Field(default=None, description="The public IP address of the ManagedClient", alias="ipAddress")
    last_seen: Optional[datetime] = Field(default=None, description="When the ManagedClient was last seen by the server", alias="lastSeen")
    name: Optional[StrictStr] = Field(default=None, description="ManagedClient name")
    since_last_seen: Optional[StrictStr] = Field(default=None, description="Milliseconds since the ManagedClient has polled the server", alias="sinceLastSeen")
    status: Optional[ManagedClientStatusEnum] = Field(default=None, description="Status of the ManagedClient")
    type: StrictStr = Field(description="Type of the ManagedClient (VA, CCG)")
    va_download_url: Optional[StrictStr] = Field(default=None, description="ManagedClient VA download URL", alias="vaDownloadUrl")
    va_version: Optional[StrictStr] = Field(default=None, description="Version that the ManagedClient's VA is running", alias="vaVersion")
    secret: Optional[StrictStr] = Field(default=None, description="Client's apiKey")
    __properties: ClassVar[List[str]] = ["id", "alertKey", "apiGatewayBaseUrl", "ccId", "clientId", "clusterId", "cookbook", "description", "ipAddress", "lastSeen", "name", "sinceLastSeen", "status", "type", "vaDownloadUrl", "vaVersion", "secret"]

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
        """Create an instance of ManagedClient from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "alert_key",
            "api_gateway_base_url",
            "cookbook",
            "ip_address",
            "last_seen",
            "since_last_seen",
            "status",
            "va_download_url",
            "va_version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagedClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "alertKey": obj.get("alertKey"),
            "apiGatewayBaseUrl": obj.get("apiGatewayBaseUrl"),
            "ccId": obj.get("ccId"),
            "clientId": obj.get("clientId"),
            "clusterId": obj.get("clusterId"),
            "cookbook": obj.get("cookbook"),
            "description": obj.get("description"),
            "ipAddress": obj.get("ipAddress"),
            "lastSeen": obj.get("lastSeen"),
            "name": obj.get("name"),
            "sinceLastSeen": obj.get("sinceLastSeen"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "vaDownloadUrl": obj.get("vaDownloadUrl"),
            "vaVersion": obj.get("vaVersion"),
            "secret": obj.get("secret")
        })
        return _obj


