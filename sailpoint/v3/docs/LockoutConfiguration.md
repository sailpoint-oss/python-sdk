# LockoutConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_attempts** | **int** | The maximum attempts allowed before lockout occurs. | [optional] 
**lockout_duration** | **int** | The total time in minutes a user will be locked out. | [optional] 
**lockout_window** | **int** | A rolling window where authentication attempts in a series count towards the maximum before lockout occurs. | [optional] 

## Example

```python
from sailpoint.v3.models.lockout_configuration import LockoutConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LockoutConfiguration from a JSON string
lockout_configuration_instance = LockoutConfiguration.from_json(json)
# print the JSON string representation of the object
print(LockoutConfiguration.to_json())

# convert the object into a dict
lockout_configuration_dict = lockout_configuration_instance.to_dict()
# create an instance of LockoutConfiguration from a dict
lockout_configuration_from_dict = LockoutConfiguration.from_dict(lockout_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


