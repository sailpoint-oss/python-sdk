# AppAccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The source app ID | [optional] 
**app_display_name** | **str** | The source app display name | [optional] 
**source_account** | [**AppAccountDetailsSourceAccount**](AppAccountDetailsSourceAccount.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.app_account_details import AppAccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccountDetails from a JSON string
app_account_details_instance = AppAccountDetails.from_json(json)
# print the JSON string representation of the object
print(AppAccountDetails.to_json())

# convert the object into a dict
app_account_details_dict = app_account_details_instance.to_dict()
# create an instance of AppAccountDetails from a dict
app_account_details_from_dict = AppAccountDetails.from_dict(app_account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


