# Ref


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v2024.models.ref import Ref

# TODO update the JSON string below
json = "{}"
# create an instance of Ref from a JSON string
ref_instance = Ref.from_json(json)
# print the JSON string representation of the object
print(Ref.to_json())

# convert the object into a dict
ref_dict = ref_instance.to_dict()
# create an instance of Ref from a dict
ref_from_dict = Ref.from_dict(ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


