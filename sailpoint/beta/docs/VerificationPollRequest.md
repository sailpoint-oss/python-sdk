# VerificationPollRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Verification request Id | 

## Example

```python
from sailpoint.beta.models.verification_poll_request import VerificationPollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationPollRequest from a JSON string
verification_poll_request_instance = VerificationPollRequest.from_json(json)
# print the JSON string representation of the object
print VerificationPollRequest.to_json()

# convert the object into a dict
verification_poll_request_dict = verification_poll_request_instance.to_dict()
# create an instance of VerificationPollRequest from a dict
verification_poll_request_form_dict = verification_poll_request.from_dict(verification_poll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


