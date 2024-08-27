# PasswordSyncGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the sync group | [optional] 
**name** | **str** | Name of the sync group | [optional] 
**password_policy_id** | **str** | ID of the password policy | [optional] 
**source_ids** | **List[str]** | List of password managed sources IDs | [optional] 
**created** | **datetime** | The date and time this sync group was created | [optional] 
**modified** | **datetime** | The date and time this sync group was last modified | [optional] 

## Example

```python
from sailpoint.v3.models.password_sync_group import PasswordSyncGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSyncGroup from a JSON string
password_sync_group_instance = PasswordSyncGroup.from_json(json)
# print the JSON string representation of the object
print(PasswordSyncGroup.to_json())

# convert the object into a dict
password_sync_group_dict = password_sync_group_instance.to_dict()
# create an instance of PasswordSyncGroup from a dict
password_sync_group_from_dict = PasswordSyncGroup.from_dict(password_sync_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


