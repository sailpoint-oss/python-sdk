# CreateScheduledSearchRequest


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

## Example

```python
from sailpoint.v3.models.create_scheduled_search_request import CreateScheduledSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledSearchRequest from a JSON string
create_scheduled_search_request_instance = CreateScheduledSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduledSearchRequest.to_json())

# convert the object into a dict
create_scheduled_search_request_dict = create_scheduled_search_request_instance.to_dict()
# create an instance of CreateScheduledSearchRequest from a dict
create_scheduled_search_request_from_dict = CreateScheduledSearchRequest.from_dict(create_scheduled_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


