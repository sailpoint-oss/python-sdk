# SetIconRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **bytearray** | file with icon. Allowed mime-types [&#39;image/png&#39;, &#39;image/jpeg&#39;] | 

## Example

```python
from sailpoint.beta.models.set_icon_request import SetIconRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetIconRequest from a JSON string
set_icon_request_instance = SetIconRequest.from_json(json)
# print the JSON string representation of the object
print(SetIconRequest.to_json())

# convert the object into a dict
set_icon_request_dict = set_icon_request_instance.to_dict()
# create an instance of SetIconRequest from a dict
set_icon_request_from_dict = SetIconRequest.from_dict(set_icon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


