# Delete202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Task result ID. | [optional] 
**name** | **str** | Task result&#39;s human-readable display name (this should be null/empty). | [optional] 

## Example

```python
from sailpoint.beta.models.delete202_response import Delete202Response

# TODO update the JSON string below
json = "{}"
# create an instance of Delete202Response from a JSON string
delete202_response_instance = Delete202Response.from_json(json)
# print the JSON string representation of the object
print(Delete202Response.to_json())

# convert the object into a dict
delete202_response_dict = delete202_response_instance.to_dict()
# create an instance of Delete202Response from a dict
delete202_response_from_dict = Delete202Response.from_dict(delete202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


