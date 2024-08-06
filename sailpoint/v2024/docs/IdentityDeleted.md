# IdentityDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**IdentityDeletedIdentity**](IdentityDeletedIdentity.md) |  | 
**attributes** | **Dict[str, object]** | The attributes assigned to the identity. Attributes are determined by the identity profile. | 

## Example

```python
from sailpoint.v2024.models.identity_deleted import IdentityDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDeleted from a JSON string
identity_deleted_instance = IdentityDeleted.from_json(json)
# print the JSON string representation of the object
print IdentityDeleted.to_json()

# convert the object into a dict
identity_deleted_dict = identity_deleted_instance.to_dict()
# create an instance of IdentityDeleted from a dict
identity_deleted_form_dict = identity_deleted.from_dict(identity_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


