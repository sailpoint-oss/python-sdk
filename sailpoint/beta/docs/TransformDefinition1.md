# TransformDefinition1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the transform definition. | [optional] 
**attributes** | [**Dict[str, TransformDefinition1AttributesValue]**](TransformDefinition1AttributesValue.md) | Arbitrary key-value pairs to store any metadata for the object | [optional] 

## Example

```python
from sailpoint.beta.models.transform_definition1 import TransformDefinition1

# TODO update the JSON string below
json = "{}"
# create an instance of TransformDefinition1 from a JSON string
transform_definition1_instance = TransformDefinition1.from_json(json)
# print the JSON string representation of the object
print TransformDefinition1.to_json()

# convert the object into a dict
transform_definition1_dict = transform_definition1_instance.to_dict()
# create an instance of TransformDefinition1 from a dict
transform_definition1_form_dict = transform_definition1.from_dict(transform_definition1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


