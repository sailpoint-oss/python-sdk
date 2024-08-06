# ImportUploadedBackupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | JSON file containing the objects to be imported. | 
**name** | **str** | Name that will be assigned to the uploaded file. | 

## Example

```python
from sailpoint.v2024.models.import_uploaded_backup_request import ImportUploadedBackupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportUploadedBackupRequest from a JSON string
import_uploaded_backup_request_instance = ImportUploadedBackupRequest.from_json(json)
# print the JSON string representation of the object
print ImportUploadedBackupRequest.to_json()

# convert the object into a dict
import_uploaded_backup_request_dict = import_uploaded_backup_request_instance.to_dict()
# create an instance of ImportUploadedBackupRequest from a dict
import_uploaded_backup_request_form_dict = import_uploaded_backup_request.from_dict(import_uploaded_backup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


