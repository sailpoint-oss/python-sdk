# IdentitiesReportArguments

Arguments for Identities report (IDENTITIES)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlated_only** | **bool** | Boolean FLAG to specify if only correlated identities should be used in report processing | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.identities_report_arguments import IdentitiesReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitiesReportArguments from a JSON string
identities_report_arguments_instance = IdentitiesReportArguments.from_json(json)
# print the JSON string representation of the object
print IdentitiesReportArguments.to_json()

# convert the object into a dict
identities_report_arguments_dict = identities_report_arguments_instance.to_dict()
# create an instance of IdentitiesReportArguments from a dict
identities_report_arguments_form_dict = identities_report_arguments.from_dict(identities_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


