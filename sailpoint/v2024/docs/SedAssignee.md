# SedAssignee

Sed Assignee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of assignment When value is PERSONA, the value MUST be SOURCE_OWNER or ENTITLEMENT_OWNER IDENTITY SED_ASSIGNEE_IDENTITY_TYPE GROUP SED_ASSIGNEE_GROUP_TYPE SOURCE_OWNER SED_ASSIGNEE_SOURCE_OWNER_TYPE ENTITLEMENT_OWNER SED_ASSIGNEE_ENTITLEMENT_OWNER_TYPE | 
**value** | **str** | Identity or Group identifier Empty when using source/entitlement owner personas | [optional] 

## Example

```python
from sailpoint.v2024.models.sed_assignee import SedAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of SedAssignee from a JSON string
sed_assignee_instance = SedAssignee.from_json(json)
# print the JSON string representation of the object
print(SedAssignee.to_json())

# convert the object into a dict
sed_assignee_dict = sed_assignee_instance.to_dict()
# create an instance of SedAssignee from a dict
sed_assignee_from_dict = SedAssignee.from_dict(sed_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


