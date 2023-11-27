# ListPredefinedSelectOptionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[str]** | Results holds a list of PreDefinedSelectOption items | [optional] 

## Example

```python
from sailpoint.beta.models.list_predefined_select_options_response import ListPredefinedSelectOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPredefinedSelectOptionsResponse from a JSON string
list_predefined_select_options_response_instance = ListPredefinedSelectOptionsResponse.from_json(json)
# print the JSON string representation of the object
print ListPredefinedSelectOptionsResponse.to_json()

# convert the object into a dict
list_predefined_select_options_response_dict = list_predefined_select_options_response_instance.to_dict()
# create an instance of ListPredefinedSelectOptionsResponse from a dict
list_predefined_select_options_response_form_dict = list_predefined_select_options_response.from_dict(list_predefined_select_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


