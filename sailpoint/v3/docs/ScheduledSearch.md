# ScheduledSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the scheduled search.  | [optional] 
**description** | **str** | The description of the scheduled search.  | [optional] 
**saved_search_id** | **str** | The ID of the saved search that will be executed. | 
**created** | **datetime** | The date the scheduled search was initially created. | [optional] [readonly] 
**modified** | **datetime** | The last date the scheduled search was modified. | [optional] [readonly] 
**schedule** | [**Schedule1**](Schedule1.md) |  | 
**recipients** | [**List[SearchScheduleRecipientsInner]**](SearchScheduleRecipientsInner.md) | A list of identities that should receive the scheduled search report via email. | 
**enabled** | **bool** | Indicates if the scheduled search is enabled.  | [optional] [default to False]
**email_empty_results** | **bool** | Indicates if email generation should occur when search returns no results.  | [optional] [default to False]
**display_query_details** | **bool** | Indicates if the generated email should include the query and search results preview (which could include PII).  | [optional] [default to False]
**id** | **str** | The scheduled search ID. | [readonly] 
**owner** | [**ScheduledSearchAllOfOwner**](ScheduledSearchAllOfOwner.md) |  | 
**owner_id** | **str** | The ID of the scheduled search owner.  Please use the &#x60;id&#x60; in the &#x60;owner&#x60; object instead.  | [readonly] 

## Example

```python
from sailpoint.v3.models.scheduled_search import ScheduledSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledSearch from a JSON string
scheduled_search_instance = ScheduledSearch.from_json(json)
# print the JSON string representation of the object
print(ScheduledSearch.to_json())

# convert the object into a dict
scheduled_search_dict = scheduled_search_instance.to_dict()
# create an instance of ScheduledSearch from a dict
scheduled_search_from_dict = ScheduledSearch.from_dict(scheduled_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


