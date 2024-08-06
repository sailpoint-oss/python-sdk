# ReportConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** | Name of column in report | [optional] 
**required** | **bool** | If true, column is required in all reports, and this entry is immutable. A 400 error will result from any attempt to modify the column&#39;s definition. | [optional] [default to False]
**included** | **bool** | If true, column is included in the report. A 400 error will be thrown if an attempt is made to set included&#x3D;false if required&#x3D;&#x3D;true. | [optional] [default to False]
**order** | **int** | Relative sort order for the column. Columns will be displayed left-to-right in nondecreasing order. | [optional] 

## Example

```python
from sailpoint.v2024.models.report_config_dto import ReportConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReportConfigDTO from a JSON string
report_config_dto_instance = ReportConfigDTO.from_json(json)
# print the JSON string representation of the object
print ReportConfigDTO.to_json()

# convert the object into a dict
report_config_dto_dict = report_config_dto_instance.to_dict()
# create an instance of ReportConfigDTO from a dict
report_config_dto_form_dict = report_config_dto.from_dict(report_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


