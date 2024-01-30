# IdentityOwnershipAssociationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_details** | [**List[IdentityOwnershipAssociationDetailsAssociationDetailsInner]**](IdentityOwnershipAssociationDetailsAssociationDetailsInner.md) | list of all the resource associations for the identity | [optional] 

## Example

```python
from sailpoint.beta.models.identity_ownership_association_details import IdentityOwnershipAssociationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityOwnershipAssociationDetails from a JSON string
identity_ownership_association_details_instance = IdentityOwnershipAssociationDetails.from_json(json)
# print the JSON string representation of the object
print IdentityOwnershipAssociationDetails.to_json()

# convert the object into a dict
identity_ownership_association_details_dict = identity_ownership_association_details_instance.to_dict()
# create an instance of IdentityOwnershipAssociationDetails from a dict
identity_ownership_association_details_form_dict = identity_ownership_association_details.from_dict(identity_ownership_association_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


