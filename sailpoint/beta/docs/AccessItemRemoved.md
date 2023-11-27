# AccessItemRemoved


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
from sailpoint.beta.models.access_item_removed import AccessItemRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemRemoved from a JSON string
access_item_removed_instance = AccessItemRemoved.from_json(json)
# print the JSON string representation of the object
print AccessItemRemoved.to_json()

# convert the object into a dict
access_item_removed_dict = access_item_removed_instance.to_dict()
# create an instance of AccessItemRemoved from a dict
access_item_removed_form_dict = access_item_removed.from_dict(access_item_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


