# AccessRequestAdminItemStatusSodViolationContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The status of SOD violation check | [optional] 
**uuid** | **str** | The id of the Violation check event | [optional] 
**violation_check_result** | [**SodViolationCheckResult1**](SodViolationCheckResult1.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_admin_item_status_sod_violation_context import AccessRequestAdminItemStatusSodViolationContext

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestAdminItemStatusSodViolationContext from a JSON string
access_request_admin_item_status_sod_violation_context_instance = AccessRequestAdminItemStatusSodViolationContext.from_json(json)
# print the JSON string representation of the object
print(AccessRequestAdminItemStatusSodViolationContext.to_json())

# convert the object into a dict
access_request_admin_item_status_sod_violation_context_dict = access_request_admin_item_status_sod_violation_context_instance.to_dict()
# create an instance of AccessRequestAdminItemStatusSodViolationContext from a dict
access_request_admin_item_status_sod_violation_context_from_dict = AccessRequestAdminItemStatusSodViolationContext.from_dict(access_request_admin_item_status_sod_violation_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


