# KbaQuestion

KBA Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | KBA Question Id | 
**text** | **str** | KBA Question description | 
**has_answer** | **bool** | Denotes whether the KBA question has an answer configured for any user in the tenant | 
**num_answers** | **int** | Denotes the number of KBA configurations for this question | 

## Example

```python
from sailpoint.v3.models.kba_question import KbaQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of KbaQuestion from a JSON string
kba_question_instance = KbaQuestion.from_json(json)
# print the JSON string representation of the object
print(KbaQuestion.to_json())

# convert the object into a dict
kba_question_dict = kba_question_instance.to_dict()
# create an instance of KbaQuestion from a dict
kba_question_from_dict = KbaQuestion.from_dict(kba_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


