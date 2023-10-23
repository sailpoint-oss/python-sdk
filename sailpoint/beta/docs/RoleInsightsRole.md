# RoleInsightsRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Role name | [optional] 
**id** | **str** | Role id | [optional] 
**description** | **str** | Role description | [optional] 
**owner_name** | **str** | Role owner name | [optional] 
**owner_id** | **str** | Role owner id | [optional] 

## Example

```python
from beta.models.role_insights_role import RoleInsightsRole

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsRole from a JSON string
role_insights_role_instance = RoleInsightsRole.from_json(json)
# print the JSON string representation of the object
print RoleInsightsRole.to_json()

# convert the object into a dict
role_insights_role_dict = role_insights_role_instance.to_dict()
# create an instance of RoleInsightsRole from a dict
role_insights_role_form_dict = role_insights_role.from_dict(role_insights_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


