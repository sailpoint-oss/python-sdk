# OriginalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | the account id | [optional] 
**attribute_requests** | [**List[AttributeRequest]**](AttributeRequest.md) |  | [optional] 
**op** | **str** | the operation that was used | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.original_request import OriginalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalRequest from a JSON string
original_request_instance = OriginalRequest.from_json(json)
# print the JSON string representation of the object
print OriginalRequest.to_json()

# convert the object into a dict
original_request_dict = original_request_instance.to_dict()
# create an instance of OriginalRequest from a dict
original_request_form_dict = original_request.from_dict(original_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


