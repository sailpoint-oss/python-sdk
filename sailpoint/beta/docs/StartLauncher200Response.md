# StartLauncher200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactive_process_id** | **str** | ID of the Interactive Process that was launched | 

## Example

```python
from sailpoint.beta.models.start_launcher200_response import StartLauncher200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StartLauncher200Response from a JSON string
start_launcher200_response_instance = StartLauncher200Response.from_json(json)
# print the JSON string representation of the object
print(StartLauncher200Response.to_json())

# convert the object into a dict
start_launcher200_response_dict = start_launcher200_response_instance.to_dict()
# create an instance of StartLauncher200Response from a dict
start_launcher200_response_from_dict = StartLauncher200Response.from_dict(start_launcher200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


