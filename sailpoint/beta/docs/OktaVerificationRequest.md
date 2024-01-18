# OktaVerificationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User identifier for Verification request. The value of the user&#39;s attribute. | 

## Example

```python
from sailpoint.beta.models.okta_verification_request import OktaVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OktaVerificationRequest from a JSON string
okta_verification_request_instance = OktaVerificationRequest.from_json(json)
# print the JSON string representation of the object
print OktaVerificationRequest.to_json()

# convert the object into a dict
okta_verification_request_dict = okta_verification_request_instance.to_dict()
# create an instance of OktaVerificationRequest from a dict
okta_verification_request_form_dict = okta_verification_request.from_dict(okta_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


