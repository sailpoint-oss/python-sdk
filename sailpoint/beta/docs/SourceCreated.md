# SourceCreated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the source. | 
**name** | **str** | Human friendly name of the source. | 
**type** | **str** | The connection type. | 
**created** | **datetime** | The date and time the source was created. | 
**connector** | **str** | The connector type used to connect to the source. | 
**actor** | [**SourceCreatedActor**](SourceCreatedActor.md) |  | 

## Example

```python
from sailpoint.beta.models.source_created import SourceCreated

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCreated from a JSON string
source_created_instance = SourceCreated.from_json(json)
# print the JSON string representation of the object
print SourceCreated.to_json()

# convert the object into a dict
source_created_dict = source_created_instance.to_dict()
# create an instance of SourceCreated from a dict
source_created_form_dict = source_created.from_dict(source_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


