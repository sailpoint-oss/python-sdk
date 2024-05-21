# AccessRequestContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_attributes** | [**List[ContextAttributeDto]**](ContextAttributeDto.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.access_request_context import AccessRequestContext

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestContext from a JSON string
access_request_context_instance = AccessRequestContext.from_json(json)
# print the JSON string representation of the object
print AccessRequestContext.to_json()

# convert the object into a dict
access_request_context_dict = access_request_context_instance.to_dict()
# create an instance of AccessRequestContext from a dict
access_request_context_form_dict = access_request_context.from_dict(access_request_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


