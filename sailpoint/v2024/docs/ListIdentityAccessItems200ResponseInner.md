# ListIdentityAccessItems200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | the access item type. role in this case | [optional] 
**id** | **str** | the access item id | [optional] 
**name** | **str** | the access profile name | [optional] 
**source_name** | **str** | the associated source name if it exists | [optional] 
**source_id** | **str** | the id of the source | [optional] 
**description** | **str** | the description for the role | [optional] 
**display_name** | **str** | the role display name | [optional] 
**entitlement_count** | **str** | the number of entitlements the account will create | [optional] 
**app_display_name** | **str** | the name of | [optional] 
**remove_date** | **str** | the date the role is no longer assigned to the specified identity | [optional] 
**standalone** | **bool** | indicates whether the entitlement is standalone | 
**revocable** | **bool** | indicates whether the role is revocable | 
**native_identity** | **str** | the native identifier used to uniquely identify an acccount | [optional] 
**app_role_id** | **str** | the app role id | [optional] 
**attribute** | **str** | the entitlement attribute | [optional] 
**value** | **str** | the associated value | [optional] 
**entitlement_type** | **str** | the type of entitlement | [optional] 
**privileged** | **bool** | indicates whether the entitlement is privileged | 
**cloud_governed** | **bool** | indicates whether the entitlement is cloud governed | 

## Example

```python
from sailpoint.v2024.models.list_identity_access_items200_response_inner import ListIdentityAccessItems200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListIdentityAccessItems200ResponseInner from a JSON string
list_identity_access_items200_response_inner_instance = ListIdentityAccessItems200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListIdentityAccessItems200ResponseInner.to_json())

# convert the object into a dict
list_identity_access_items200_response_inner_dict = list_identity_access_items200_response_inner_instance.to_dict()
# create an instance of ListIdentityAccessItems200ResponseInner from a dict
list_identity_access_items200_response_inner_from_dict = ListIdentityAccessItems200ResponseInner.from_dict(list_identity_access_items200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


