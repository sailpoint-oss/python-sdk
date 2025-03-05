# AccessModelMetadataValuesInner

An individual value to assign to the metadata item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value to assign to the metdata item | [optional] 
**name** | **str** | Display name of the value | [optional] 
**status** | **str** | The status of the individual value | [optional] 

## Example

```python
from sailpoint.v2024.models.access_model_metadata_values_inner import AccessModelMetadataValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelMetadataValuesInner from a JSON string
access_model_metadata_values_inner_instance = AccessModelMetadataValuesInner.from_json(json)
# print the JSON string representation of the object
print(AccessModelMetadataValuesInner.to_json())

# convert the object into a dict
access_model_metadata_values_inner_dict = access_model_metadata_values_inner_instance.to_dict()
# create an instance of AccessModelMetadataValuesInner from a dict
access_model_metadata_values_inner_from_dict = AccessModelMetadataValuesInner.from_dict(access_model_metadata_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


