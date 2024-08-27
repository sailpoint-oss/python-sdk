# NetworkConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **List[str]** | The collection of ip ranges. | [optional] 
**geolocation** | **List[str]** | The collection of country codes. | [optional] 
**whitelisted** | **bool** | Denotes whether the provided lists are whitelisted or blacklisted for geo location. | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.network_configuration import NetworkConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConfiguration from a JSON string
network_configuration_instance = NetworkConfiguration.from_json(json)
# print the JSON string representation of the object
print(NetworkConfiguration.to_json())

# convert the object into a dict
network_configuration_dict = network_configuration_instance.to_dict()
# create an instance of NetworkConfiguration from a dict
network_configuration_from_dict = NetworkConfiguration.from_dict(network_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


