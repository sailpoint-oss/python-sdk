# ListConnectors200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**items** | [**List[ListConnectors200ResponseItemsInner]**](ListConnectors200ResponseItemsInner.md) |  | [optional] 

## Example

```python
from sailpoint.cc.models.list_connectors200_response import ListConnectors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectors200Response from a JSON string
list_connectors200_response_instance = ListConnectors200Response.from_json(json)
# print the JSON string representation of the object
print ListConnectors200Response.to_json()

# convert the object into a dict
list_connectors200_response_dict = list_connectors200_response_instance.to_dict()
# create an instance of ListConnectors200Response from a dict
list_connectors200_response_form_dict = list_connectors200_response.from_dict(list_connectors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


