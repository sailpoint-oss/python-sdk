# KbaAnswerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | [**List[KbaAnswerRequestItem]**](KbaAnswerRequestItem.md) | Kba answers | 

## Example

```python
from sailpoint.beta.models.kba_answer_request import KbaAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KbaAnswerRequest from a JSON string
kba_answer_request_instance = KbaAnswerRequest.from_json(json)
# print the JSON string representation of the object
print KbaAnswerRequest.to_json()

# convert the object into a dict
kba_answer_request_dict = kba_answer_request_instance.to_dict()
# create an instance of KbaAnswerRequest from a dict
kba_answer_request_form_dict = kba_answer_request.from_dict(kba_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


