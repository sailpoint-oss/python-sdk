# PutCorrelationConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector correlation config xml file | 

## Example

```python
from sailpoint.v3.models.put_correlation_config_request import PutCorrelationConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCorrelationConfigRequest from a JSON string
put_correlation_config_request_instance = PutCorrelationConfigRequest.from_json(json)
# print the JSON string representation of the object
print PutCorrelationConfigRequest.to_json()

# convert the object into a dict
put_correlation_config_request_dict = put_correlation_config_request_instance.to_dict()
# create an instance of PutCorrelationConfigRequest from a dict
put_correlation_config_request_form_dict = put_correlation_config_request.from_dict(put_correlation_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


