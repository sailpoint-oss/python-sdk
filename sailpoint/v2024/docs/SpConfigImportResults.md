# SpConfigImportResults

Response Body for Config Import command.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Dict[str, ObjectImportResult1]**](ObjectImportResult1.md) | The results of an object configuration import job. | 
**export_job_id** | **str** | If a backup was performed before the import, this will contain the jobId of the backup job. This id can be used to retrieve the json file of the backup export. | [optional] 

## Example

```python
from sailpoint.v2024.models.sp_config_import_results import SpConfigImportResults

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigImportResults from a JSON string
sp_config_import_results_instance = SpConfigImportResults.from_json(json)
# print the JSON string representation of the object
print SpConfigImportResults.to_json()

# convert the object into a dict
sp_config_import_results_dict = sp_config_import_results_instance.to_dict()
# create an instance of SpConfigImportResults from a dict
sp_config_import_results_form_dict = sp_config_import_results.from_dict(sp_config_import_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


