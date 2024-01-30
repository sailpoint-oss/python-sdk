# BaseAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**account_id** | **str** | The ID of the account | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 
**disabled** | **bool** | Indicates if the account is disabled | [optional] 
**locked** | **bool** | Indicates if the account is locked | [optional] 
**privileged** | **bool** |  | [optional] 
**manually_correlated** | **bool** | Indicates if the account has been manually correlated to an identity | [optional] 
**password_last_set** | **datetime** | A date-time in ISO-8601 format | [optional] 
**entitlement_attributes** | **Dict[str, object]** | a map or dictionary of key/value pairs | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 

## Example

```python
from sailpoint.v3.models.base_account import BaseAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccount from a JSON string
base_account_instance = BaseAccount.from_json(json)
# print the JSON string representation of the object
print BaseAccount.to_json()

# convert the object into a dict
base_account_dict = base_account_instance.to_dict()
# create an instance of BaseAccount from a dict
base_account_form_dict = base_account.from_dict(base_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


