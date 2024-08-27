# IdentitiesDetailsReportArguments

Arguments for Identities details report (IDENTITIES_DETAILS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlated_only** | **bool** | Boolean FLAG to specify if only correlated identities should be used in report processing | [default to False]

## Example

```python
from sailpoint.v2024.models.identities_details_report_arguments import IdentitiesDetailsReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitiesDetailsReportArguments from a JSON string
identities_details_report_arguments_instance = IdentitiesDetailsReportArguments.from_json(json)
# print the JSON string representation of the object
print(IdentitiesDetailsReportArguments.to_json())

# convert the object into a dict
identities_details_report_arguments_dict = identities_details_report_arguments_instance.to_dict()
# create an instance of IdentitiesDetailsReportArguments from a dict
identities_details_report_arguments_from_dict = IdentitiesDetailsReportArguments.from_dict(identities_details_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


