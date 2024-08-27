# DuoVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User id for Verification request. | 
**signed_response** | **str** | User id for Verification request. | 

## Example

```python
from sailpoint.beta.models.duo_verification_request import DuoVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuoVerificationRequest from a JSON string
duo_verification_request_instance = DuoVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(DuoVerificationRequest.to_json())

# convert the object into a dict
duo_verification_request_dict = duo_verification_request_instance.to_dict()
# create an instance of DuoVerificationRequest from a dict
duo_verification_request_from_dict = DuoVerificationRequest.from_dict(duo_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


