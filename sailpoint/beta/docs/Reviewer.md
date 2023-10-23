# Reviewer

Details of the reviewer for certification.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that the reviewer is. | 
**email** | **str** | The email of the reviewing identity. Only applicable to &#x60;IDENTITY&#x60; | [optional] 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.reviewer import Reviewer

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


