# FormDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the form | [optional] 
**name** | **str** | Name of the form | [optional] 
**title** | **str** | The form title | [optional] 
**subtitle** | **str** | The form subtitle. | [optional] 
**target_user** | **str** | The name of the user that should be shown this form | [optional] 
**sections** | [**List[SectionDetails]**](SectionDetails.md) | Sections of the form | [optional] 

## Example

```python
from sailpoint.v2024.models.form_details import FormDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FormDetails from a JSON string
form_details_instance = FormDetails.from_json(json)
# print the JSON string representation of the object
print FormDetails.to_json()

# convert the object into a dict
form_details_dict = form_details_instance.to_dict()
# create an instance of FormDetails from a dict
form_details_form_dict = form_details.from_dict(form_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


