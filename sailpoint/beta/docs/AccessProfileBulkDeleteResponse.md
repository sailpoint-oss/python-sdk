# AccessProfileBulkDeleteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | ID of the task which is executing the bulk deletion. This can be passed to the **/task-status** API to track status. | [optional] 
**pending** | **List[str]** | List of IDs of Access Profiles which are pending deletion. | [optional] 
**in_use** | [**List[AccessProfileUsage]**](AccessProfileUsage.md) | List of usages of Access Profiles targeted for deletion. | [optional] 

## Example

```python
from sailpoint.beta.models.access_profile_bulk_delete_response import AccessProfileBulkDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileBulkDeleteResponse from a JSON string
access_profile_bulk_delete_response_instance = AccessProfileBulkDeleteResponse.from_json(json)
# print the JSON string representation of the object
print AccessProfileBulkDeleteResponse.to_json()

# convert the object into a dict
access_profile_bulk_delete_response_dict = access_profile_bulk_delete_response_instance.to_dict()
# create an instance of AccessProfileBulkDeleteResponse from a dict
access_profile_bulk_delete_response_form_dict = access_profile_bulk_delete_response.from_dict(access_profile_bulk_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


