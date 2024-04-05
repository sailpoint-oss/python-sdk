# ObjectMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_mapping_id** | **str** | Id of the object mapping | [optional] 
**object_type** | **str** | Type of the object the mapping value applies to | [optional] 
**json_path** | **str** | JSONPath expression denoting the path within the object where the mapping value should be applied | [optional] 
**source_value** | **str** | Original value at the jsonPath location within the object | [optional] 
**target_value** | **str** | Value to be assigned at the jsonPath location within the object | [optional] 
**enabled** | **bool** | Whether or not this object mapping is enabled | [optional] [default to False]
**created** | **str** | Object mapping creation timestamp | [optional] 
**modified** | **str** | Object mapping latest update timestamp | [optional] 

## Example

```python
from sailpoint.v3.models.object_mapping_response import ObjectMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMappingResponse from a JSON string
object_mapping_response_instance = ObjectMappingResponse.from_json(json)
# print the JSON string representation of the object
print ObjectMappingResponse.to_json()

# convert the object into a dict
object_mapping_response_dict = object_mapping_response_instance.to_dict()
# create an instance of ObjectMappingResponse from a dict
object_mapping_response_form_dict = object_mapping_response.from_dict(object_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


