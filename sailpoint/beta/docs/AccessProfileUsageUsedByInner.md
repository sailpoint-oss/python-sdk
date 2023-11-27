# AccessProfileUsageUsedByInner

Role using the access profile.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of role using the access profile. | [optional] 
**id** | **str** | ID of role using the access profile. | [optional] 
**name** | **str** | Display name of role using the access profile. | [optional] 

## Example

```python
from sailpoint.beta.models.access_profile_usage_used_by_inner import AccessProfileUsageUsedByInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileUsageUsedByInner from a JSON string
access_profile_usage_used_by_inner_instance = AccessProfileUsageUsedByInner.from_json(json)
# print the JSON string representation of the object
print AccessProfileUsageUsedByInner.to_json()

# convert the object into a dict
access_profile_usage_used_by_inner_dict = access_profile_usage_used_by_inner_instance.to_dict()
# create an instance of AccessProfileUsageUsedByInner from a dict
access_profile_usage_used_by_inner_form_dict = access_profile_usage_used_by_inner.from_dict(access_profile_usage_used_by_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


