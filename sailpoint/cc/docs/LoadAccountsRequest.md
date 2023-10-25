# LoadAccountsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_optimization** | **bool** |  | [optional] 
**file** | **bytearray** |  | [optional] 

## Example

```python
from cc.models.load_accounts_request import LoadAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoadAccountsRequest from a JSON string
load_accounts_request_instance = LoadAccountsRequest.from_json(json)
# print the JSON string representation of the object
print LoadAccountsRequest.to_json()

# convert the object into a dict
load_accounts_request_dict = load_accounts_request_instance.to_dict()
# create an instance of LoadAccountsRequest from a dict
load_accounts_request_form_dict = load_accounts_request.from_dict(load_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


