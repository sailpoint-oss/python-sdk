# KbaAuthResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_id** | **str** | The KBA question id | [optional] 
**is_verified** | **bool** | Return true if verified | [optional] 

## Example

```python
from sailpoint.beta.models.kba_auth_response_item import KbaAuthResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of KbaAuthResponseItem from a JSON string
kba_auth_response_item_instance = KbaAuthResponseItem.from_json(json)
# print the JSON string representation of the object
print KbaAuthResponseItem.to_json()

# convert the object into a dict
kba_auth_response_item_dict = kba_auth_response_item_instance.to_dict()
# create an instance of KbaAuthResponseItem from a dict
kba_auth_response_item_form_dict = kba_auth_response_item.from_dict(kba_auth_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


