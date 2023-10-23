# SourceSchemasInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the schema | [optional] 
**name** | **str** | Human-readable display name of the schema | [optional] 

## Example

```python
from v3.models.source_schemas_inner import SourceSchemasInner

# TODO update the JSON string below
json = "{}"
# create an instance of SourceSchemasInner from a JSON string
source_schemas_inner_instance = SourceSchemasInner.from_json(json)
# print the JSON string representation of the object
print SourceSchemasInner.to_json()

# convert the object into a dict
source_schemas_inner_dict = source_schemas_inner_instance.to_dict()
# create an instance of SourceSchemasInner from a dict
source_schemas_inner_form_dict = source_schemas_inner.from_dict(source_schemas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


