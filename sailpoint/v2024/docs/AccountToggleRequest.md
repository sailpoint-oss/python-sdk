# AccountToggleRequest

Request used for account enable/disable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_verification_id** | **str** | If set, an external process validates that the user wants to proceed with this request. | [optional] 
**force_provisioning** | **bool** | If set, provisioning updates the account attribute at the source.   This option is used when the account is not synced to ensure the attribute is updated. Providing &#39;true&#39; for an unlocked account will add and process &#39;Unlock&#39; operation by the workflow. | [optional] 

## Example

```python
from sailpoint.v2024.models.account_toggle_request import AccountToggleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountToggleRequest from a JSON string
account_toggle_request_instance = AccountToggleRequest.from_json(json)
# print the JSON string representation of the object
print AccountToggleRequest.to_json()

# convert the object into a dict
account_toggle_request_dict = account_toggle_request_instance.to_dict()
# create an instance of AccountToggleRequest from a dict
account_toggle_request_form_dict = account_toggle_request.from_dict(account_toggle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


