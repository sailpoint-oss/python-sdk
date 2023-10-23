# Trigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the trigger. | 
**name** | **str** | Trigger Name. | 
**type** | [**TriggerType**](TriggerType.md) |  | 
**description** | **str** | Trigger Description. | [optional] 
**input_schema** | **str** | The JSON schema of the payload that will be sent by the trigger to the subscribed service. | 
**example_input** | [**TriggerExampleInput**](TriggerExampleInput.md) |  | 
**output_schema** | **str** | The JSON schema of the response that will be sent by the subscribed service to the trigger in response to an event.  This only applies to a trigger type of &#x60;REQUEST_RESPONSE&#x60;. | [optional] 
**example_output** | [**TriggerExampleOutput**](TriggerExampleOutput.md) |  | [optional] 

## Example

```python
from beta.models.trigger import Trigger

# TODO update the JSON string below
json = "{}"
# create an instance of Trigger from a JSON string
trigger_instance = Trigger.from_json(json)
# print the JSON string representation of the object
print Trigger.to_json()

# convert the object into a dict
trigger_dict = trigger_instance.to_dict()
# create an instance of Trigger from a dict
trigger_form_dict = trigger.from_dict(trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


