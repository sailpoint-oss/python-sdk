# ExternalAttributes

Attributes related to an external trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for the external trigger | [optional] 
**description** | **str** | Additional context about the external trigger | [optional] 
**client_id** | **str** | OAuth Client ID to authenticate with this trigger | [optional] 
**url** | **str** | URL to invoke this workflow | [optional] 

## Example

```python
from sailpoint.beta.models.external_attributes import ExternalAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAttributes from a JSON string
external_attributes_instance = ExternalAttributes.from_json(json)
# print the JSON string representation of the object
print(ExternalAttributes.to_json())

# convert the object into a dict
external_attributes_dict = external_attributes_instance.to_dict()
# create an instance of ExternalAttributes from a dict
external_attributes_from_dict = ExternalAttributes.from_dict(external_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


