# PasswordStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The password change request ID | [optional] 
**state** | **str** | Password change state | [optional] 
**errors** | **List[str]** | The errors during the password change request | [optional] 
**source_ids** | **List[str]** | List of source IDs in the password change request | [optional] 

## Example

```python
from beta.models.password_status import PasswordStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordStatus from a JSON string
password_status_instance = PasswordStatus.from_json(json)
# print the JSON string representation of the object
print PasswordStatus.to_json()

# convert the object into a dict
password_status_dict = password_status_instance.to_dict()
# create an instance of PasswordStatus from a dict
password_status_form_dict = password_status.from_dict(password_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


