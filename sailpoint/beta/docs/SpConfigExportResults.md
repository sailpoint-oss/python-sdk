# SpConfigExportResults

Response model for config export download response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Current version of the export results object. | [optional] 
**timestamp** | **datetime** | Time the export was completed. | [optional] 
**tenant** | **str** | Name of the tenant where this export originated. | [optional] 
**description** | **str** | Optional user defined description/name for export job. | [optional] 
**options** | [**ExportOptions**](ExportOptions.md) |  | [optional] 
**objects** | [**List[ConfigObject]**](ConfigObject.md) |  | [optional] 

## Example

```python
from beta.models.sp_config_export_results import SpConfigExportResults

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigExportResults from a JSON string
sp_config_export_results_instance = SpConfigExportResults.from_json(json)
# print the JSON string representation of the object
print SpConfigExportResults.to_json()

# convert the object into a dict
sp_config_export_results_dict = sp_config_export_results_instance.to_dict()
# create an instance of SpConfigExportResults from a dict
sp_config_export_results_form_dict = sp_config_export_results.from_dict(sp_config_export_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


