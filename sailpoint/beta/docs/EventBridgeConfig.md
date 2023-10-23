# EventBridgeConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account** | **str** | AWS Account Number (12-digit number) that has the EventBridge Partner Event Source Resource. | 
**aws_region** | **str** | AWS Region that has the EventBridge Partner Event Source Resource. See https://docs.aws.amazon.com/general/latest/gr/rande.html for a full list of available values. | 

## Example

```python
from beta.models.event_bridge_config import EventBridgeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventBridgeConfig from a JSON string
event_bridge_config_instance = EventBridgeConfig.from_json(json)
# print the JSON string representation of the object
print EventBridgeConfig.to_json()

# convert the object into a dict
event_bridge_config_dict = event_bridge_config_instance.to_dict()
# create an instance of EventBridgeConfig from a dict
event_bridge_config_form_dict = event_bridge_config.from_dict(event_bridge_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


