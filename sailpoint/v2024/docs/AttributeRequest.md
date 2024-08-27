# AttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Attribute name. | [optional] 
**op** | **str** | Operation to perform on attribute. | [optional] 
**value** | **str** | Value of attribute. | [optional] 

## Example

```python
from sailpoint.v2024.models.attribute_request import AttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeRequest from a JSON string
attribute_request_instance = AttributeRequest.from_json(json)
# print the JSON string representation of the object
print(AttributeRequest.to_json())

# convert the object into a dict
attribute_request_dict = attribute_request_instance.to_dict()
# create an instance of AttributeRequest from a dict
attribute_request_from_dict = AttributeRequest.from_dict(attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


