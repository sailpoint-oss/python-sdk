# SendAccountVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | The source name where identity account password should be reset | [optional] 
**via** | **str** | The method to send notification | 

## Example

```python
from sailpoint.beta.models.send_account_verification_request import SendAccountVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendAccountVerificationRequest from a JSON string
send_account_verification_request_instance = SendAccountVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(SendAccountVerificationRequest.to_json())

# convert the object into a dict
send_account_verification_request_dict = send_account_verification_request_instance.to_dict()
# create an instance of SendAccountVerificationRequest from a dict
send_account_verification_request_from_dict = SendAccountVerificationRequest.from_dict(send_account_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


