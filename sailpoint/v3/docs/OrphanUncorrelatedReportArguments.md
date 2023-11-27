# OrphanUncorrelatedReportArguments

Arguments for Orphan Identities report (ORPHAN_IDENTITIES) and Uncorrelated Accounts report (UNCORRELATED_ACCOUNTS)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_formats** | **List[str]** | Output report file formats. This are formats for calling get endpoint as a query parameter &#39;fileFormat&#39;.  In case report won&#39;t have this argument there will be [&#39;CSV&#39;, &#39;PDF&#39;] as default. | [optional] 
**default_s3_bucket** | **bool** | Use it to set default s3 bucket where generated report will be saved.  In case this argument is false and &#39;s3Bucket&#39; argument is null or absent there will be default s3Bucket assigned to the report. | 
**s3_bucket** | **str** | If you want to be specific you could use this argument with defaultS3Bucket &#x3D; false. | [optional] 

## Example

```python
from sailpoint.v3.models.orphan_uncorrelated_report_arguments import OrphanUncorrelatedReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of OrphanUncorrelatedReportArguments from a JSON string
orphan_uncorrelated_report_arguments_instance = OrphanUncorrelatedReportArguments.from_json(json)
# print the JSON string representation of the object
print OrphanUncorrelatedReportArguments.to_json()

# convert the object into a dict
orphan_uncorrelated_report_arguments_dict = orphan_uncorrelated_report_arguments_instance.to_dict()
# create an instance of OrphanUncorrelatedReportArguments from a dict
orphan_uncorrelated_report_arguments_form_dict = orphan_uncorrelated_report_arguments.from_dict(orphan_uncorrelated_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


