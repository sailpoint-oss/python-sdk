# AccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique ID of the account | [optional] 
**attribute_requests** | [**List[AttributeRequest]**](AttributeRequest.md) |  | [optional] 
**op** | **str** | The operation that was performed | [optional] 
**provisioning_target** | [**AccountSource**](AccountSource.md) |  | [optional] 
**result** | [**AccountRequestResult**](AccountRequestResult.md) |  | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.account_request import AccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequest from a JSON string
account_request_instance = AccountRequest.from_json(json)
# print the JSON string representation of the object
print(AccountRequest.to_json())

# convert the object into a dict
account_request_dict = account_request_instance.to_dict()
# create an instance of AccountRequest from a dict
account_request_from_dict = AccountRequest.from_dict(account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


