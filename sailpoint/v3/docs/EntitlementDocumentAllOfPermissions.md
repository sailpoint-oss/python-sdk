# EntitlementDocumentAllOfPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The target the permission would grants rights on. | [optional] 
**rights** | **List[str]** | All the rights (e.g. actions) that this permission allows on the target | [optional] 

## Example

```python
from sailpoint.v3.models.entitlement_document_all_of_permissions import EntitlementDocumentAllOfPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDocumentAllOfPermissions from a JSON string
entitlement_document_all_of_permissions_instance = EntitlementDocumentAllOfPermissions.from_json(json)
# print the JSON string representation of the object
print(EntitlementDocumentAllOfPermissions.to_json())

# convert the object into a dict
entitlement_document_all_of_permissions_dict = entitlement_document_all_of_permissions_instance.to_dict()
# create an instance of EntitlementDocumentAllOfPermissions from a dict
entitlement_document_all_of_permissions_from_dict = EntitlementDocumentAllOfPermissions.from_dict(entitlement_document_all_of_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


