# AccessProfileUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_profile_id** | **str** | ID of the Access Profile that is in use | [optional] 
**used_by** | [**List[AccessProfileUsageUsedByInner]**](AccessProfileUsageUsedByInner.md) | List of references to objects which are using the indicated Access Profile | [optional] 

## Example

```python
from sailpoint.v2024.models.access_profile_usage import AccessProfileUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileUsage from a JSON string
access_profile_usage_instance = AccessProfileUsage.from_json(json)
# print the JSON string representation of the object
print(AccessProfileUsage.to_json())

# convert the object into a dict
access_profile_usage_dict = access_profile_usage_instance.to_dict()
# create an instance of AccessProfileUsage from a dict
access_profile_usage_from_dict = AccessProfileUsage.from_dict(access_profile_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


