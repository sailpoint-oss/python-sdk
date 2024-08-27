# TriggerExampleOutput

An example of the JSON payload that will be sent by the subscribed service to the trigger in response to an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the identity to add to the approver list for the access request. | 
**name** | **str** | The name of the identity to add to the approver list for the access request. | 
**type** | **object** | The type of object being referenced. | 
**approved** | **bool** | Whether or not to approve the access request. | 
**comment** | **str** | A comment about the decision to approve or deny the request. | 
**approver** | **str** | The name of the entity that approved or denied the request. | 

## Example

```python
from sailpoint.v2024.models.trigger_example_output import TriggerExampleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExampleOutput from a JSON string
trigger_example_output_instance = TriggerExampleOutput.from_json(json)
# print the JSON string representation of the object
print(TriggerExampleOutput.to_json())

# convert the object into a dict
trigger_example_output_dict = trigger_example_output_instance.to_dict()
# create an instance of TriggerExampleOutput from a dict
trigger_example_output_from_dict = TriggerExampleOutput.from_dict(trigger_example_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


