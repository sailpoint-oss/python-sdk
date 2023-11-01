# ReviewableEntitlement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id for the entitlement | [optional] 
**name** | **str** | The name of the entitlement | [optional] 
**description** | **str** | Information about the entitlement | [optional] 
**privileged** | **bool** | Indicates if the entitlement is a privileged entitlement | [optional] [default to False]
**owner** | [**IdentityReferenceWithNameAndEmail**](IdentityReferenceWithNameAndEmail.md) |  | [optional] 
**attribute_name** | **str** | The name of the attribute on the source | [optional] 
**attribute_value** | **str** | The value of the attribute on the source | [optional] 
**source_schema_object_type** | **str** | The schema object type on the source used to represent the entitlement and its attributes | [optional] 
**source_name** | **str** | The name of the source for which this entitlement belongs | [optional] 
**source_type** | **str** | The type of the source for which the entitlement belongs | [optional] 
**source_id** | **str** | The ID of the source for which the entitlement belongs | [optional] 
**has_permissions** | **bool** | Indicates if the entitlement has permissions | [optional] [default to False]
**is_permission** | **bool** | Indicates if the entitlement is a representation of an account permission | [optional] [default to False]
**revocable** | **bool** | Indicates whether the entitlement can be revoked | [optional] [default to False]
**cloud_governed** | **bool** | True if the entitlement is cloud governed | [optional] [default to False]
**contains_data_access** | **bool** | True if the entitlement has DAS data | [optional] [default to False]
**data_access** | [**DataAccess**](DataAccess.md) |  | [optional] 
**account** | [**ReviewableEntitlementAccount**](ReviewableEntitlementAccount.md) |  | [optional] 

## Example

```python
from v3.models.reviewable_entitlement import ReviewableEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewableEntitlement from a JSON string
reviewable_entitlement_instance = ReviewableEntitlement.from_json(json)
# print the JSON string representation of the object
print ReviewableEntitlement.to_json()

# convert the object into a dict
reviewable_entitlement_dict = reviewable_entitlement_instance.to_dict()
# create an instance of ReviewableEntitlement from a dict
reviewable_entitlement_form_dict = reviewable_entitlement.from_dict(reviewable_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


