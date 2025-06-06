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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from sailpoint.v2025.models.json_patch_operation import JsonPatchOperation
from typing import Optional, Set
from typing_extensions import Self

class SourceAppBulkUpdateRequest(BaseModel):
    """
    SourceAppBulkUpdateRequest
    """ # noqa: E501
    app_ids: Annotated[List[StrictStr], Field(max_length=50)] = Field(description="List of source app ids to update", alias="appIds")
    json_patch: List[JsonPatchOperation] = Field(description="The JSONPatch payload used to update the source app.", alias="jsonPatch")
    __properties: ClassVar[List[str]] = ["appIds", "jsonPatch"]

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
        """Create an instance of SourceAppBulkUpdateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in json_patch (list)
        _items = []
        if self.json_patch:
            for _item_json_patch in self.json_patch:
                if _item_json_patch:
                    _items.append(_item_json_patch.to_dict())
            _dict['jsonPatch'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceAppBulkUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appIds": obj.get("appIds"),
            "jsonPatch": [JsonPatchOperation.from_dict(_item) for _item in obj["jsonPatch"]] if obj.get("jsonPatch") is not None else None
        })
        return _obj


