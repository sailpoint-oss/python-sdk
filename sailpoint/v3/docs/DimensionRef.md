# DimensionRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the object to which this reference applies | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v3.models.dimension_ref import DimensionRef

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionRef from a JSON string
dimension_ref_instance = DimensionRef.from_json(json)
# print the JSON string representation of the object
print(DimensionRef.to_json())

# convert the object into a dict
dimension_ref_dict = dimension_ref_instance.to_dict()
# create an instance of DimensionRef from a dict
dimension_ref_from_dict = DimensionRef.from_dict(dimension_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


