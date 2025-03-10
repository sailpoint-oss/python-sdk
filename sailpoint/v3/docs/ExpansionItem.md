# ExpansionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account | [optional] 
**cause** | **str** | Cause of the expansion item. | [optional] 
**name** | **str** | The name of the item | [optional] 
**attribute_request** | [**AttributeRequest**](AttributeRequest.md) |  | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 
**id** | **str** | ID of the expansion item | [optional] 
**state** | **str** | State of the expansion item | [optional] 

## Example

```python
from sailpoint.v3.models.expansion_item import ExpansionItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExpansionItem from a JSON string
expansion_item_instance = ExpansionItem.from_json(json)
# print the JSON string representation of the object
print(ExpansionItem.to_json())

# convert the object into a dict
expansion_item_dict = expansion_item_instance.to_dict()
# create an instance of ExpansionItem from a dict
expansion_item_from_dict = ExpansionItem.from_dict(expansion_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


