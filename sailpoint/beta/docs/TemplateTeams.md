# TemplateTeams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**message_json** | **str** |  | [optional] 
**is_subscription** | **bool** |  | [optional] 
**approval_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**requested_by_id** | **str** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**auto_approval_data** | [**TemplateSlackAutoApprovalData**](TemplateSlackAutoApprovalData.md) |  | [optional] 
**custom_fields** | [**TemplateSlackCustomFields**](TemplateSlackCustomFields.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.template_teams import TemplateTeams

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTeams from a JSON string
template_teams_instance = TemplateTeams.from_json(json)
# print the JSON string representation of the object
print TemplateTeams.to_json()

# convert the object into a dict
template_teams_dict = template_teams_instance.to_dict()
# create an instance of TemplateTeams from a dict
template_teams_form_dict = template_teams.from_dict(template_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


