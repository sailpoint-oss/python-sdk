# SearchArguments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | The ID of the scheduled search that triggered the saved search execution.  | [optional] 
**owner** | [**TypedReference**](TypedReference.md) |  | [optional] 
**recipients** | [**List[TypedReference]**](TypedReference.md) | The email recipients of the scheduled search being tested.  | [optional] 

## Example

```python
from sailpoint.v3.models.search_arguments import SearchArguments

# TODO update the JSON string below
json = "{}"
# create an instance of SearchArguments from a JSON string
search_arguments_instance = SearchArguments.from_json(json)
# print the JSON string representation of the object
print SearchArguments.to_json()

# convert the object into a dict
search_arguments_dict = search_arguments_instance.to_dict()
# create an instance of SearchArguments from a dict
search_arguments_form_dict = search_arguments.from_dict(search_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


