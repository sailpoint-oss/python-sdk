# AccessItemAssociated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_item** | [**AccessItemAssociatedAccessItem**](AccessItemAssociatedAccessItem.md) |  | [optional] 
**identity_id** | **str** | the identity id | [optional] 
**event_type** | **str** | the event type | [optional] 
**dt** | **str** | the date of event | [optional] 
**governance_event** | [**CorrelatedGovernanceEvent**](CorrelatedGovernanceEvent.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_item_associated import AccessItemAssociated

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemAssociated from a JSON string
access_item_associated_instance = AccessItemAssociated.from_json(json)
# print the JSON string representation of the object
print(AccessItemAssociated.to_json())

# convert the object into a dict
access_item_associated_dict = access_item_associated_instance.to_dict()
# create an instance of AccessItemAssociated from a dict
access_item_associated_from_dict = AccessItemAssociated.from_dict(access_item_associated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


