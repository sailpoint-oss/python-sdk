# TemplateSlackAutoApprovalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_approved** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**auto_approval_message_json** | **str** |  | [optional] 
**auto_approval_title** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.template_slack_auto_approval_data import TemplateSlackAutoApprovalData

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSlackAutoApprovalData from a JSON string
template_slack_auto_approval_data_instance = TemplateSlackAutoApprovalData.from_json(json)
# print the JSON string representation of the object
print(TemplateSlackAutoApprovalData.to_json())

# convert the object into a dict
template_slack_auto_approval_data_dict = template_slack_auto_approval_data_instance.to_dict()
# create an instance of TemplateSlackAutoApprovalData from a dict
template_slack_auto_approval_data_from_dict = TemplateSlackAutoApprovalData.from_dict(template_slack_auto_approval_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


