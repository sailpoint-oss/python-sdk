# UpdateUserPermissionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** |  | [optional] 
**is_admin** | **str** | Indicates if user should be an IDN Admin.  \&quot;0\&quot; for false, \&quot;1\&quot; for true. | [optional] 
**admin_type** | **str** |  | [optional] 

## Example

```python
from cc.models.update_user_permissions_request import UpdateUserPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPermissionsRequest from a JSON string
update_user_permissions_request_instance = UpdateUserPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateUserPermissionsRequest.to_json()

# convert the object into a dict
update_user_permissions_request_dict = update_user_permissions_request_instance.to_dict()
# create an instance of UpdateUserPermissionsRequest from a dict
update_user_permissions_request_form_dict = update_user_permissions_request.from_dict(update_user_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


