# VerificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The verificationPollRequest request ID | [optional] 
**status** | **str** | MFA Authentication status | [optional] 
**error** | **str** | Error messages from MFA verification request | [optional] 

## Example

```python
from sailpoint.v3.models.verification_response import VerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationResponse from a JSON string
verification_response_instance = VerificationResponse.from_json(json)
# print the JSON string representation of the object
print VerificationResponse.to_json()

# convert the object into a dict
verification_response_dict = verification_response_instance.to_dict()
# create an instance of VerificationResponse from a dict
verification_response_form_dict = verification_response.from_dict(verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


