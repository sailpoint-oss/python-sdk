# LoadAccountsTaskTaskAttributes

Extra attributes map(dictionary) for the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The id of the source | [optional] 
**optimized_aggregation** | **str** | The indicator if the aggregation process was enabled/disabled for the aggregation job | [optional] 

## Example

```python
from sailpoint.v2024.models.load_accounts_task_task_attributes import LoadAccountsTaskTaskAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LoadAccountsTaskTaskAttributes from a JSON string
load_accounts_task_task_attributes_instance = LoadAccountsTaskTaskAttributes.from_json(json)
# print the JSON string representation of the object
print LoadAccountsTaskTaskAttributes.to_json()

# convert the object into a dict
load_accounts_task_task_attributes_dict = load_accounts_task_task_attributes_instance.to_dict()
# create an instance of LoadAccountsTaskTaskAttributes from a dict
load_accounts_task_task_attributes_form_dict = load_accounts_task_task_attributes.from_dict(load_accounts_task_task_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


