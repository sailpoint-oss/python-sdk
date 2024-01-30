# DeleteSource202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the task result | [optional] 
**name** | **str** | Human-readable display name of the task result (should be null/empty) | [optional] 

## Example

```python
from sailpoint.v3.models.delete_source202_response import DeleteSource202Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSource202Response from a JSON string
delete_source202_response_instance = DeleteSource202Response.from_json(json)
# print the JSON string representation of the object
print DeleteSource202Response.to_json()

# convert the object into a dict
delete_source202_response_dict = delete_source202_response_instance.to_dict()
# create an instance of DeleteSource202Response from a dict
delete_source202_response_form_dict = delete_source202_response.from_dict(delete_source202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


