# SedPatch

Patch for Suggested Entitlement Description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | desired operation | [optional] 
**path** | **str** | field to be patched | [optional] 
**value** | **object** | value to replace with | [optional] 

## Example

```python
from sailpoint.beta.models.sed_patch import SedPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SedPatch from a JSON string
sed_patch_instance = SedPatch.from_json(json)
# print the JSON string representation of the object
print SedPatch.to_json()

# convert the object into a dict
sed_patch_dict = sed_patch_instance.to_dict()
# create an instance of SedPatch from a dict
sed_patch_form_dict = sed_patch.from_dict(sed_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


