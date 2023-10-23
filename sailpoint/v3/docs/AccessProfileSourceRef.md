# AccessProfileSourceRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Source with with which the Access Profile is associated | [optional] 
**type** | **str** | The type of the Source, will always be SOURCE | [optional] 
**name** | **str** | The display name of the associated Source | [optional] 

## Example

```python
from v3.models.access_profile_source_ref import AccessProfileSourceRef

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileSourceRef from a JSON string
access_profile_source_ref_instance = AccessProfileSourceRef.from_json(json)
# print the JSON string representation of the object
print AccessProfileSourceRef.to_json()

# convert the object into a dict
access_profile_source_ref_dict = access_profile_source_ref_instance.to_dict()
# create an instance of AccessProfileSourceRef from a dict
access_profile_source_ref_form_dict = access_profile_source_ref.from_dict(access_profile_source_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


