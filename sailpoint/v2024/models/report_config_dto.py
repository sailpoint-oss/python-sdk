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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReportConfigDTO(BaseModel):
    """
    ReportConfigDTO
    """ # noqa: E501
    column_name: Optional[StrictStr] = Field(default=None, description="Name of column in report", alias="columnName")
    required: Optional[StrictBool] = Field(default=False, description="If true, column is required in all reports, and this entry is immutable. A 400 error will result from any attempt to modify the column's definition.")
    included: Optional[StrictBool] = Field(default=False, description="If true, column is included in the report. A 400 error will be thrown if an attempt is made to set included=false if required==true.")
    order: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="Relative sort order for the column. Columns will be displayed left-to-right in nondecreasing order.")
    __properties: ClassVar[List[str]] = ["columnName", "required", "included", "order"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReportConfigDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ReportConfigDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "columnName": obj.get("columnName"),
            "required": obj.get("required") if obj.get("required") is not None else False,
            "included": obj.get("included") if obj.get("included") is not None else False,
            "order": obj.get("order")
        })
        return _obj

