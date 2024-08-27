# WorkItemsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open** | **int** | The count of open work items | [optional] 
**completed** | **int** | The count of completed work items | [optional] 
**total** | **int** | The count of total work items | [optional] 

## Example

```python
from sailpoint.v2024.models.work_items_summary import WorkItemsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemsSummary from a JSON string
work_items_summary_instance = WorkItemsSummary.from_json(json)
# print the JSON string representation of the object
print(WorkItemsSummary.to_json())

# convert the object into a dict
work_items_summary_dict = work_items_summary_instance.to_dict()
# create an instance of WorkItemsSummary from a dict
work_items_summary_from_dict = WorkItemsSummary.from_dict(work_items_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


