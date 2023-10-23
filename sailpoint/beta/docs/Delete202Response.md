# Delete202Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the task result | [optional] 
**name** | **str** | Human-readable display name of the task result (should be null/empty) | [optional] 

## Example

```python
from beta.models.delete202_response import Delete202Response

# TODO update the JSON string below
json = "{}"
# create an instance of Delete202Response from a JSON string
delete202_response_instance = Delete202Response.from_json(json)
# print the JSON string representation of the object
print Delete202Response.to_json()

# convert the object into a dict
delete202_response_dict = delete202_response_instance.to_dict()
# create an instance of Delete202Response from a dict
delete202_response_form_dict = delete202_response.from_dict(delete202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


