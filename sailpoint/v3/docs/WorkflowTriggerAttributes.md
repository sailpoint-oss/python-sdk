# WorkflowTriggerAttributes

Workflow Trigger Attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the trigger | 
**filter_** | **str** | JSON path expression that will limit which events the trigger will fire on | [optional] 
**description** | **str** | Additonal context about the external trigger | [optional] 
**attribute_to_filter** | **str** | The attribute to filter on | [optional] 
**name** | **str** | A unique name for the external trigger | [optional] 
**client_id** | **str** | OAuth Client ID to authenticate with this trigger | [optional] 
**url** | **str** | URL to invoke this workflow | [optional] 
**cron_string** | **str** | A valid CRON expression | [optional] 
**frequency** | **str** | Frequency of execution | 
**time_zone** | **str** | Time zone identifier | [optional] 
**weekly_days** | **List[str]** | Scheduled days of the week for execution | [optional] 
**weekly_times** | **List[str]** | Scheduled execution times | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_trigger_attributes import WorkflowTriggerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTriggerAttributes from a JSON string
workflow_trigger_attributes_instance = WorkflowTriggerAttributes.from_json(json)
# print the JSON string representation of the object
print(WorkflowTriggerAttributes.to_json())

# convert the object into a dict
workflow_trigger_attributes_dict = workflow_trigger_attributes_instance.to_dict()
# create an instance of WorkflowTriggerAttributes from a dict
workflow_trigger_attributes_from_dict = WorkflowTriggerAttributes.from_dict(workflow_trigger_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


