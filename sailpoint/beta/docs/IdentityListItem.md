# IdentityListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identity ID | [optional] 
**display_name** | **str** | the display name of the identity | [optional] 
**first_name** | **str** | the first name of the identity | [optional] 
**last_name** | **str** | the last name of the identity | [optional] 
**active** | **bool** | indicates if an identity is active or not | [optional] [default to True]
**deleted_date** | **str** | the date when the identity was deleted | [optional] 

## Example

```python
from sailpoint.beta.models.identity_list_item import IdentityListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityListItem from a JSON string
identity_list_item_instance = IdentityListItem.from_json(json)
# print the JSON string representation of the object
print IdentityListItem.to_json()

# convert the object into a dict
identity_list_item_dict = identity_list_item_instance.to_dict()
# create an instance of IdentityListItem from a dict
identity_list_item_form_dict = identity_list_item.from_dict(identity_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


