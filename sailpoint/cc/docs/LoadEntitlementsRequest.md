# LoadEntitlementsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 

## Example

```python
from sailpoint.cc.models.load_entitlements_request import LoadEntitlementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoadEntitlementsRequest from a JSON string
load_entitlements_request_instance = LoadEntitlementsRequest.from_json(json)
# print the JSON string representation of the object
print LoadEntitlementsRequest.to_json()

# convert the object into a dict
load_entitlements_request_dict = load_entitlements_request_instance.to_dict()
# create an instance of LoadEntitlementsRequest from a dict
load_entitlements_request_form_dict = load_entitlements_request.from_dict(load_entitlements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


