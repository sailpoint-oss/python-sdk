# KbaAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kba_auth_response_items** | [**List[KbaAuthResponseItem]**](KbaAuthResponseItem.md) |  | [optional] 
**status** | **str** | MFA Authentication status | [optional] 

## Example

```python
from sailpoint.v3.models.kba_auth_response import KbaAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KbaAuthResponse from a JSON string
kba_auth_response_instance = KbaAuthResponse.from_json(json)
# print the JSON string representation of the object
print(KbaAuthResponse.to_json())

# convert the object into a dict
kba_auth_response_dict = kba_auth_response_instance.to_dict()
# create an instance of KbaAuthResponse from a dict
kba_auth_response_from_dict = KbaAuthResponse.from_dict(kba_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


