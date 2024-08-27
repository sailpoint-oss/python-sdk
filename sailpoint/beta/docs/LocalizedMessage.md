# LocalizedMessage

Localized error message to indicate a failed invocation or error if any.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Message locale | 
**message** | **str** | Message text | 

## Example

```python
from sailpoint.beta.models.localized_message import LocalizedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedMessage from a JSON string
localized_message_instance = LocalizedMessage.from_json(json)
# print the JSON string representation of the object
print(LocalizedMessage.to_json())

# convert the object into a dict
localized_message_dict = localized_message_instance.to_dict()
# create an instance of LocalizedMessage from a dict
localized_message_from_dict = LocalizedMessage.from_dict(localized_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


