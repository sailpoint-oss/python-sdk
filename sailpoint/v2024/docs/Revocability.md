# Revocability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_schemes** | [**List[AccessProfileApprovalScheme]**](AccessProfileApprovalScheme.md) | List describing the steps in approving the revocation request | [optional] 

## Example

```python
from sailpoint.v2024.models.revocability import Revocability

# TODO update the JSON string below
json = "{}"
# create an instance of Revocability from a JSON string
revocability_instance = Revocability.from_json(json)
# print the JSON string representation of the object
print Revocability.to_json()

# convert the object into a dict
revocability_dict = revocability_instance.to_dict()
# create an instance of Revocability from a dict
revocability_form_dict = revocability.from_dict(revocability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


