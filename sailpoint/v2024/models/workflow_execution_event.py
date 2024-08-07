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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowExecutionEvent(BaseModel):
    """
    WorkflowExecutionEvent
    """ # noqa: E501
    type: Optional[Dict[str, Any]] = Field(default=None, description="The type of event")
    timestamp: Optional[datetime] = Field(default=None, description="The date-time when the event occurred")
    attributes: Optional[Dict[str, Any]] = Field(default=None, description="Additional attributes associated with the event")
    __properties: ClassVar[List[str]] = ["type", "timestamp", "attributes"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('WorkflowExecutionScheduled', 'WorkflowExecutionStarted', 'WorkflowExecutionCompleted', 'WorkflowExecutionFailed', 'WorkflowTaskScheduled', 'WorkflowTaskStarted', 'WorkflowTaskCompleted', 'WorkflowTaskFailed', 'ActivityTaskScheduled', 'ActivityTaskStarted', 'ActivityTaskCompleted', 'ActivityTaskFailed'):
            raise ValueError("must be one of enum values ('WorkflowExecutionScheduled', 'WorkflowExecutionStarted', 'WorkflowExecutionCompleted', 'WorkflowExecutionFailed', 'WorkflowTaskScheduled', 'WorkflowTaskStarted', 'WorkflowTaskCompleted', 'WorkflowTaskFailed', 'ActivityTaskScheduled', 'ActivityTaskStarted', 'ActivityTaskCompleted', 'ActivityTaskFailed')")
        return value

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
        """Create an instance of WorkflowExecutionEvent from a JSON string"""
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
        """Create an instance of WorkflowExecutionEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "attributes": obj.get("attributes")
        })
        return _obj


