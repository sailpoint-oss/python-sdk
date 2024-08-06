# KbaAnswerRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Question Id | 
**answer** | **str** | An answer for the KBA question | 

## Example

```python
from sailpoint.v2024.models.kba_answer_request_item import KbaAnswerRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of KbaAnswerRequestItem from a JSON string
kba_answer_request_item_instance = KbaAnswerRequestItem.from_json(json)
# print the JSON string representation of the object
print KbaAnswerRequestItem.to_json()

# convert the object into a dict
kba_answer_request_item_dict = kba_answer_request_item_instance.to_dict()
# create an instance of KbaAnswerRequestItem from a dict
kba_answer_request_item_form_dict = kba_answer_request_item.from_dict(kba_answer_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


