# WorkflowAllOfCreator

Workflow creator's identity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Workflow creator&#39;s DTO type. | [optional] 
**id** | **str** | Workflow creator&#39;s identity ID. | [optional] 
**name** | **str** | Workflow creator&#39;s display name. | [optional] 

## Example

```python
from beta.models.workflow_all_of_creator import WorkflowAllOfCreator

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAllOfCreator from a JSON string
workflow_all_of_creator_instance = WorkflowAllOfCreator.from_json(json)
# print the JSON string representation of the object
print WorkflowAllOfCreator.to_json()

# convert the object into a dict
workflow_all_of_creator_dict = workflow_all_of_creator_instance.to_dict()
# create an instance of WorkflowAllOfCreator from a dict
workflow_all_of_creator_form_dict = workflow_all_of_creator.from_dict(workflow_all_of_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


