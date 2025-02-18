# RoleDocumentAllOfEntitlements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_permissions** | **bool** | Indicates whether the entitlement has permissions. | [optional] [default to False]
**description** | **str** | Entitlement&#39;s description. | [optional] 
**attribute** | **str** | Entitlement attribute&#39;s name. | [optional] 
**value** | **str** | Entitlement&#39;s value. | [optional] 
**var_schema** | **str** | Entitlement&#39;s schema. | [optional] 
**privileged** | **bool** | Indicates whether the entitlement is privileged. | [optional] [default to False]
**id** | **str** | Entitlement&#39;s ID. | [optional] 
**name** | **str** | Entitlement&#39;s name. | [optional] 
**source_schema_object_type** | **str** | Schema objectType. | [optional] 
**hash** | **str** | Read-only calculated hash value of an entitlement. | [optional] 

## Example

```python
from sailpoint.v3.models.role_document_all_of_entitlements import RoleDocumentAllOfEntitlements

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDocumentAllOfEntitlements from a JSON string
role_document_all_of_entitlements_instance = RoleDocumentAllOfEntitlements.from_json(json)
# print the JSON string representation of the object
print(RoleDocumentAllOfEntitlements.to_json())

# convert the object into a dict
role_document_all_of_entitlements_dict = role_document_all_of_entitlements_instance.to_dict()
# create an instance of RoleDocumentAllOfEntitlements from a dict
role_document_all_of_entitlements_from_dict = RoleDocumentAllOfEntitlements.from_dict(role_document_all_of_entitlements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


