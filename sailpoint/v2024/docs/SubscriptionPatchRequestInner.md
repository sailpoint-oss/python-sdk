# SubscriptionPatchRequestInner

A JSONPatch Operation as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation to be performed | 
**path** | **str** | A string JSON Pointer representing the target path to an element to be affected by the operation | 
**value** | [**SubscriptionPatchRequestInnerValue**](SubscriptionPatchRequestInnerValue.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.subscription_patch_request_inner import SubscriptionPatchRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPatchRequestInner from a JSON string
subscription_patch_request_inner_instance = SubscriptionPatchRequestInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPatchRequestInner.to_json())

# convert the object into a dict
subscription_patch_request_inner_dict = subscription_patch_request_inner_instance.to_dict()
# create an instance of SubscriptionPatchRequestInner from a dict
subscription_patch_request_inner_from_dict = SubscriptionPatchRequestInner.from_dict(subscription_patch_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


