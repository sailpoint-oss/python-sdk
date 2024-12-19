# AccessProfileDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Access Profile | [optional] 
**name** | **str** | Name of the Access Profile | [optional] 
**description** | **str** | Information about the Access Profile | [optional] 
**created** | **datetime** | Date the Access Profile was created | [optional] 
**modified** | **datetime** | Date the Access Profile was last modified. | [optional] 
**disabled** | **bool** | Whether the Access Profile is enabled. | [optional] [default to True]
**requestable** | **bool** | Whether the Access Profile is requestable via access request. | [optional] [default to False]
**protected** | **bool** | Whether the Access Profile is protected. | [optional] [default to False]
**owner_id** | **str** | The owner ID of the Access Profile | [optional] 
**source_id** | **int** | The source ID of the Access Profile | [optional] 
**source_name** | **str** | The source name of the Access Profile | [optional] 
**app_id** | **int** | The source app ID of the Access Profile | [optional] 
**app_name** | **str** | The source app name of the Access Profile | [optional] 
**application_id** | **str** | The id of the application | [optional] 
**type** | **str** | The type of the access profile | [optional] 
**entitlements** | **List[str]** | List of IDs of entitlements | [optional] 
**entitlement_count** | **int** | The number of entitlements in the access profile | [optional] 
**segments** | **List[str]** | List of IDs of segments, if any, to which this Access Profile is assigned. | [optional] 
**approval_schemes** | **str** | Comma-separated list of approval schemes. Each approval scheme is one of - manager - appOwner - sourceOwner - accessProfileOwner - workgroup:&amp;lt;workgroupId&amp;gt;  | [optional] 
**revoke_request_approval_schemes** | **str** | Comma-separated list of revoke request approval schemes. Each approval scheme is one of - manager - sourceOwner - accessProfileOwner - workgroup:&amp;lt;workgroupId&amp;gt;  | [optional] 
**request_comments_required** | **bool** | Whether the access profile require request comment for access request. | [optional] [default to False]
**denied_comments_required** | **bool** | Whether denied comment is required when access request is denied. | [optional] [default to False]
**account_selector** | [**AccessProfileDetailsAccountSelector**](AccessProfileDetailsAccountSelector.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_profile_details import AccessProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileDetails from a JSON string
access_profile_details_instance = AccessProfileDetails.from_json(json)
# print the JSON string representation of the object
print(AccessProfileDetails.to_json())

# convert the object into a dict
access_profile_details_dict = access_profile_details_instance.to_dict()
# create an instance of AccessProfileDetails from a dict
access_profile_details_from_dict = AccessProfileDetails.from_dict(access_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


