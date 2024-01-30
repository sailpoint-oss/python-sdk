# SourceUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the source. | 
**name** | **str** | The user friendly name of the source. | 
**type** | **str** | The connection type of the source. | 
**modified** | **datetime** | The date and time the source was modified. | 
**connector** | **str** | The connector type used to connect to the source. | 
**actor** | [**SourceUpdatedActor**](SourceUpdatedActor.md) |  | 

## Example

```python
from sailpoint.beta.models.source_updated import SourceUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUpdated from a JSON string
source_updated_instance = SourceUpdated.from_json(json)
# print the JSON string representation of the object
print SourceUpdated.to_json()

# convert the object into a dict
source_updated_dict = source_updated_instance.to_dict()
# create an instance of SourceUpdated from a dict
source_updated_form_dict = source_updated.from_dict(source_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


