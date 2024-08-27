# IdentityAssociationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | any additional context information of the http call result | [optional] 
**association_details** | [**List[IdentityAssociationDetailsAssociationDetailsInner]**](IdentityAssociationDetailsAssociationDetailsInner.md) | list of all the resource associations for the identity | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_association_details import IdentityAssociationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssociationDetails from a JSON string
identity_association_details_instance = IdentityAssociationDetails.from_json(json)
# print the JSON string representation of the object
print(IdentityAssociationDetails.to_json())

# convert the object into a dict
identity_association_details_dict = identity_association_details_instance.to_dict()
# create an instance of IdentityAssociationDetails from a dict
identity_association_details_from_dict = IdentityAssociationDetails.from_dict(identity_association_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


