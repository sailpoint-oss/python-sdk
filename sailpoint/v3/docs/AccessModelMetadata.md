# AccessModelMetadata

Metadata that describes an access item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique identifier for the metadata type | [optional] 
**name** | **str** | Human readable name of the metadata type | [optional] 
**multiselect** | **bool** | Allows selecting multiple values | [optional] [default to False]
**status** | **str** | The state of the metadata item | [optional] 
**type** | **str** | The type of the metadata item | [optional] 
**object_types** | **List[str]** | The types of objects | [optional] 
**description** | **str** | Describes the metadata item | [optional] 
**values** | [**List[AccessModelMetadataValuesInner]**](AccessModelMetadataValuesInner.md) | The value to assign to the metadata item | [optional] 

## Example

```python
from sailpoint.v3.models.access_model_metadata import AccessModelMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelMetadata from a JSON string
access_model_metadata_instance = AccessModelMetadata.from_json(json)
# print the JSON string representation of the object
print(AccessModelMetadata.to_json())

# convert the object into a dict
access_model_metadata_dict = access_model_metadata_instance.to_dict()
# create an instance of AccessModelMetadata from a dict
access_model_metadata_from_dict = AccessModelMetadata.from_dict(access_model_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


