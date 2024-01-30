# WorkflowTrigger

The trigger that starts the workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The trigger type | 
**attributes** | **object** | Workflow Trigger Attributes. | 

## Example

```python
from sailpoint.beta.models.workflow_trigger import WorkflowTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTrigger from a JSON string
workflow_trigger_instance = WorkflowTrigger.from_json(json)
# print the JSON string representation of the object
print WorkflowTrigger.to_json()

# convert the object into a dict
workflow_trigger_dict = workflow_trigger_instance.to_dict()
# create an instance of WorkflowTrigger from a dict
workflow_trigger_form_dict = workflow_trigger.from_dict(workflow_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


