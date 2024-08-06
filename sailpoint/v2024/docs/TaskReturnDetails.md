# TaskReturnDetails

Task return details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the TaskReturnDetails | 
**attribute_name** | **str** | Attribute the TaskReturnDetails is for | 

## Example

```python
from sailpoint.v2024.models.task_return_details import TaskReturnDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TaskReturnDetails from a JSON string
task_return_details_instance = TaskReturnDetails.from_json(json)
# print the JSON string representation of the object
print TaskReturnDetails.to_json()

# convert the object into a dict
task_return_details_dict = task_return_details_instance.to_dict()
# create an instance of TaskReturnDetails from a dict
task_return_details_form_dict = task_return_details.from_dict(task_return_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


