# SearchFormDefinitionsByTenant400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** | **str** |  | [optional] 
**messages** | [**List[ErrorMessage]**](ErrorMessage.md) |  | [optional] 
**status_code** | **int** |  | [optional] 
**tracking_id** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.search_form_definitions_by_tenant400_response import SearchFormDefinitionsByTenant400Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFormDefinitionsByTenant400Response from a JSON string
search_form_definitions_by_tenant400_response_instance = SearchFormDefinitionsByTenant400Response.from_json(json)
# print the JSON string representation of the object
print(SearchFormDefinitionsByTenant400Response.to_json())

# convert the object into a dict
search_form_definitions_by_tenant400_response_dict = search_form_definitions_by_tenant400_response_instance.to_dict()
# create an instance of SearchFormDefinitionsByTenant400Response from a dict
search_form_definitions_by_tenant400_response_from_dict = SearchFormDefinitionsByTenant400Response.from_dict(search_form_definitions_by_tenant400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


