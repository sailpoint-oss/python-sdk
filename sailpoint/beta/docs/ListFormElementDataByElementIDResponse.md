# ListFormElementDataByElementIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FormElementDataSourceConfigOptions]**](FormElementDataSourceConfigOptions.md) | Results holds a list of FormElementDataSourceConfigOptions items | [optional] 

## Example

```python
from sailpoint.beta.models.list_form_element_data_by_element_id_response import ListFormElementDataByElementIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFormElementDataByElementIDResponse from a JSON string
list_form_element_data_by_element_id_response_instance = ListFormElementDataByElementIDResponse.from_json(json)
# print the JSON string representation of the object
print ListFormElementDataByElementIDResponse.to_json()

# convert the object into a dict
list_form_element_data_by_element_id_response_dict = list_form_element_data_by_element_id_response_instance.to_dict()
# create an instance of ListFormElementDataByElementIDResponse from a dict
list_form_element_data_by_element_id_response_form_dict = list_form_element_data_by_element_id_response.from_dict(list_form_element_data_by_element_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


