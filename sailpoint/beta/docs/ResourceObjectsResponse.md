# ResourceObjectsResponse

Response model for peek resource objects from source connectors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the source | [optional] [readonly] 
**name** | **str** | Name of the source | [optional] [readonly] 
**object_count** | **int** | The number of objects that were fetched by the connector. | [optional] [readonly] 
**elapsed_millis** | **int** | The number of milliseconds spent on the entire request. | [optional] [readonly] 
**resource_objects** | [**List[ResourceObject]**](ResourceObject.md) | Fetched objects from the source connector. | [optional] [readonly] 

## Example

```python
from beta.models.resource_objects_response import ResourceObjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceObjectsResponse from a JSON string
resource_objects_response_instance = ResourceObjectsResponse.from_json(json)
# print the JSON string representation of the object
print ResourceObjectsResponse.to_json()

# convert the object into a dict
resource_objects_response_dict = resource_objects_response_instance.to_dict()
# create an instance of ResourceObjectsResponse from a dict
resource_objects_response_form_dict = resource_objects_response.from_dict(resource_objects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


