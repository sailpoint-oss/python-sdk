# IdentityCreated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**IdentityCreatedIdentity**](IdentityCreatedIdentity.md) |  | 
**attributes** | **Dict[str, object]** | The attributes assigned to the identity.  Attributes are determined by the identity profile. | 

## Example

```python
from beta.models.identity_created import IdentityCreated

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCreated from a JSON string
identity_created_instance = IdentityCreated.from_json(json)
# print the JSON string representation of the object
print IdentityCreated.to_json()

# convert the object into a dict
identity_created_dict = identity_created_instance.to_dict()
# create an instance of IdentityCreated from a dict
identity_created_form_dict = identity_created.from_dict(identity_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


