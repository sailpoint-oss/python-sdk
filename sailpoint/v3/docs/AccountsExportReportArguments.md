# AccountsExportReportArguments

Arguments for Account Export (ACCOUNTS)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | Id of the authoritative source to export related accounts e.g. identities | 
**source_name** | **str** | Name of the authoritative source for accounts export | 
**default_s3_bucket** | **bool** | Use it to set default s3 bucket where generated report will be saved.  In case this argument is false and &#39;s3Bucket&#39; argument is null or absent there will be default s3Bucket assigned to the report. | 
**s3_bucket** | **str** | If you want to be specific you could use this argument with defaultS3Bucket &#x3D; false. | [optional] 

## Example

```python
from v3.models.accounts_export_report_arguments import AccountsExportReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsExportReportArguments from a JSON string
accounts_export_report_arguments_instance = AccountsExportReportArguments.from_json(json)
# print the JSON string representation of the object
print AccountsExportReportArguments.to_json()

# convert the object into a dict
accounts_export_report_arguments_dict = accounts_export_report_arguments_instance.to_dict()
# create an instance of AccountsExportReportArguments from a dict
accounts_export_report_arguments_form_dict = accounts_export_report_arguments.from_dict(accounts_export_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


