# WorkflowModifiedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** | Identity ID | [optional] 
**name** | **str** | Human-readable display name of identity. | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_modified_by import WorkflowModifiedBy

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowModifiedBy from a JSON string
workflow_modified_by_instance = WorkflowModifiedBy.from_json(json)
# print the JSON string representation of the object
print WorkflowModifiedBy.to_json()

# convert the object into a dict
workflow_modified_by_dict = workflow_modified_by_instance.to_dict()
# create an instance of WorkflowModifiedBy from a dict
workflow_modified_by_form_dict = workflow_modified_by.from_dict(workflow_modified_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


