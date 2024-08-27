# LoadUncorrelatedAccountsTaskTaskAttributes

Extra attributes map(dictionary) for the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qpoc_job_id** | **str** | The id of qpoc job | [optional] 
**task_start_delay** | **object** | the task start delay value | [optional] 

## Example

```python
from sailpoint.v2024.models.load_uncorrelated_accounts_task_task_attributes import LoadUncorrelatedAccountsTaskTaskAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LoadUncorrelatedAccountsTaskTaskAttributes from a JSON string
load_uncorrelated_accounts_task_task_attributes_instance = LoadUncorrelatedAccountsTaskTaskAttributes.from_json(json)
# print the JSON string representation of the object
print(LoadUncorrelatedAccountsTaskTaskAttributes.to_json())

# convert the object into a dict
load_uncorrelated_accounts_task_task_attributes_dict = load_uncorrelated_accounts_task_task_attributes_instance.to_dict()
# create an instance of LoadUncorrelatedAccountsTaskTaskAttributes from a dict
load_uncorrelated_accounts_task_task_attributes_from_dict = LoadUncorrelatedAccountsTaskTaskAttributes.from_dict(load_uncorrelated_accounts_task_task_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


