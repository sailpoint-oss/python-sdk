# Owns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[Reference]**](Reference.md) |  | [optional] 
**entitlements** | [**List[Reference]**](Reference.md) |  | [optional] 
**access_profiles** | [**List[Reference]**](Reference.md) |  | [optional] 
**roles** | [**List[Reference]**](Reference.md) |  | [optional] 
**apps** | [**List[Reference]**](Reference.md) |  | [optional] 
**governance_groups** | [**List[Reference]**](Reference.md) |  | [optional] 
**fallback_approver** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v3.models.owns import Owns

# TODO update the JSON string below
json = "{}"
# create an instance of Owns from a JSON string
owns_instance = Owns.from_json(json)
# print the JSON string representation of the object
print Owns.to_json()

# convert the object into a dict
owns_dict = owns_instance.to_dict()
# create an instance of Owns from a dict
owns_form_dict = owns.from_dict(owns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


