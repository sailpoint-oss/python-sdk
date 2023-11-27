# ImportFormDefinitions202Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ImportFormDefinitions202ResponseErrorsInner]**](ImportFormDefinitions202ResponseErrorsInner.md) |  | [optional] 
**imported_objects** | [**List[ExportFormDefinitionsByTenant200ResponseInner]**](ExportFormDefinitionsByTenant200ResponseInner.md) |  | [optional] 
**infos** | [**List[ImportFormDefinitions202ResponseErrorsInner]**](ImportFormDefinitions202ResponseErrorsInner.md) |  | [optional] 
**warnings** | [**List[ImportFormDefinitions202ResponseErrorsInner]**](ImportFormDefinitions202ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.import_form_definitions202_response import ImportFormDefinitions202Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportFormDefinitions202Response from a JSON string
import_form_definitions202_response_instance = ImportFormDefinitions202Response.from_json(json)
# print the JSON string representation of the object
print ImportFormDefinitions202Response.to_json()

# convert the object into a dict
import_form_definitions202_response_dict = import_form_definitions202_response_instance.to_dict()
# create an instance of ImportFormDefinitions202Response from a dict
import_form_definitions202_response_form_dict = import_form_definitions202_response.from_dict(import_form_definitions202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


