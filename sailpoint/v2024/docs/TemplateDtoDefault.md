# TemplateDtoDefault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the default template | [optional] 
**name** | **str** | The name of the default template | [optional] 
**medium** | **str** | The message medium. More mediums may be added in the future. | [optional] 
**locale** | **str** | The locale for the message text, a BCP 47 language tag. | [optional] 
**subject** | **str** | The subject of the default template | [optional] 
**header** | **str** | The header value is now located within the body field. If included with non-null values, will result in a 400. | [optional] 
**body** | **str** | The body of the default template | [optional] 
**footer** | **str** | The footer value is now located within the body field. If included with non-null values, will result in a 400. | [optional] 
**var_from** | **str** | The \&quot;From:\&quot; address of the default template | [optional] 
**reply_to** | **str** | The \&quot;Reply To\&quot; field of the default template | [optional] 
**description** | **str** | The description of the default template | [optional] 
**slack_template** | [**TemplateSlack**](TemplateSlack.md) |  | [optional] 
**teams_template** | [**TemplateTeams**](TemplateTeams.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.template_dto_default import TemplateDtoDefault

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDtoDefault from a JSON string
template_dto_default_instance = TemplateDtoDefault.from_json(json)
# print the JSON string representation of the object
print TemplateDtoDefault.to_json()

# convert the object into a dict
template_dto_default_dict = template_dto_default_instance.to_dict()
# create an instance of TemplateDtoDefault from a dict
template_dto_default_form_dict = template_dto_default.from_dict(template_dto_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


