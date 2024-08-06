# GetHistoricalIdentityEvents200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_item** | [**AccessItemAssociatedAccessItem**](AccessItemAssociatedAccessItem.md) |  | [optional] 
**identity_id** | **str** | the identity id | [optional] 
**event_type** | **str** | the event type | [optional] 
**dt** | **str** | the date of event | [optional] 
**governance_event** | [**CorrelatedGovernanceEvent**](CorrelatedGovernanceEvent.md) |  | [optional] 
**changes** | [**List[AttributeChange]**](AttributeChange.md) |  | [optional] 
**access_request** | [**AccessRequestResponse**](AccessRequestResponse.md) |  | [optional] 
**certification_id** | **str** | the id of the certification item | [optional] 
**certification_name** | **str** | the certification item name | [optional] 
**signed_date** | **str** | the date ceritification was signed | [optional] 
**certifiers** | [**List[CertifierResponse]**](CertifierResponse.md) | this field is deprecated and may go away | [optional] 
**reviewers** | [**List[CertifierResponse]**](CertifierResponse.md) | The list of identities who review this certification | [optional] 
**signer** | [**CertifierResponse**](CertifierResponse.md) |  | [optional] 
**account** | [**AccountStatusChangedAccount**](AccountStatusChangedAccount.md) |  | [optional] 
**status_change** | [**AccountStatusChangedStatusChange**](AccountStatusChangedStatusChange.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.get_historical_identity_events200_response_inner import GetHistoricalIdentityEvents200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoricalIdentityEvents200ResponseInner from a JSON string
get_historical_identity_events200_response_inner_instance = GetHistoricalIdentityEvents200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetHistoricalIdentityEvents200ResponseInner.to_json()

# convert the object into a dict
get_historical_identity_events200_response_inner_dict = get_historical_identity_events200_response_inner_instance.to_dict()
# create an instance of GetHistoricalIdentityEvents200ResponseInner from a dict
get_historical_identity_events200_response_inner_form_dict = get_historical_identity_events200_response_inner.from_dict(get_historical_identity_events200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


