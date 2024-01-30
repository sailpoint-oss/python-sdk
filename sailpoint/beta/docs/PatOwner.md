# PatOwner

Personal access token owner's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Personal access token owner&#39;s DTO type. | [optional] 
**id** | **str** | Personal access token owner&#39;s identity ID. | [optional] 
**name** | **str** | Personal access token owner&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.pat_owner import PatOwner

# TODO update the JSON string below
json = "{}"
# create an instance of PatOwner from a JSON string
pat_owner_instance = PatOwner.from_json(json)
# print the JSON string representation of the object
print PatOwner.to_json()

# convert the object into a dict
pat_owner_dict = pat_owner_instance.to_dict()
# create an instance of PatOwner from a dict
pat_owner_form_dict = pat_owner.from_dict(pat_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


