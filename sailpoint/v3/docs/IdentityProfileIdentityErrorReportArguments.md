# IdentityProfileIdentityErrorReportArguments

Arguments for Identity Profile Identity Error report (IDENTITY_PROFILE_IDENTITY_ERROR)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authoritative_source** | **str** | Source ID. | 

## Example

```python
from sailpoint.v3.models.identity_profile_identity_error_report_arguments import IdentityProfileIdentityErrorReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfileIdentityErrorReportArguments from a JSON string
identity_profile_identity_error_report_arguments_instance = IdentityProfileIdentityErrorReportArguments.from_json(json)
# print the JSON string representation of the object
print(IdentityProfileIdentityErrorReportArguments.to_json())

# convert the object into a dict
identity_profile_identity_error_report_arguments_dict = identity_profile_identity_error_report_arguments_instance.to_dict()
# create an instance of IdentityProfileIdentityErrorReportArguments from a dict
identity_profile_identity_error_report_arguments_from_dict = IdentityProfileIdentityErrorReportArguments.from_dict(identity_profile_identity_error_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


