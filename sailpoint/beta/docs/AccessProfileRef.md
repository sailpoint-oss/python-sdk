# AccessProfileRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Access Profile | [optional] 
**type** | **str** | Type of requested object. This field must be either left null or set to &#39;ACCESS_PROFILE&#39; when creating an Access Profile, otherwise a 400 Bad Request error will result. | [optional] 
**name** | **str** | Human-readable display name of the Access Profile. This field is ignored on input. | [optional] 

## Example

```python
from beta.models.access_profile_ref import AccessProfileRef

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileRef from a JSON string
access_profile_ref_instance = AccessProfileRef.from_json(json)
# print the JSON string representation of the object
print AccessProfileRef.to_json()

# convert the object into a dict
access_profile_ref_dict = access_profile_ref_instance.to_dict()
# create an instance of AccessProfileRef from a dict
access_profile_ref_form_dict = access_profile_ref.from_dict(access_profile_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


