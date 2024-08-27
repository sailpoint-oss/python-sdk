# SectionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the FormItem | [optional] 
**label** | **str** | Label of the section | [optional] 
**form_items** | **List[object]** | List of FormItems. FormItems can be SectionDetails and/or FieldDetails | [optional] 

## Example

```python
from sailpoint.v3.models.section_details import SectionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SectionDetails from a JSON string
section_details_instance = SectionDetails.from_json(json)
# print the JSON string representation of the object
print(SectionDetails.to_json())

# convert the object into a dict
section_details_dict = section_details_instance.to_dict()
# create an instance of SectionDetails from a dict
section_details_from_dict = SectionDetails.from_dict(section_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


