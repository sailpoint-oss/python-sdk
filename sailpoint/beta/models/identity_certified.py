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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.certifier_response import CertifierResponse
from typing import Optional, Set
from typing_extensions import Self

class IdentityCertified(BaseModel):
    """
    IdentityCertified
    """ # noqa: E501
    certification_id: Optional[StrictStr] = Field(default=None, description="the id of the certification item", alias="certificationId")
    certification_name: Optional[StrictStr] = Field(default=None, description="the certification item name", alias="certificationName")
    signed_date: Optional[StrictStr] = Field(default=None, description="the date ceritification was signed", alias="signedDate")
    certifiers: Optional[List[CertifierResponse]] = Field(default=None, description="this field is deprecated and may go away")
    reviewers: Optional[List[CertifierResponse]] = Field(default=None, description="The list of identities who review this certification")
    signer: Optional[CertifierResponse] = None
    event_type: Optional[StrictStr] = Field(default=None, description="the event type", alias="eventType")
    dt: Optional[StrictStr] = Field(default=None, description="the date of event")
    __properties: ClassVar[List[str]] = ["certificationId", "certificationName", "signedDate", "certifiers", "reviewers", "signer", "eventType", "dt"]

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
        """Create an instance of IdentityCertified from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in certifiers (list)
        _items = []
        if self.certifiers:
            for _item_certifiers in self.certifiers:
                if _item_certifiers:
                    _items.append(_item_certifiers.to_dict())
            _dict['certifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reviewers (list)
        _items = []
        if self.reviewers:
            for _item_reviewers in self.reviewers:
                if _item_reviewers:
                    _items.append(_item_reviewers.to_dict())
            _dict['reviewers'] = _items
        # override the default output from pydantic by calling `to_dict()` of signer
        if self.signer:
            _dict['signer'] = self.signer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentityCertified from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certificationId": obj.get("certificationId"),
            "certificationName": obj.get("certificationName"),
            "signedDate": obj.get("signedDate"),
            "certifiers": [CertifierResponse.from_dict(_item) for _item in obj["certifiers"]] if obj.get("certifiers") is not None else None,
            "reviewers": [CertifierResponse.from_dict(_item) for _item in obj["reviewers"]] if obj.get("reviewers") is not None else None,
            "signer": CertifierResponse.from_dict(obj["signer"]) if obj.get("signer") is not None else None,
            "eventType": obj.get("eventType"),
            "dt": obj.get("dt")
        })
        return _obj


