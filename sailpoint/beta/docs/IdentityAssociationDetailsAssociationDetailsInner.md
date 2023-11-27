# IdentityAssociationDetailsAssociationDetailsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type** | **str** | association type with the identity | [optional] 
**entities** | [**List[IdentityEntities]**](IdentityEntities.md) | the specific resource this identity has ownership on | [optional] 

## Example

```python
from sailpoint.beta.models.identity_association_details_association_details_inner import IdentityAssociationDetailsAssociationDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssociationDetailsAssociationDetailsInner from a JSON string
identity_association_details_association_details_inner_instance = IdentityAssociationDetailsAssociationDetailsInner.from_json(json)
# print the JSON string representation of the object
print IdentityAssociationDetailsAssociationDetailsInner.to_json()

# convert the object into a dict
identity_association_details_association_details_inner_dict = identity_association_details_association_details_inner_instance.to_dict()
# create an instance of IdentityAssociationDetailsAssociationDetailsInner from a dict
identity_association_details_association_details_inner_form_dict = identity_association_details_association_details_inner.from_dict(identity_association_details_association_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


