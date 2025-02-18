# RoleDocumentAllOfDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the dimension. | [optional] 
**name** | **str** | Name of the dimension. | [optional] 
**description** | **str** | Description of the dimension. | [optional] 
**entitlements** | [**List[RoleDocumentAllOfEntitlements1]**](RoleDocumentAllOfEntitlements1.md) | Entitlements included with the role. | [optional] 
**access_profiles** | [**List[BaseAccessProfile]**](BaseAccessProfile.md) | Access profiles included in the dimension. | [optional] 

## Example

```python
from sailpoint.v3.models.role_document_all_of_dimensions import RoleDocumentAllOfDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDocumentAllOfDimensions from a JSON string
role_document_all_of_dimensions_instance = RoleDocumentAllOfDimensions.from_json(json)
# print the JSON string representation of the object
print(RoleDocumentAllOfDimensions.to_json())

# convert the object into a dict
role_document_all_of_dimensions_dict = role_document_all_of_dimensions_instance.to_dict()
# create an instance of RoleDocumentAllOfDimensions from a dict
role_document_all_of_dimensions_from_dict = RoleDocumentAllOfDimensions.from_dict(role_document_all_of_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


