# SourceCreationErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multihost_id** | **str** | Multi-Host Integration ID. | [optional] [readonly] 
**source_name** | **str** | Source&#39;s human-readable name. | [optional] 
**source_error** | **str** | Source&#39;s human-readable description. | [optional] 
**created** | **datetime** | Date-time when the source was created | [optional] 
**modified** | **datetime** | Date-time when the source was last modified. | [optional] 
**operation** | **str** | operation category (e.g. DELETE). | [optional] 

## Example

```python
from sailpoint.beta.models.source_creation_errors import SourceCreationErrors

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCreationErrors from a JSON string
source_creation_errors_instance = SourceCreationErrors.from_json(json)
# print the JSON string representation of the object
print(SourceCreationErrors.to_json())

# convert the object into a dict
source_creation_errors_dict = source_creation_errors_instance.to_dict()
# create an instance of SourceCreationErrors from a dict
source_creation_errors_from_dict = SourceCreationErrors.from_dict(source_creation_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


