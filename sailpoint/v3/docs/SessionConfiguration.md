# SessionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_idle_time** | **int** | The maximum time in minutes a session can be idle. | [optional] 
**remember_me** | **bool** | Denotes if &#39;remember me&#39; is enabled. | [optional] [default to False]
**max_session_time** | **int** | The maximum allowable session time in minutes. | [optional] 

## Example

```python
from sailpoint.v3.models.session_configuration import SessionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SessionConfiguration from a JSON string
session_configuration_instance = SessionConfiguration.from_json(json)
# print the JSON string representation of the object
print(SessionConfiguration.to_json())

# convert the object into a dict
session_configuration_dict = session_configuration_instance.to_dict()
# create an instance of SessionConfiguration from a dict
session_configuration_from_dict = SessionConfiguration.from_dict(session_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


