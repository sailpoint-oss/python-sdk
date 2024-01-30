# SourceDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the source. | 
**name** | **str** | Human friendly name of the source. | 
**type** | **str** | The connection type. | 
**deleted** | **datetime** | The date and time the source was deleted. | 
**connector** | **str** | The connector type used to connect to the source. | 
**actor** | [**SourceDeletedActor**](SourceDeletedActor.md) |  | 

## Example

```python
from sailpoint.beta.models.source_deleted import SourceDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDeleted from a JSON string
source_deleted_instance = SourceDeleted.from_json(json)
# print the JSON string representation of the object
print SourceDeleted.to_json()

# convert the object into a dict
source_deleted_dict = source_deleted_instance.to_dict()
# create an instance of SourceDeleted from a dict
source_deleted_form_dict = source_deleted.from_dict(source_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


