# ImportFormDefinitionsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**FormDefinitionResponse**](FormDefinitionResponse.md) |  | [optional] 
**var_self** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from sailpoint.beta.models.import_form_definitions_request_inner import ImportFormDefinitionsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportFormDefinitionsRequestInner from a JSON string
import_form_definitions_request_inner_instance = ImportFormDefinitionsRequestInner.from_json(json)
# print the JSON string representation of the object
print ImportFormDefinitionsRequestInner.to_json()

# convert the object into a dict
import_form_definitions_request_inner_dict = import_form_definitions_request_inner_instance.to_dict()
# create an instance of ImportFormDefinitionsRequestInner from a dict
import_form_definitions_request_inner_form_dict = import_form_definitions_request_inner.from_dict(import_form_definitions_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


