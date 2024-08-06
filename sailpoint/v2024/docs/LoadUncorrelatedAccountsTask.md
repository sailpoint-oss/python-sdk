# LoadUncorrelatedAccountsTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | The status of the result | [optional] [default to True]
**task** | [**LoadUncorrelatedAccountsTaskTask**](LoadUncorrelatedAccountsTaskTask.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.load_uncorrelated_accounts_task import LoadUncorrelatedAccountsTask

# TODO update the JSON string below
json = "{}"
# create an instance of LoadUncorrelatedAccountsTask from a JSON string
load_uncorrelated_accounts_task_instance = LoadUncorrelatedAccountsTask.from_json(json)
# print the JSON string representation of the object
print LoadUncorrelatedAccountsTask.to_json()

# convert the object into a dict
load_uncorrelated_accounts_task_dict = load_uncorrelated_accounts_task_instance.to_dict()
# create an instance of LoadUncorrelatedAccountsTask from a dict
load_uncorrelated_accounts_task_form_dict = load_uncorrelated_accounts_task.from_dict(load_uncorrelated_accounts_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


