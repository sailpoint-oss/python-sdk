# ImportSpConfigRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | JSON file containing the objects to be imported. | 
**options** | [**ImportOptions**](ImportOptions.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.import_sp_config_request import ImportSpConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSpConfigRequest from a JSON string
import_sp_config_request_instance = ImportSpConfigRequest.from_json(json)
# print the JSON string representation of the object
print ImportSpConfigRequest.to_json()

# convert the object into a dict
import_sp_config_request_dict = import_sp_config_request_instance.to_dict()
# create an instance of ImportSpConfigRequest from a dict
import_sp_config_request_form_dict = import_sp_config_request.from_dict(import_sp_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


