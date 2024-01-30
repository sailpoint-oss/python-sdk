# AccessProfileBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_profile_ids** | **List[str]** | List of IDs of Access Profiles to be deleted. | [optional] 
**best_effort_only** | **bool** | If **true**, silently skip over any of the specified Access Profiles if they cannot be deleted because they are in use. If **false**, no deletions will be attempted if any of the Access Profiles are in use. | [optional] 

## Example

```python
from sailpoint.beta.models.access_profile_bulk_delete_request import AccessProfileBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileBulkDeleteRequest from a JSON string
access_profile_bulk_delete_request_instance = AccessProfileBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print AccessProfileBulkDeleteRequest.to_json()

# convert the object into a dict
access_profile_bulk_delete_request_dict = access_profile_bulk_delete_request_instance.to_dict()
# create an instance of AccessProfileBulkDeleteRequest from a dict
access_profile_bulk_delete_request_form_dict = access_profile_bulk_delete_request.from_dict(access_profile_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


