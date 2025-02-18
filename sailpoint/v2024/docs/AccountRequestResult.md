# AccountRequestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | Error message. | [optional] 
**status** | **str** | The status of the account request | [optional] 
**ticket_id** | **str** | ID of associated ticket. | [optional] 

## Example

```python
from sailpoint.v2024.models.account_request_result import AccountRequestResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequestResult from a JSON string
account_request_result_instance = AccountRequestResult.from_json(json)
# print the JSON string representation of the object
print(AccountRequestResult.to_json())

# convert the object into a dict
account_request_result_dict = account_request_result_instance.to_dict()
# create an instance of AccountRequestResult from a dict
account_request_result_from_dict = AccountRequestResult.from_dict(account_request_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


