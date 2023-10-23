# AccountStatusChangedStatusChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_status** | **str** | the previous status of the account | [optional] 
**new_status** | **str** | the new status of the account | [optional] 

## Example

```python
from beta.models.account_status_changed_status_change import AccountStatusChangedStatusChange

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatusChangedStatusChange from a JSON string
account_status_changed_status_change_instance = AccountStatusChangedStatusChange.from_json(json)
# print the JSON string representation of the object
print AccountStatusChangedStatusChange.to_json()

# convert the object into a dict
account_status_changed_status_change_dict = account_status_changed_status_change_instance.to_dict()
# create an instance of AccountStatusChangedStatusChange from a dict
account_status_changed_status_change_form_dict = account_status_changed_status_change.from_dict(account_status_changed_status_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


