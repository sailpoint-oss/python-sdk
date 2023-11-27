# AccessItemEntitlementResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | the access item type. entitlement in this case | [optional] 
**id** | **str** | the access item id | [optional] 
**attribute** | **str** | the entitlement attribute | [optional] 
**value** | **str** | the associated value | [optional] 
**entitlement_type** | **str** | the type of entitlement | [optional] 
**source_name** | **str** | the name of the source | [optional] 
**source_id** | **str** | the id of the source | [optional] 
**description** | **str** | the description for the entitlment | [optional] 
**display_name** | **str** | the display name of the identity | [optional] 

## Example

```python
from sailpoint.beta.models.access_item_entitlement_response import AccessItemEntitlementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemEntitlementResponse from a JSON string
access_item_entitlement_response_instance = AccessItemEntitlementResponse.from_json(json)
# print the JSON string representation of the object
print AccessItemEntitlementResponse.to_json()

# convert the object into a dict
access_item_entitlement_response_dict = access_item_entitlement_response_instance.to_dict()
# create an instance of AccessItemEntitlementResponse from a dict
access_item_entitlement_response_form_dict = access_item_entitlement_response.from_dict(access_item_entitlement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


