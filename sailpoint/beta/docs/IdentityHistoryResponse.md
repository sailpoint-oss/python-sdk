# IdentityHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identity ID | [optional] 
**display_name** | **str** | the display name of the identity | [optional] 
**snapshot** | **str** | the date when the identity record was created | [optional] 
**deleted_date** | **str** | the date when the identity was deleted | [optional] 
**access_item_count** | **Dict[str, int]** | A map containing the count of each access item | [optional] 
**attributes** | **Dict[str, object]** | A map containing the identity attributes | [optional] 

## Example

```python
from sailpoint.beta.models.identity_history_response import IdentityHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityHistoryResponse from a JSON string
identity_history_response_instance = IdentityHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(IdentityHistoryResponse.to_json())

# convert the object into a dict
identity_history_response_dict = identity_history_response_instance.to_dict()
# create an instance of IdentityHistoryResponse from a dict
identity_history_response_from_dict = IdentityHistoryResponse.from_dict(identity_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


