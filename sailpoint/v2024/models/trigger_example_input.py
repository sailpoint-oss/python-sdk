# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from sailpoint.v2024.models.access_request_dynamic_approver import AccessRequestDynamicApprover
from sailpoint.v2024.models.access_request_post_approval import AccessRequestPostApproval
from sailpoint.v2024.models.access_request_pre_approval import AccessRequestPreApproval
from sailpoint.v2024.models.account_aggregation_completed import AccountAggregationCompleted
from sailpoint.v2024.models.account_attributes_changed import AccountAttributesChanged
from sailpoint.v2024.models.account_correlated import AccountCorrelated
from sailpoint.v2024.models.account_uncorrelated import AccountUncorrelated
from sailpoint.v2024.models.accounts_collected_for_aggregation import AccountsCollectedForAggregation
from sailpoint.v2024.models.campaign_activated import CampaignActivated
from sailpoint.v2024.models.campaign_ended import CampaignEnded
from sailpoint.v2024.models.campaign_generated import CampaignGenerated
from sailpoint.v2024.models.certification_signed_off import CertificationSignedOff
from sailpoint.v2024.models.identity_attributes_changed import IdentityAttributesChanged
from sailpoint.v2024.models.identity_created import IdentityCreated
from sailpoint.v2024.models.identity_deleted import IdentityDeleted
from sailpoint.v2024.models.provisioning_completed import ProvisioningCompleted
from sailpoint.v2024.models.saved_search_complete import SavedSearchComplete
from sailpoint.v2024.models.source_account_created import SourceAccountCreated
from sailpoint.v2024.models.source_account_deleted import SourceAccountDeleted
from sailpoint.v2024.models.source_account_updated import SourceAccountUpdated
from sailpoint.v2024.models.source_created import SourceCreated
from sailpoint.v2024.models.source_deleted import SourceDeleted
from sailpoint.v2024.models.source_updated import SourceUpdated
from sailpoint.v2024.models.va_cluster_status_change_event import VAClusterStatusChangeEvent
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

TRIGGEREXAMPLEINPUT_ONE_OF_SCHEMAS = ["AccessRequestDynamicApprover", "AccessRequestPostApproval", "AccessRequestPreApproval", "AccountAggregationCompleted", "AccountAttributesChanged", "AccountCorrelated", "AccountUncorrelated", "AccountsCollectedForAggregation", "CampaignActivated", "CampaignEnded", "CampaignGenerated", "CertificationSignedOff", "IdentityAttributesChanged", "IdentityCreated", "IdentityDeleted", "ProvisioningCompleted", "SavedSearchComplete", "SourceAccountCreated", "SourceAccountDeleted", "SourceAccountUpdated", "SourceCreated", "SourceDeleted", "SourceUpdated", "VAClusterStatusChangeEvent"]

