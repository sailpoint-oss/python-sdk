# BaseAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**account_id** | **str** | Account ID. | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 
**disabled** | **bool** | Indicates whether the account is disabled. | [optional] [default to False]
**locked** | **bool** | Indicates whether the account is locked. | [optional] [default to False]
**privileged** | **bool** | Indicates whether the account is privileged. | [optional] [default to False]
**manually_correlated** | **bool** | Indicates whether the account has been manually correlated to an identity. | [optional] [default to False]
**password_last_set** | **datetime** | A date-time in ISO-8601 format | [optional] 
**entitlement_attributes** | **Dict[str, object]** | Map or dictionary of key/value pairs. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**supports_password_change** | **bool** | Indicates whether the account supports password change. | [optional] [default to False]
**account_attributes** | **Dict[str, object]** | Map or dictionary of key/value pairs. | [optional] 

## Example

```python
from sailpoint.v2024.models.base_account import BaseAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccount from a JSON string
base_account_instance = BaseAccount.from_json(json)
# print the JSON string representation of the object
print(BaseAccount.to_json())

# convert the object into a dict
base_account_dict = base_account_instance.to_dict()
# create an instance of BaseAccount from a dict
base_account_from_dict = BaseAccount.from_dict(base_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


