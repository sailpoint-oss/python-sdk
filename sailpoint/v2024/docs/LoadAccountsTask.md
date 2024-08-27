# LoadAccountsTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | The status of the result | [optional] [default to True]
**task** | [**LoadAccountsTaskTask**](LoadAccountsTaskTask.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.load_accounts_task import LoadAccountsTask

# TODO update the JSON string below
json = "{}"
# create an instance of LoadAccountsTask from a JSON string
load_accounts_task_instance = LoadAccountsTask.from_json(json)
# print the JSON string representation of the object
print(LoadAccountsTask.to_json())

# convert the object into a dict
load_accounts_task_dict = load_accounts_task_instance.to_dict()
# create an instance of LoadAccountsTask from a dict
load_accounts_task_from_dict = LoadAccountsTask.from_dict(load_accounts_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


