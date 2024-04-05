# ObjectMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Type of the object the mapping value applies to, must be one from enum | 
**json_path** | **str** | JSONPath expression denoting the path within the object where the mapping value should be applied | 
**source_value** | **str** | Original value at the jsonPath location within the object | 
**target_value** | **str** | Value to be assigned at the jsonPath location within the object | 
**enabled** | **bool** | Whether or not this object mapping is enabled | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.object_mapping_request import ObjectMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMappingRequest from a JSON string
object_mapping_request_instance = ObjectMappingRequest.from_json(json)
# print the JSON string representation of the object
print ObjectMappingRequest.to_json()

# convert the object into a dict
object_mapping_request_dict = object_mapping_request_instance.to_dict()
# create an instance of ObjectMappingRequest from a dict
object_mapping_request_form_dict = object_mapping_request.from_dict(object_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


