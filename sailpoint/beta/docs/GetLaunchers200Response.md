# GetLaunchers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Pagination marker | [optional] 
**items** | [**List[Launcher]**](Launcher.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.get_launchers200_response import GetLaunchers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLaunchers200Response from a JSON string
get_launchers200_response_instance = GetLaunchers200Response.from_json(json)
# print the JSON string representation of the object
print(GetLaunchers200Response.to_json())

# convert the object into a dict
get_launchers200_response_dict = get_launchers200_response_instance.to_dict()
# create an instance of GetLaunchers200Response from a dict
get_launchers200_response_from_dict = GetLaunchers200Response.from_dict(get_launchers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


