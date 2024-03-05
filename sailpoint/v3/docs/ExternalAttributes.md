# ExternalAttributes

Attributes related to an external trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for the external trigger | 
**description** | **str** | Additonal context about the external trigger | [optional] 

## Example

```python
from sailpoint.v3.models.external_attributes import ExternalAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAttributes from a JSON string
external_attributes_instance = ExternalAttributes.from_json(json)
# print the JSON string representation of the object
print ExternalAttributes.to_json()

# convert the object into a dict
external_attributes_dict = external_attributes_instance.to_dict()
# create an instance of ExternalAttributes from a dict
external_attributes_form_dict = external_attributes.from_dict(external_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


