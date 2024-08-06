# ResourceObjectsRequest

Request model for peek resource objects from source connectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The type of resource objects to iterate over. | [optional] [default to 'account']
**max_count** | **int** | The maximum number of resource objects to iterate over and return. | [optional] [default to 25]

## Example

```python
from sailpoint.v2024.models.resource_objects_request import ResourceObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceObjectsRequest from a JSON string
resource_objects_request_instance = ResourceObjectsRequest.from_json(json)
# print the JSON string representation of the object
print ResourceObjectsRequest.to_json()

# convert the object into a dict
resource_objects_request_dict = resource_objects_request_instance.to_dict()
# create an instance of ResourceObjectsRequest from a dict
resource_objects_request_form_dict = resource_objects_request.from_dict(resource_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


