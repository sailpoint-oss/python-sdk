# MultiHostSourcesSchemasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Schema ID. | [optional] 
**name** | **str** | Schema&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_sources_schemas_inner import MultiHostSourcesSchemasInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostSourcesSchemasInner from a JSON string
multi_host_sources_schemas_inner_instance = MultiHostSourcesSchemasInner.from_json(json)
# print the JSON string representation of the object
print(MultiHostSourcesSchemasInner.to_json())

# convert the object into a dict
multi_host_sources_schemas_inner_dict = multi_host_sources_schemas_inner_instance.to_dict()
# create an instance of MultiHostSourcesSchemasInner from a dict
multi_host_sources_schemas_inner_from_dict = MultiHostSourcesSchemasInner.from_dict(multi_host_sources_schemas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


