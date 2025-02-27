# IdentityProfile1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**description** | **str** | Identity profile&#39;s description. | [optional] 
**owner** | [**IdentityProfileAllOfOwner**](IdentityProfileAllOfOwner.md) |  | [optional] 
**priority** | **int** | Identity profile&#39;s priority. | [optional] 
**authoritative_source** | [**IdentityProfile1AllOfAuthoritativeSource**](IdentityProfile1AllOfAuthoritativeSource.md) |  | 
**identity_refresh_required** | **bool** | Set this value to &#39;True&#39; if an identity refresh is necessary. You would typically want to trigger an identity refresh when a change has been made on the source. | [optional] [default to False]
**identity_count** | **int** | Number of identities belonging to the identity profile. | [optional] 
**identity_attribute_config** | [**IdentityAttributeConfig1**](IdentityAttributeConfig1.md) |  | [optional] 
**identity_exception_report_reference** | [**IdentityExceptionReportReference1**](IdentityExceptionReportReference1.md) |  | [optional] 
**has_time_based_attr** | **bool** | Indicates the value of &#x60;requiresPeriodicRefresh&#x60; attribute for the identity profile. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.identity_profile1 import IdentityProfile1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfile1 from a JSON string
identity_profile1_instance = IdentityProfile1.from_json(json)
# print the JSON string representation of the object
print(IdentityProfile1.to_json())

# convert the object into a dict
identity_profile1_dict = identity_profile1_instance.to_dict()
# create an instance of IdentityProfile1 from a dict
identity_profile1_from_dict = IdentityProfile1.from_dict(identity_profile1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


