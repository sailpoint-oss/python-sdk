# IdentityAccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**source** | [**Reference**](Reference.md) |  | [optional] 
**owner** | [**DisplayReference**](DisplayReference.md) |  | [optional] 
**revocable** | **bool** |  | [optional] 
**privileged** | **bool** |  | [optional] 
**attribute** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**standalone** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v3.models.identity_access import IdentityAccess

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAccess from a JSON string
identity_access_instance = IdentityAccess.from_json(json)
# print the JSON string representation of the object
print IdentityAccess.to_json()

# convert the object into a dict
identity_access_dict = identity_access_instance.to_dict()
# create an instance of IdentityAccess from a dict
identity_access_form_dict = identity_access.from_dict(identity_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


