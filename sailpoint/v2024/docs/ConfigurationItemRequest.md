# ConfigurationItemRequest

The request body for creation or update of a Reassignment Configuration for a single identity and work type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassigned_from_id** | **str** | The identity id to reassign an item from | [optional] 
**reassigned_to_id** | **str** | The identity id to reassign an item to | [optional] 
**config_type** | [**ConfigTypeEnum**](ConfigTypeEnum.md) |  | [optional] 
**start_date** | **datetime** | The date from which to start reassigning work items | [optional] 
**end_date** | **datetime** | The date from which to stop reassigning work items.  If this is an null string it indicates a permanent reassignment. | [optional] 

## Example

```python
from sailpoint.v2024.models.configuration_item_request import ConfigurationItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationItemRequest from a JSON string
configuration_item_request_instance = ConfigurationItemRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigurationItemRequest.to_json())

# convert the object into a dict
configuration_item_request_dict = configuration_item_request_instance.to_dict()
# create an instance of ConfigurationItemRequest from a dict
configuration_item_request_from_dict = ConfigurationItemRequest.from_dict(configuration_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


