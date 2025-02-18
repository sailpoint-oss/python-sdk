# BaseAccessOwner

Owner's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner&#39;s DTO type. | [optional] 
**id** | **str** | Owner&#39;s identity ID. | [optional] 
**name** | **str** | Owner&#39;s display name. | [optional] 
**email** | **str** | Owner&#39;s email. | [optional] 

## Example

```python
from sailpoint.v3.models.base_access_owner import BaseAccessOwner

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccessOwner from a JSON string
base_access_owner_instance = BaseAccessOwner.from_json(json)
# print the JSON string representation of the object
print(BaseAccessOwner.to_json())

# convert the object into a dict
base_access_owner_dict = base_access_owner_instance.to_dict()
# create an instance of BaseAccessOwner from a dict
base_access_owner_from_dict = BaseAccessOwner.from_dict(base_access_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


