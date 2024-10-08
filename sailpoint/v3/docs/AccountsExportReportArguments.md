# AccountsExportReportArguments

Arguments for Account Export report (ACCOUNTS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | Source ID. | 
**source_name** | **str** | Source name. | 

## Example

```python
from sailpoint.v3.models.accounts_export_report_arguments import AccountsExportReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsExportReportArguments from a JSON string
accounts_export_report_arguments_instance = AccountsExportReportArguments.from_json(json)
# print the JSON string representation of the object
print(AccountsExportReportArguments.to_json())

# convert the object into a dict
accounts_export_report_arguments_dict = accounts_export_report_arguments_instance.to_dict()
# create an instance of AccountsExportReportArguments from a dict
accounts_export_report_arguments_from_dict = AccountsExportReportArguments.from_dict(accounts_export_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


