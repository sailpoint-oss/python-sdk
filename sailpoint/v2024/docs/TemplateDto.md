# TemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the template | 
**name** | **str** | The name of the Task Manager Subscription | [optional] 
**medium** | **str** | The message medium. More mediums may be added in the future. | 
**locale** | **str** | The locale for the message text, a BCP 47 language tag. | 
**subject** | **str** | The subject line in the template | [optional] 
**header** | **str** | The header value is now located within the body field. If included with non-null values, will result in a 400. | [optional] 
**body** | **str** | The body in the template | [optional] 
**footer** | **str** | The footer value is now located within the body field. If included with non-null values, will result in a 400. | [optional] 
**var_from** | **str** | The \&quot;From:\&quot; address in the template | [optional] 
**reply_to** | **str** | The \&quot;Reply To\&quot; line in the template | [optional] 
**description** | **str** | The description in the template | [optional] 
**id** | **str** | This is auto-generated. | [optional] 
**created** | **datetime** | The time when this template is created. This is auto-generated. | [optional] 
**modified** | **datetime** | The time when this template was last modified. This is auto-generated. | [optional] 
**slack_template** | **str** |  | [optional] 
**teams_template** | **str** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.template_dto import TemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDto from a JSON string
template_dto_instance = TemplateDto.from_json(json)
# print the JSON string representation of the object
print(TemplateDto.to_json())

# convert the object into a dict
template_dto_dict = template_dto_instance.to_dict()
# create an instance of TemplateDto from a dict
template_dto_from_dict = TemplateDto.from_dict(template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


