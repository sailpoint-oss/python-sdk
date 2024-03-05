# BaseAccessAllOfOwner

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
from sailpoint.v3.models.base_access_all_of_owner import BaseAccessAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccessAllOfOwner from a JSON string
base_access_all_of_owner_instance = BaseAccessAllOfOwner.from_json(json)
# print the JSON string representation of the object
print BaseAccessAllOfOwner.to_json()

# convert the object into a dict
base_access_all_of_owner_dict = base_access_all_of_owner_instance.to_dict()
# create an instance of BaseAccessAllOfOwner from a dict
base_access_all_of_owner_form_dict = base_access_all_of_owner.from_dict(base_access_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


