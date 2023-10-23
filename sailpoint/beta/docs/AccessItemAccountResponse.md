# AccessItemAccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | the access item type. account in this case | [optional] 
**id** | **str** | the access item id | [optional] 
**native_identity** | **str** | the native identifier used to uniquely identify an acccount | [optional] 
**source_name** | **str** | the name of the source | [optional] 
**source_id** | **str** | the id of the source | [optional] 
**entitlement_count** | **str** | the number of entitlements the account will create | [optional] 
**display_name** | **str** | the display name of the identity | [optional] 

## Example

```python
from beta.models.access_item_account_response import AccessItemAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemAccountResponse from a JSON string
access_item_account_response_instance = AccessItemAccountResponse.from_json(json)
# print the JSON string representation of the object
print AccessItemAccountResponse.to_json()

# convert the object into a dict
access_item_account_response_dict = access_item_account_response_instance.to_dict()
# create an instance of AccessItemAccountResponse from a dict
access_item_account_response_form_dict = access_item_account_response.from_dict(access_item_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


