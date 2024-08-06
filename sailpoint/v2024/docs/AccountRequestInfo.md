# AccountRequestInfo

If an account activity item is associated with an access request, captures details of that request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_object_id** | **str** | Id of requested object | [optional] 
**requested_object_name** | **str** | Human-readable name of requested object | [optional] 
**requested_object_type** | [**RequestableObjectType**](RequestableObjectType.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.account_request_info import AccountRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequestInfo from a JSON string
account_request_info_instance = AccountRequestInfo.from_json(json)
# print the JSON string representation of the object
print AccountRequestInfo.to_json()

# convert the object into a dict
account_request_info_dict = account_request_info_instance.to_dict()
# create an instance of AccountRequestInfo from a dict
account_request_info_form_dict = account_request_info.from_dict(account_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


