# CorrelatedGovernanceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the governance event, such as the certification name or access request ID. | [optional] 
**dt** | **str** | The date that the certification or access request was completed. | [optional] 
**type** | **str** | The type of governance event. | [optional] 
**governance_id** | **str** | The ID of the instance that caused the event - either the certification ID or access request ID. | [optional] 
**owners** | [**List[CertifierResponse]**](CertifierResponse.md) | The owners of the governance event (the certifiers or approvers) | [optional] 
**reviewers** | [**List[CertifierResponse]**](CertifierResponse.md) | The owners of the governance event (the certifiers or approvers), this field should be preferred over owners | [optional] 
**decision_maker** | [**CertifierResponse**](CertifierResponse.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.correlated_governance_event import CorrelatedGovernanceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelatedGovernanceEvent from a JSON string
correlated_governance_event_instance = CorrelatedGovernanceEvent.from_json(json)
# print the JSON string representation of the object
print CorrelatedGovernanceEvent.to_json()

# convert the object into a dict
correlated_governance_event_dict = correlated_governance_event_instance.to_dict()
# create an instance of CorrelatedGovernanceEvent from a dict
correlated_governance_event_form_dict = correlated_governance_event.from_dict(correlated_governance_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


