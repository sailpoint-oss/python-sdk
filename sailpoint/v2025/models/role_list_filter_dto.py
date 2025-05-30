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
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2025.models.role_list_filter_dto_amm_key_values_inner import RoleListFilterDTOAmmKeyValuesInner
from typing import Optional, Set
from typing_extensions import Self

class RoleListFilterDTO(BaseModel):
    """
    AMMFilterValues
    """ # noqa: E501
    filters: Optional[StrictStr] = Field(default=None, description="Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, sw*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in*  **requestable**: *eq*")
    amm_key_values: Optional[List[RoleListFilterDTOAmmKeyValuesInner]] = Field(default=None, alias="ammKeyValues")
    __properties: ClassVar[List[str]] = ["filters", "ammKeyValues"]

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
        """Create an instance of RoleListFilterDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in amm_key_values (list)
        _items = []
        if self.amm_key_values:
            for _item_amm_key_values in self.amm_key_values:
                if _item_amm_key_values:
                    _items.append(_item_amm_key_values.to_dict())
            _dict['ammKeyValues'] = _items
        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if amm_key_values (nullable) is None
        # and model_fields_set contains the field
        if self.amm_key_values is None and "amm_key_values" in self.model_fields_set:
            _dict['ammKeyValues'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoleListFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filters": obj.get("filters"),
            "ammKeyValues": [RoleListFilterDTOAmmKeyValuesInner.from_dict(_item) for _item in obj["ammKeyValues"]] if obj.get("ammKeyValues") is not None else None
        })
        return _obj