class TriggerExampleInput(BaseModel):
    """
    An example of the JSON payload that will be sent by the trigger to the subscribed service.
    """
    # data type: AccessRequestDynamicApprover
    oneof_schema_1_validator: Optional[AccessRequestDynamicApprover] = None
    # data type: AccessRequestPostApproval
    oneof_schema_2_validator: Optional[AccessRequestPostApproval] = None
    # data type: AccessRequestPreApproval
    oneof_schema_3_validator: Optional[AccessRequestPreApproval] = None
    # data type: AccountAggregationCompleted
    oneof_schema_4_validator: Optional[AccountAggregationCompleted] = None
    # data type: AccountAttributesChanged
    oneof_schema_5_validator: Optional[AccountAttributesChanged] = None
    # data type: AccountCorrelated
    oneof_schema_6_validator: Optional[AccountCorrelated] = None
    # data type: AccountsCollectedForAggregation
    oneof_schema_7_validator: Optional[AccountsCollectedForAggregation] = None
    # data type: AccountUncorrelated
    oneof_schema_8_validator: Optional[AccountUncorrelated] = None
    # data type: CampaignActivated
    oneof_schema_9_validator: Optional[CampaignActivated] = None
    # data type: CampaignEnded
    oneof_schema_10_validator: Optional[CampaignEnded] = None
    # data type: CampaignGenerated
    oneof_schema_11_validator: Optional[CampaignGenerated] = None
    # data type: CertificationSignedOff
    oneof_schema_12_validator: Optional[CertificationSignedOff] = None
    # data type: IdentityAttributesChanged
    oneof_schema_13_validator: Optional[IdentityAttributesChanged] = None
    # data type: IdentityCreated
    oneof_schema_14_validator: Optional[IdentityCreated] = None
    # data type: IdentityDeleted
    oneof_schema_15_validator: Optional[IdentityDeleted] = None
    # data type: ProvisioningCompleted
    oneof_schema_16_validator: Optional[ProvisioningCompleted] = None
    # data type: SavedSearchComplete
    oneof_schema_17_validator: Optional[SavedSearchComplete] = None
    # data type: SourceAccountCreated
    oneof_schema_18_validator: Optional[SourceAccountCreated] = None
    # data type: SourceAccountDeleted
    oneof_schema_19_validator: Optional[SourceAccountDeleted] = None
    # data type: SourceAccountUpdated
    oneof_schema_20_validator: Optional[SourceAccountUpdated] = None
    # data type: SourceCreated
    oneof_schema_21_validator: Optional[SourceCreated] = None
    # data type: SourceDeleted
    oneof_schema_22_validator: Optional[SourceDeleted] = None
    # data type: SourceUpdated
    oneof_schema_23_validator: Optional[SourceUpdated] = None
    # data type: VAClusterStatusChangeEvent
    oneof_schema_24_validator: Optional[VAClusterStatusChangeEvent] = None
    actual_instance: Optional[Union[AccessRequestDynamicApprover, AccessRequestPostApproval, AccessRequestPreApproval, AccountAggregationCompleted, AccountAttributesChanged, AccountCorrelated, AccountUncorrelated, AccountsCollectedForAggregation, CampaignActivated, CampaignEnded, CampaignGenerated, CertificationSignedOff, IdentityAttributesChanged, IdentityCreated, IdentityDeleted, ProvisioningCompleted, SavedSearchComplete, SourceAccountCreated, SourceAccountDeleted, SourceAccountUpdated, SourceCreated, SourceDeleted, SourceUpdated, VAClusterStatusChangeEvent]] = None
    one_of_schemas: List[str] = Literal["AccessRequestDynamicApprover", "AccessRequestPostApproval", "AccessRequestPreApproval", "AccountAggregationCompleted", "AccountAttributesChanged", "AccountCorrelated", "AccountUncorrelated", "AccountsCollectedForAggregation", "CampaignActivated", "CampaignEnded", "CampaignGenerated", "CertificationSignedOff", "IdentityAttributesChanged", "IdentityCreated", "IdentityDeleted", "ProvisioningCompleted", "SavedSearchComplete", "SourceAccountCreated", "SourceAccountDeleted", "SourceAccountUpdated", "SourceCreated", "SourceDeleted", "SourceUpdated", "VAClusterStatusChangeEvent"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TriggerExampleInput.model_construct()
        error_messages = []
        match = 0
        # validate data type: AccessRequestDynamicApprover
        if not isinstance(v, AccessRequestDynamicApprover):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccessRequestDynamicApprover`")
        else:
            match += 1
        # validate data type: AccessRequestPostApproval
        if not isinstance(v, AccessRequestPostApproval):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccessRequestPostApproval`")
        else:
            match += 1
        # validate data type: AccessRequestPreApproval
        if not isinstance(v, AccessRequestPreApproval):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccessRequestPreApproval`")
        else:
            match += 1
        # validate data type: AccountAggregationCompleted
        if not isinstance(v, AccountAggregationCompleted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountAggregationCompleted`")
        else:
            match += 1
        # validate data type: AccountAttributesChanged
        if not isinstance(v, AccountAttributesChanged):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountAttributesChanged`")
        else:
            match += 1
        # validate data type: AccountCorrelated
        if not isinstance(v, AccountCorrelated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountCorrelated`")
        else:
            match += 1
        # validate data type: AccountsCollectedForAggregation
        if not isinstance(v, AccountsCollectedForAggregation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountsCollectedForAggregation`")
        else:
            match += 1
        # validate data type: AccountUncorrelated
        if not isinstance(v, AccountUncorrelated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountUncorrelated`")
        else:
            match += 1
        # validate data type: CampaignActivated
        if not isinstance(v, CampaignActivated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CampaignActivated`")
        else:
            match += 1
        # validate data type: CampaignEnded
        if not isinstance(v, CampaignEnded):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CampaignEnded`")
        else:
            match += 1
        # validate data type: CampaignGenerated
        if not isinstance(v, CampaignGenerated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CampaignGenerated`")
        else:
            match += 1
        # validate data type: CertificationSignedOff
        if not isinstance(v, CertificationSignedOff):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CertificationSignedOff`")
        else:
            match += 1
        # validate data type: IdentityAttributesChanged
        if not isinstance(v, IdentityAttributesChanged):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentityAttributesChanged`")
        else:
            match += 1
        # validate data type: IdentityCreated
        if not isinstance(v, IdentityCreated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentityCreated`")
        else:
            match += 1
        # validate data type: IdentityDeleted
        if not isinstance(v, IdentityDeleted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentityDeleted`")
        else:
            match += 1
        # validate data type: ProvisioningCompleted
        if not isinstance(v, ProvisioningCompleted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProvisioningCompleted`")
        else:
            match += 1
        # validate data type: SavedSearchComplete
        if not isinstance(v, SavedSearchComplete):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SavedSearchComplete`")
        else:
            match += 1
        # validate data type: SourceAccountCreated
        if not isinstance(v, SourceAccountCreated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAccountCreated`")
        else:
            match += 1
        # validate data type: SourceAccountDeleted
        if not isinstance(v, SourceAccountDeleted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAccountDeleted`")
        else:
            match += 1
        # validate data type: SourceAccountUpdated
        if not isinstance(v, SourceAccountUpdated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAccountUpdated`")
        else:
            match += 1
        # validate data type: SourceCreated
        if not isinstance(v, SourceCreated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceCreated`")
        else:
            match += 1
        # validate data type: SourceDeleted
        if not isinstance(v, SourceDeleted):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceDeleted`")
        else:
            match += 1
        # validate data type: SourceUpdated
        if not isinstance(v, SourceUpdated):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceUpdated`")
        else:
            match += 1
        # validate data type: VAClusterStatusChangeEvent
        if not isinstance(v, VAClusterStatusChangeEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VAClusterStatusChangeEvent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TriggerExampleInput with oneOf schemas: AccessRequestDynamicApprover, AccessRequestPostApproval, AccessRequestPreApproval, AccountAggregationCompleted, AccountAttributesChanged, AccountCorrelated, AccountUncorrelated, AccountsCollectedForAggregation, CampaignActivated, CampaignEnded, CampaignGenerated, CertificationSignedOff, IdentityAttributesChanged, IdentityCreated, IdentityDeleted, ProvisioningCompleted, SavedSearchComplete, SourceAccountCreated, SourceAccountDeleted, SourceAccountUpdated, SourceCreated, SourceDeleted, SourceUpdated, VAClusterStatusChangeEvent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TriggerExampleInput with oneOf schemas: AccessRequestDynamicApprover, AccessRequestPostApproval, AccessRequestPreApproval, AccountAggregationCompleted, AccountAttributesChanged, AccountCorrelated, AccountUncorrelated, AccountsCollectedForAggregation, CampaignActivated, CampaignEnded, CampaignGenerated, CertificationSignedOff, IdentityAttributesChanged, IdentityCreated, IdentityDeleted, ProvisioningCompleted, SavedSearchComplete, SourceAccountCreated, SourceAccountDeleted, SourceAccountUpdated, SourceCreated, SourceDeleted, SourceUpdated, VAClusterStatusChangeEvent. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AccessRequestDynamicApprover
        try:
            instance.actual_instance = AccessRequestDynamicApprover.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccessRequestPostApproval
        try:
            instance.actual_instance = AccessRequestPostApproval.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccessRequestPreApproval
        try:
            instance.actual_instance = AccessRequestPreApproval.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccountAggregationCompleted
        try:
            instance.actual_instance = AccountAggregationCompleted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccountAttributesChanged
        try:
            instance.actual_instance = AccountAttributesChanged.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccountCorrelated
        try:
            instance.actual_instance = AccountCorrelated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccountsCollectedForAggregation
        try:
            instance.actual_instance = AccountsCollectedForAggregation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccountUncorrelated
        try:
            instance.actual_instance = AccountUncorrelated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CampaignActivated
        try:
            instance.actual_instance = CampaignActivated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CampaignEnded
        try:
            instance.actual_instance = CampaignEnded.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CampaignGenerated
        try:
            instance.actual_instance = CampaignGenerated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CertificationSignedOff
        try:
            instance.actual_instance = CertificationSignedOff.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentityAttributesChanged
        try:
            instance.actual_instance = IdentityAttributesChanged.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentityCreated
        try:
            instance.actual_instance = IdentityCreated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentityDeleted
        try:
            instance.actual_instance = IdentityDeleted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProvisioningCompleted
        try:
            instance.actual_instance = ProvisioningCompleted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SavedSearchComplete
        try:
            instance.actual_instance = SavedSearchComplete.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAccountCreated
        try:
            instance.actual_instance = SourceAccountCreated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAccountDeleted
        try:
            instance.actual_instance = SourceAccountDeleted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAccountUpdated
        try:
            instance.actual_instance = SourceAccountUpdated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceCreated
        try:
            instance.actual_instance = SourceCreated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceDeleted
        try:
            instance.actual_instance = SourceDeleted.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceUpdated
        try:
            instance.actual_instance = SourceUpdated.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VAClusterStatusChangeEvent
        try:
            instance.actual_instance = VAClusterStatusChangeEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TriggerExampleInput with oneOf schemas: AccessRequestDynamicApprover, AccessRequestPostApproval, AccessRequestPreApproval, AccountAggregationCompleted, AccountAttributesChanged, AccountCorrelated, AccountUncorrelated, AccountsCollectedForAggregation, CampaignActivated, CampaignEnded, CampaignGenerated, CertificationSignedOff, IdentityAttributesChanged, IdentityCreated, IdentityDeleted, ProvisioningCompleted, SavedSearchComplete, SourceAccountCreated, SourceAccountDeleted, SourceAccountUpdated, SourceCreated, SourceDeleted, SourceUpdated, VAClusterStatusChangeEvent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TriggerExampleInput with oneOf schemas: AccessRequestDynamicApprover, AccessRequestPostApproval, AccessRequestPreApproval, AccountAggregationCompleted, AccountAttributesChanged, AccountCorrelated, AccountUncorrelated, AccountsCollectedForAggregation, CampaignActivated, CampaignEnded, CampaignGenerated, CertificationSignedOff, IdentityAttributesChanged, IdentityCreated, IdentityDeleted, ProvisioningCompleted, SavedSearchComplete, SourceAccountCreated, SourceAccountDeleted, SourceAccountUpdated, SourceCreated, SourceDeleted, SourceUpdated, VAClusterStatusChangeEvent. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

