# IdentityProfileIdentityErrorReportArguments

Arguments for Identity Profile Identity Error report (IDENTITY_PROFILE_IDENTITY_ERROR)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authoritative_source** | **str** | Source Id to be checked on errors of identity profiles aggregation | 
**default_s3_bucket** | **bool** | Use it to set default s3 bucket where generated report will be saved.  In case this argument is false and &#39;s3Bucket&#39; argument is null or absent there will be default s3Bucket assigned to the report. | 
**s3_bucket** | **str** | If you want to be specific you could use this argument with defaultS3Bucket &#x3D; false. | [optional] 

## Example

```python
from v3.models.identity_profile_identity_error_report_arguments import IdentityProfileIdentityErrorReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfileIdentityErrorReportArguments from a JSON string
identity_profile_identity_error_report_arguments_instance = IdentityProfileIdentityErrorReportArguments.from_json(json)
# print the JSON string representation of the object
print IdentityProfileIdentityErrorReportArguments.to_json()

# convert the object into a dict
identity_profile_identity_error_report_arguments_dict = identity_profile_identity_error_report_arguments_instance.to_dict()
# create an instance of IdentityProfileIdentityErrorReportArguments from a dict
identity_profile_identity_error_report_arguments_form_dict = identity_profile_identity_error_report_arguments.from_dict(identity_profile_identity_error_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


