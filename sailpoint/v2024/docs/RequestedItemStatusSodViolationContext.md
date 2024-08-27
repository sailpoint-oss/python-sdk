# RequestedItemStatusSodViolationContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The status of SOD violation check | [optional] 
**uuid** | **str** | The id of the Violation check event | [optional] 
**violation_check_result** | [**SodViolationCheckResult**](SodViolationCheckResult.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.requested_item_status_sod_violation_context import RequestedItemStatusSodViolationContext

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatusSodViolationContext from a JSON string
requested_item_status_sod_violation_context_instance = RequestedItemStatusSodViolationContext.from_json(json)
# print the JSON string representation of the object
print(RequestedItemStatusSodViolationContext.to_json())

# convert the object into a dict
requested_item_status_sod_violation_context_dict = requested_item_status_sod_violation_context_instance.to_dict()
# create an instance of RequestedItemStatusSodViolationContext from a dict
requested_item_status_sod_violation_context_from_dict = RequestedItemStatusSodViolationContext.from_dict(requested_item_status_sod_violation_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


