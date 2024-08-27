# IdentityCompareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_item_diff** | **Dict[str, object]** | Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on completion of the violation check. | [optional] 

## Example

```python
from sailpoint.beta.models.identity_compare_response import IdentityCompareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCompareResponse from a JSON string
identity_compare_response_instance = IdentityCompareResponse.from_json(json)
# print the JSON string representation of the object
print(IdentityCompareResponse.to_json())

# convert the object into a dict
identity_compare_response_dict = identity_compare_response_instance.to_dict()
# create an instance of IdentityCompareResponse from a dict
identity_compare_response_from_dict = IdentityCompareResponse.from_dict(identity_compare_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


