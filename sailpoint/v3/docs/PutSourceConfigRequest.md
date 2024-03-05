# PutSourceConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector source config xml file | 

## Example

```python
from sailpoint.v3.models.put_source_config_request import PutSourceConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSourceConfigRequest from a JSON string
put_source_config_request_instance = PutSourceConfigRequest.from_json(json)
# print the JSON string representation of the object
print PutSourceConfigRequest.to_json()

# convert the object into a dict
put_source_config_request_dict = put_source_config_request_instance.to_dict()
# create an instance of PutSourceConfigRequest from a dict
put_source_config_request_form_dict = put_source_config_request.from_dict(put_source_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


