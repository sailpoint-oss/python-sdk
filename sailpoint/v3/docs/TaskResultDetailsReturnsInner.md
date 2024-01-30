# TaskResultDetailsReturnsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_label** | **str** | Attribute description. | [optional] 
**attribute_name** | **str** | System or database attribute name. | [optional] 

## Example

```python
from sailpoint.v3.models.task_result_details_returns_inner import TaskResultDetailsReturnsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResultDetailsReturnsInner from a JSON string
task_result_details_returns_inner_instance = TaskResultDetailsReturnsInner.from_json(json)
# print the JSON string representation of the object
print TaskResultDetailsReturnsInner.to_json()

# convert the object into a dict
task_result_details_returns_inner_dict = task_result_details_returns_inner_instance.to_dict()
# create an instance of TaskResultDetailsReturnsInner from a dict
task_result_details_returns_inner_form_dict = task_result_details_returns_inner.from_dict(task_result_details_returns_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


