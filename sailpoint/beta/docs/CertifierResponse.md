# CertifierResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of the certifier | [optional] 
**display_name** | **str** | the name of the certifier | [optional] 

## Example

```python
from beta.models.certifier_response import CertifierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CertifierResponse from a JSON string
certifier_response_instance = CertifierResponse.from_json(json)
# print the JSON string representation of the object
print CertifierResponse.to_json()

# convert the object into a dict
certifier_response_dict = certifier_response_instance.to_dict()
# create an instance of CertifierResponse from a dict
certifier_response_form_dict = certifier_response.from_dict(certifier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


