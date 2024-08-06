# TemplateSlack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**blocks** | **str** |  | [optional] 
**attachments** | **str** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**approval_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**requested_by_id** | **str** |  | [optional] 
**is_subscription** | **bool** |  | [optional] 
**auto_approval_data** | [**TemplateSlackAutoApprovalData**](TemplateSlackAutoApprovalData.md) |  | [optional] 
**custom_fields** | [**TemplateSlackCustomFields**](TemplateSlackCustomFields.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.template_slack import TemplateSlack

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSlack from a JSON string
template_slack_instance = TemplateSlack.from_json(json)
# print the JSON string representation of the object
print TemplateSlack.to_json()

# convert the object into a dict
template_slack_dict = template_slack_instance.to_dict()
# create an instance of TemplateSlack from a dict
template_slack_form_dict = template_slack.from_dict(template_slack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


