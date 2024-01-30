# Reviewer

Details of the reviewer for certification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The reviewer&#39;s DTO type. | 
**id** | **str** | The reviewer&#39;s ID. | 
**name** | **str** | The reviewer&#39;s display name. | 
**email** | **str** | The reviewing identity&#39;s email. Only applicable to &#x60;IDENTITY&#x60;. | [optional] 

## Example

```python
from sailpoint.beta.models.reviewer import Reviewer

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


