# SendTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The token request ID | [optional] 
**status** | **str** | Status of sending token | [optional] 
**error_message** | **str** | Error messages from token send request | [optional] 

## Example

```python
from sailpoint.v3.models.send_token_response import SendTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendTokenResponse from a JSON string
send_token_response_instance = SendTokenResponse.from_json(json)
# print the JSON string representation of the object
print SendTokenResponse.to_json()

# convert the object into a dict
send_token_response_dict = send_token_response_instance.to_dict()
# create an instance of SendTokenResponse from a dict
send_token_response_form_dict = send_token_response.from_dict(send_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


