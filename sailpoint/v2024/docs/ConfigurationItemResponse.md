# ConfigurationItemResponse

The response body of a Reassignment Configuration for a single identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**Identity1**](Identity1.md) |  | [optional] 
**config_details** | [**List[ConfigurationDetailsResponse]**](ConfigurationDetailsResponse.md) | Details of how work should be reassigned for an Identity | [optional] 

## Example

```python
from sailpoint.v2024.models.configuration_item_response import ConfigurationItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationItemResponse from a JSON string
configuration_item_response_instance = ConfigurationItemResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigurationItemResponse.to_json())

# convert the object into a dict
configuration_item_response_dict = configuration_item_response_instance.to_dict()
# create an instance of ConfigurationItemResponse from a dict
configuration_item_response_from_dict = ConfigurationItemResponse.from_dict(configuration_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


