# NonEmployeeRequestLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee request id. | [optional] 
**requester** | [**IdentityReferenceWithId**](IdentityReferenceWithId.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.non_employee_request_lite import NonEmployeeRequestLite

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeRequestLite from a JSON string
non_employee_request_lite_instance = NonEmployeeRequestLite.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeRequestLite.to_json())

# convert the object into a dict
non_employee_request_lite_dict = non_employee_request_lite_instance.to_dict()
# create an instance of NonEmployeeRequestLite from a dict
non_employee_request_lite_from_dict = NonEmployeeRequestLite.from_dict(non_employee_request_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


