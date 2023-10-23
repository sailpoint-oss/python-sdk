# EntitlementRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Entitlement | [optional] 
**type** | **str** | The type of the Entitlement, will always be ENTITLEMENT | [optional] 
**name** | **str** | The display name of the Entitlement | [optional] 

## Example

```python
from v3.models.entitlement_ref import EntitlementRef

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementRef from a JSON string
entitlement_ref_instance = EntitlementRef.from_json(json)
# print the JSON string representation of the object
print EntitlementRef.to_json()

# convert the object into a dict
entitlement_ref_dict = entitlement_ref_instance.to_dict()
# create an instance of EntitlementRef from a dict
entitlement_ref_form_dict = entitlement_ref.from_dict(entitlement_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


