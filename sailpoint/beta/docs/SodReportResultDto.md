# SodReportResultDto

SOD policy violation report result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | SOD policy violation report result DTO type. | [optional] 
**id** | **str** | SOD policy violation report result ID. | [optional] 
**name** | **str** | Human-readable name of the SOD policy violation report result. | [optional] 

## Example

```python
from sailpoint.beta.models.sod_report_result_dto import SodReportResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of SodReportResultDto from a JSON string
sod_report_result_dto_instance = SodReportResultDto.from_json(json)
# print the JSON string representation of the object
print(SodReportResultDto.to_json())

# convert the object into a dict
sod_report_result_dto_dict = sod_report_result_dto_instance.to_dict()
# create an instance of SodReportResultDto from a dict
sod_report_result_dto_from_dict = SodReportResultDto.from_dict(sod_report_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


