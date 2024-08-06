# SpConfigMessage

Message model for Config Import/Export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Message key. | 
**text** | **str** | Message text. | 
**details** | **Dict[str, object]** | Message details if any, in key:value pairs. | 

## Example

```python
from sailpoint.v2024.models.sp_config_message import SpConfigMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigMessage from a JSON string
sp_config_message_instance = SpConfigMessage.from_json(json)
# print the JSON string representation of the object
print SpConfigMessage.to_json()

# convert the object into a dict
sp_config_message_dict = sp_config_message_instance.to_dict()
# create an instance of SpConfigMessage from a dict
sp_config_message_form_dict = sp_config_message.from_dict(sp_config_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


