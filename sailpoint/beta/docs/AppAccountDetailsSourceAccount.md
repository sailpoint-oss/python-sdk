# AppAccountDetailsSourceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The account ID | [optional] 
**native_identity** | **str** | The native identity of account | [optional] 
**display_name** | **str** | The display name of account | [optional] 
**source_id** | **str** | The source ID of account | [optional] 
**source_display_name** | **str** | The source name of account | [optional] 

## Example

```python
from sailpoint.beta.models.app_account_details_source_account import AppAccountDetailsSourceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccountDetailsSourceAccount from a JSON string
app_account_details_source_account_instance = AppAccountDetailsSourceAccount.from_json(json)
# print the JSON string representation of the object
print(AppAccountDetailsSourceAccount.to_json())

# convert the object into a dict
app_account_details_source_account_dict = app_account_details_source_account_instance.to_dict()
# create an instance of AppAccountDetailsSourceAccount from a dict
app_account_details_source_account_from_dict = AppAccountDetailsSourceAccount.from_dict(app_account_details_source_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


