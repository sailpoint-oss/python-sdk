# CustomPasswordInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** | The page ID that represents the page for forget user name, reset password and unlock account flow. | [optional] 
**page_content** | **str** | The custom instructions for the specified page. Allow basic HTML format and maximum length is 1000 characters. The custom instructions will be sanitized to avoid attacks. If the customization text includes a link, like &lt;A HREF&#x3D;\\\&quot;URL\\\&quot;&gt;...&lt;/A&gt; clicking on this will open the link on the current browser page. If you want your link to be redirected to a different page, please redirect it to \&quot;_blank\&quot; like this: &lt;a href&#x3D;\\\&quot;URL\&quot; target&#x3D;\\\&quot;_blank\\\&quot; &gt;link&lt;/a&gt;. This will open a new tab when the link is clicked. Notice we&#39;re only supporting _blank as the redirection target. | [optional] 
**locale** | **str** | The locale for the custom instructions, a BCP47 language tag. The default value is \\\&quot;default\\\&quot;. | [optional] 

## Example

```python
from sailpoint.v2024.models.custom_password_instruction import CustomPasswordInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPasswordInstruction from a JSON string
custom_password_instruction_instance = CustomPasswordInstruction.from_json(json)
# print the JSON string representation of the object
print(CustomPasswordInstruction.to_json())

# convert the object into a dict
custom_password_instruction_dict = custom_password_instruction_instance.to_dict()
# create an instance of CustomPasswordInstruction from a dict
custom_password_instruction_from_dict = CustomPasswordInstruction.from_dict(custom_password_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


