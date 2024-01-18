# SearchSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saved_search_id** | **str** | The ID of the saved search that will be executed. | 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] [readonly] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] [readonly] 
**schedule** | [**Schedule1**](Schedule1.md) |  | 
**recipients** | [**List[SearchScheduleRecipientsInner]**](SearchScheduleRecipientsInner.md) | A list of identities that should receive the scheduled search report via email. | 
**enabled** | **bool** | Indicates if the scheduled search is enabled.  | [optional] [default to False]
**email_empty_results** | **bool** | Indicates if email generation should occur when search returns no results.  | [optional] [default to False]
**display_query_details** | **bool** | Indicates if the generated email should include the query and search results preview (which could include PII).  | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.search_schedule import SearchSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSchedule from a JSON string
search_schedule_instance = SearchSchedule.from_json(json)
# print the JSON string representation of the object
print SearchSchedule.to_json()

# convert the object into a dict
search_schedule_dict = search_schedule_instance.to_dict()
# create an instance of SearchSchedule from a dict
search_schedule_form_dict = search_schedule.from_dict(search_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


