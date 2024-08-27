# IdentityProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**description** | **str** | The description of the Identity Profile. | [optional] 
**owner** | [**IdentityProfileAllOfOwner**](IdentityProfileAllOfOwner.md) |  | [optional] 
**priority** | **int** | The priority for an Identity Profile. | [optional] 
**authoritative_source** | [**IdentityProfileAllOfAuthoritativeSource**](IdentityProfileAllOfAuthoritativeSource.md) |  | 
**identity_refresh_required** | **bool** | True if a identity refresh is needed. Typically triggered when a change on the source has been made | [optional] [default to False]
**identity_count** | **int** | The number of identities that belong to the Identity Profile. | [optional] 
**identity_attribute_config** | [**IdentityAttributeConfig**](IdentityAttributeConfig.md) |  | [optional] 
**identity_exception_report_reference** | [**IdentityExceptionReportReference**](IdentityExceptionReportReference.md) |  | [optional] 
**has_time_based_attr** | **bool** | Indicates the value of requiresPeriodicRefresh attribute for the Identity Profile. | [optional] [default to True]

## Example

```python
from sailpoint.beta.models.identity_profile import IdentityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfile from a JSON string
identity_profile_instance = IdentityProfile.from_json(json)
# print the JSON string representation of the object
print(IdentityProfile.to_json())

# convert the object into a dict
identity_profile_dict = identity_profile_instance.to_dict()
# create an instance of IdentityProfile from a dict
identity_profile_from_dict = IdentityProfile.from_dict(identity_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


