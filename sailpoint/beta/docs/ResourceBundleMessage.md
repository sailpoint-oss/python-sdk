# ResourceBundleMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the message | [optional] 
**format** | **str** | The format of the message | [optional] 

## Example

```python
from beta.models.resource_bundle_message import ResourceBundleMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceBundleMessage from a JSON string
resource_bundle_message_instance = ResourceBundleMessage.from_json(json)
# print the JSON string representation of the object
print ResourceBundleMessage.to_json()

# convert the object into a dict
resource_bundle_message_dict = resource_bundle_message_instance.to_dict()
# create an instance of ResourceBundleMessage from a dict
resource_bundle_message_form_dict = resource_bundle_message.from_dict(resource_bundle_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


