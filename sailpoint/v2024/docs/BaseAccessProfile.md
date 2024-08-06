# BaseAccessProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Access profile&#39;s unique ID. | [optional] 
**name** | **str** | Access profile&#39;s display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.base_access_profile import BaseAccessProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccessProfile from a JSON string
base_access_profile_instance = BaseAccessProfile.from_json(json)
# print the JSON string representation of the object
print BaseAccessProfile.to_json()

# convert the object into a dict
base_access_profile_dict = base_access_profile_instance.to_dict()
# create an instance of BaseAccessProfile from a dict
base_access_profile_form_dict = base_access_profile.from_dict(base_access_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


