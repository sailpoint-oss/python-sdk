# TriggerExampleInput

An example of the JSON payload that will be sent by the trigger to the subscribed service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_id** | **str** | The unique ID of the access request. | 
**requested_for** | [**List[AccessItemRequestedForDto]**](AccessItemRequestedForDto.md) | Identities access was requested for. | 
**requested_items** | [**List[AccessRequestPreApprovalRequestedItemsInner]**](AccessRequestPreApprovalRequestedItemsInner.md) | Details of the access items being requested. | 
**requested_by** | [**AccessItemRequesterDto**](AccessItemRequesterDto.md) |  | 
**requested_items_status** | [**List[AccessRequestPostApprovalRequestedItemsStatusInner]**](AccessRequestPostApprovalRequestedItemsStatusInner.md) | Details on the outcome of each access item. | 
**source** | [**AccountUncorrelatedSource**](AccountUncorrelatedSource.md) |  | 
**status** | **object** | The overall status of the collection. | 
**started** | **datetime** | The date and time when the account collection started. | 
**completed** | **datetime** | The date and time when the account collection finished. | 
**errors** | **List[str]** | A list of any accumulated error messages that occurred during provisioning. | 
**warnings** | **List[str]** | A list of any accumulated warning messages that occurred during provisioning. | 
**stats** | [**AccountsCollectedForAggregationStats**](AccountsCollectedForAggregationStats.md) |  | 
**identity** | [**IdentityDeletedIdentity**](IdentityDeletedIdentity.md) |  | 
**account** | [**AccountUncorrelatedAccount**](AccountUncorrelatedAccount.md) |  | 
**changes** | [**List[IdentityAttributesChangedChangesInner]**](IdentityAttributesChangedChangesInner.md) | A list of one or more identity attributes that changed on the identity. | 
**attributes** | **Dict[str, object]** | The attributes of the account. The contents of attributes depends on the account schema for the source. | 
**entitlement_count** | **int** | The number of entitlements associated with this account. | [optional] 
**campaign** | [**CampaignGeneratedCampaign**](CampaignGeneratedCampaign.md) |  | 
**certification** | [**CertificationSignedOffCertification**](CertificationSignedOffCertification.md) |  | 
**tracking_number** | **str** | The reference number of the provisioning request. Useful for tracking status in the Account Activity search interface. | 
**sources** | **str** | One or more sources that the provisioning transaction(s) were done against.  Sources are comma separated. | 
**action** | **str** | Origin of where the provisioning request came from. | [optional] 
**recipient** | [**ProvisioningCompletedRecipient**](ProvisioningCompletedRecipient.md) |  | 
**requester** | [**ProvisioningCompletedRequester**](ProvisioningCompletedRequester.md) |  | [optional] 
**account_requests** | [**List[ProvisioningCompletedAccountRequestsInner]**](ProvisioningCompletedAccountRequestsInner.md) | A list of provisioning instructions to perform on an account-by-account basis. | 
**file_name** | **str** | A name for the report file. | 
**owner_email** | **str** | The email address of the identity that owns the saved search. | 
**owner_name** | **str** | The name of the identity that owns the saved search. | 
**query** | **str** | The search query that was used to generate the report. | 
**search_name** | **str** | The name of the saved search. | 
**search_results** | [**SavedSearchCompleteSearchResults**](SavedSearchCompleteSearchResults.md) |  | 
**signed_s3_url** | **str** | The Amazon S3 URL to download the report from. | 
**uuid** | **str** | Source unique identifier for the identity. UUID is generated by the source system. | [optional] 
**id** | **str** | The unique ID of the source. | 
**native_identifier** | **str** | Unique ID of the account on the source. | 
**source_id** | **str** | The ID of the source. | 
**source_name** | **str** | The name of the source. | 
**identity_id** | **str** | The ID of the identity that is correlated with this account. | 
**identity_name** | **str** | The name of the identity that is correlated with this account. | 
**name** | **str** | The user friendly name of the source. | 
**type** | **str** | The connection type of the source. | 
**created** | **datetime** | The date and time the status change occurred. | 
**connector** | **str** | The connector type used to connect to the source. | 
**actor** | [**SourceUpdatedActor**](SourceUpdatedActor.md) |  | 
**deleted** | **datetime** | The date and time the source was deleted. | 
**modified** | **datetime** | The date and time the source was modified. | 
**application** | [**VAClusterStatusChangeEventApplication**](VAClusterStatusChangeEventApplication.md) |  | 
**health_check_result** | [**VAClusterStatusChangeEventHealthCheckResult**](VAClusterStatusChangeEventHealthCheckResult.md) |  | 
**previous_health_check_result** | [**VAClusterStatusChangeEventPreviousHealthCheckResult**](VAClusterStatusChangeEventPreviousHealthCheckResult.md) |  | 

## Example

```python
from sailpoint.v2024.models.trigger_example_input import TriggerExampleInput

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExampleInput from a JSON string
trigger_example_input_instance = TriggerExampleInput.from_json(json)
# print the JSON string representation of the object
print TriggerExampleInput.to_json()

# convert the object into a dict
trigger_example_input_dict = trigger_example_input_instance.to_dict()
# create an instance of TriggerExampleInput from a dict
trigger_example_input_form_dict = trigger_example_input.from_dict(trigger_example_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

