# SendTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_alias** | **str** | User alias from table spt_identity field named &#39;name&#39; | 
**delivery_type** | **str** | Token delivery type | 

## Example

```python
from sailpoint.beta.models.send_token_request import SendTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendTokenRequest from a JSON string
send_token_request_instance = SendTokenRequest.from_json(json)
# print the JSON string representation of the object
print(SendTokenRequest.to_json())

# convert the object into a dict
send_token_request_dict = send_token_request_instance.to_dict()
# create an instance of SendTokenRequest from a dict
send_token_request_from_dict = SendTokenRequest.from_dict(send_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


