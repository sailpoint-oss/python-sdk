# KbaAnswerResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Question Id | 
**question** | **str** | Question description | 
**has_answer** | **bool** | Denotes whether the KBA question has an answer configured for the current user | 

## Example

```python
from sailpoint.beta.models.kba_answer_response_item import KbaAnswerResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of KbaAnswerResponseItem from a JSON string
kba_answer_response_item_instance = KbaAnswerResponseItem.from_json(json)
# print the JSON string representation of the object
print KbaAnswerResponseItem.to_json()

# convert the object into a dict
kba_answer_response_item_dict = kba_answer_response_item_instance.to_dict()
# create an instance of KbaAnswerResponseItem from a dict
kba_answer_response_item_form_dict = kba_answer_response_item.from_dict(kba_answer_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


