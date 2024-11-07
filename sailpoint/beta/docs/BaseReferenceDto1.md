# BaseReferenceDto1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the application ID | [optional] 
**name** | **str** | the application name | [optional] 

## Example

```python
from sailpoint.beta.models.base_reference_dto1 import BaseReferenceDto1

# TODO update the JSON string below
json = "{}"
# create an instance of BaseReferenceDto1 from a JSON string
base_reference_dto1_instance = BaseReferenceDto1.from_json(json)
# print the JSON string representation of the object
print(BaseReferenceDto1.to_json())

# convert the object into a dict
base_reference_dto1_dict = base_reference_dto1_instance.to_dict()
# create an instance of BaseReferenceDto1 from a dict
base_reference_dto1_from_dict = BaseReferenceDto1.from_dict(base_reference_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


