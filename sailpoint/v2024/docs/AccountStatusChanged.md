# AccountStatusChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | the event type | [optional] 
**identity_id** | **str** | the identity id | [optional] 
**dt** | **str** | the date of event | [optional] 
**account** | [**AccountStatusChangedAccount**](AccountStatusChangedAccount.md) |  | [optional] 
**status_change** | [**AccountStatusChangedStatusChange**](AccountStatusChangedStatusChange.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.account_status_changed import AccountStatusChanged

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatusChanged from a JSON string
account_status_changed_instance = AccountStatusChanged.from_json(json)
# print the JSON string representation of the object
print(AccountStatusChanged.to_json())

# convert the object into a dict
account_status_changed_dict = account_status_changed_instance.to_dict()
# create an instance of AccountStatusChanged from a dict
account_status_changed_from_dict = AccountStatusChanged.from_dict(account_status_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


