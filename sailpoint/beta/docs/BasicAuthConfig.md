# BasicAuthConfig

Config required if BASIC_AUTH is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The username to authenticate. | [optional] 
**password** | **str** | The password to authenticate. On response, this field is set to null as to not return secrets. | [optional] 

## Example

```python
from sailpoint.beta.models.basic_auth_config import BasicAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAuthConfig from a JSON string
basic_auth_config_instance = BasicAuthConfig.from_json(json)
# print the JSON string representation of the object
print(BasicAuthConfig.to_json())

# convert the object into a dict
basic_auth_config_dict = basic_auth_config_instance.to_dict()
# create an instance of BasicAuthConfig from a dict
basic_auth_config_from_dict = BasicAuthConfig.from_dict(basic_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


