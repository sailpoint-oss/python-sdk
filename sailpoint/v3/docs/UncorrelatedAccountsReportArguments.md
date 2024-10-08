# UncorrelatedAccountsReportArguments

Arguments for Uncorrelated Accounts report (UNCORRELATED_ACCOUNTS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_formats** | **List[str]** | Output report file formats. These are formats for calling GET endpoint as query parameter &#39;fileFormat&#39;.  In case report won&#39;t have this argument there will be [&#39;CSV&#39;, &#39;PDF&#39;] as default. | [optional] 

## Example

```python
from sailpoint.v3.models.uncorrelated_accounts_report_arguments import UncorrelatedAccountsReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of UncorrelatedAccountsReportArguments from a JSON string
uncorrelated_accounts_report_arguments_instance = UncorrelatedAccountsReportArguments.from_json(json)
# print the JSON string representation of the object
print(UncorrelatedAccountsReportArguments.to_json())

# convert the object into a dict
uncorrelated_accounts_report_arguments_dict = uncorrelated_accounts_report_arguments_instance.to_dict()
# create an instance of UncorrelatedAccountsReportArguments from a dict
uncorrelated_accounts_report_arguments_from_dict = UncorrelatedAccountsReportArguments.from_dict(uncorrelated_accounts_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


