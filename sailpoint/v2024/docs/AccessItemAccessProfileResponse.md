# AccessItemAccessProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | the access item type. accessProfile in this case | [optional] 
**id** | **str** | the access item id | [optional] 
**name** | **str** | the access profile name | [optional] 
**source_name** | **str** | the name of the source | [optional] 
**source_id** | **str** | the id of the source | [optional] 
**description** | **str** | the description for the access profile | [optional] 
**display_name** | **str** | the display name of the identity | [optional] 
**entitlement_count** | **str** | the number of entitlements the access profile will create | [optional] 
**app_display_name** | **str** | the name of | [optional] 
**remove_date** | **str** | the date the access profile is no longer assigned to the specified identity | [optional] 
**standalone** | **bool** | indicates whether the access profile is standalone | 
**revocable** | **bool** | indicates whether the access profile is | 

## Example

```python
from sailpoint.v2024.models.access_item_access_profile_response import AccessItemAccessProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemAccessProfileResponse from a JSON string
access_item_access_profile_response_instance = AccessItemAccessProfileResponse.from_json(json)
# print the JSON string representation of the object
print(AccessItemAccessProfileResponse.to_json())

# convert the object into a dict
access_item_access_profile_response_dict = access_item_access_profile_response_instance.to_dict()
# create an instance of AccessItemAccessProfileResponse from a dict
access_item_access_profile_response_from_dict = AccessItemAccessProfileResponse.from_dict(access_item_access_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


