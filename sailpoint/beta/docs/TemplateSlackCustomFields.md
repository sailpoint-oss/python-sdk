# TemplateSlackCustomFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** |  | [optional] 
**contains_deny** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**campaign_status** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.template_slack_custom_fields import TemplateSlackCustomFields

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSlackCustomFields from a JSON string
template_slack_custom_fields_instance = TemplateSlackCustomFields.from_json(json)
# print the JSON string representation of the object
print TemplateSlackCustomFields.to_json()

# convert the object into a dict
template_slack_custom_fields_dict = template_slack_custom_fields_instance.to_dict()
# create an instance of TemplateSlackCustomFields from a dict
template_slack_custom_fields_form_dict = template_slack_custom_fields.from_dict(template_slack_custom_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


