# Reviewer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the reviewer. | [optional] 
**name** | **str** | The name of the reviewer. | [optional] 
**email** | **str** | The email of the reviewing identity. | [optional] 
**type** | **str** | The type of the reviewing identity. | [optional] 
**created** | **datetime** | The created date of the reviewing identity. | [optional] 
**modified** | **datetime** | The modified date of the reviewing identity. | [optional] 

## Example

```python
from sailpoint.v3.models.reviewer import Reviewer

# TODO update the JSON string below
json = "{}"
# create an instance of Reviewer from a JSON string
reviewer_instance = Reviewer.from_json(json)
# print the JSON string representation of the object
print Reviewer.to_json()

# convert the object into a dict
reviewer_dict = reviewer_instance.to_dict()
# create an instance of Reviewer from a dict
reviewer_form_dict = reviewer.from_dict(reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


