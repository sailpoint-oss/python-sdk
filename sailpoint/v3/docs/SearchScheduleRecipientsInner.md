# SearchScheduleRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | 
**id** | **str** | The ID of the referenced object | 

## Example

```python
from v3.models.search_schedule_recipients_inner import SearchScheduleRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchScheduleRecipientsInner from a JSON string
search_schedule_recipients_inner_instance = SearchScheduleRecipientsInner.from_json(json)
# print the JSON string representation of the object
print SearchScheduleRecipientsInner.to_json()

# convert the object into a dict
search_schedule_recipients_inner_dict = search_schedule_recipients_inner_instance.to_dict()
# create an instance of SearchScheduleRecipientsInner from a dict
search_schedule_recipients_inner_form_dict = search_schedule_recipients_inner.from_dict(search_schedule_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


