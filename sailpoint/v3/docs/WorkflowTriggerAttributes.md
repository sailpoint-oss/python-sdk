# WorkflowTriggerAttributes

Workflow Trigger Attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the trigger | 
**filter_** | **str** | JSON path expression that will limit which events the trigger will fire on | [optional] 
**name** | **str** | A unique name for the external trigger | 
**description** | **str** | Additonal context about the external trigger | [optional] 
**cron_string** | **str** | A valid CRON expression | 

## Example

```python
from sailpoint.v3.models.workflow_trigger_attributes import WorkflowTriggerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTriggerAttributes from a JSON string
workflow_trigger_attributes_instance = WorkflowTriggerAttributes.from_json(json)
# print the JSON string representation of the object
print WorkflowTriggerAttributes.to_json()

# convert the object into a dict
workflow_trigger_attributes_dict = workflow_trigger_attributes_instance.to_dict()
# create an instance of WorkflowTriggerAttributes from a dict
workflow_trigger_attributes_form_dict = workflow_trigger_attributes.from_dict(workflow_trigger_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


