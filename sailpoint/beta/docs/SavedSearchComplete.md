# SavedSearchComplete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | A name for the report file. | 
**owner_email** | **str** | The email address of the identity that owns the saved search. | 
**owner_name** | **str** | The name of the identity that owns the saved search. | 
**query** | **str** | The search query that was used to generate the report. | 
**search_name** | **str** | The name of the saved search. | 
**search_results** | [**SavedSearchCompleteSearchResults**](SavedSearchCompleteSearchResults.md) |  | 
**signed_s3_url** | **str** | The Amazon S3 URL to download the report from. | 

## Example

```python
from sailpoint.beta.models.saved_search_complete import SavedSearchComplete

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchComplete from a JSON string
saved_search_complete_instance = SavedSearchComplete.from_json(json)
# print the JSON string representation of the object
print SavedSearchComplete.to_json()

# convert the object into a dict
saved_search_complete_dict = saved_search_complete_instance.to_dict()
# create an instance of SavedSearchComplete from a dict
saved_search_complete_form_dict = saved_search_complete.from_dict(saved_search_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


