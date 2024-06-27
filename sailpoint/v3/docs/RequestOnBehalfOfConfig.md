# RequestOnBehalfOfConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_request_on_behalf_of_anyone_by_anyone** | **bool** | If this is true, anyone can request access for anyone. | [optional] [default to False]
**allow_request_on_behalf_of_employee_by_manager** | **bool** | If this is true, a manager can request access for his or her direct reports. | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.request_on_behalf_of_config import RequestOnBehalfOfConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RequestOnBehalfOfConfig from a JSON string
request_on_behalf_of_config_instance = RequestOnBehalfOfConfig.from_json(json)
# print the JSON string representation of the object
print RequestOnBehalfOfConfig.to_json()

# convert the object into a dict
request_on_behalf_of_config_dict = request_on_behalf_of_config_instance.to_dict()
# create an instance of RequestOnBehalfOfConfig from a dict
request_on_behalf_of_config_form_dict = request_on_behalf_of_config.from_dict(request_on_behalf_of_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


