# BaseDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 

## Example

```python
from sailpoint.v3.models.base_document import BaseDocument

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDocument from a JSON string
base_document_instance = BaseDocument.from_json(json)
# print the JSON string representation of the object
print(BaseDocument.to_json())

# convert the object into a dict
base_document_dict = base_document_instance.to_dict()
# create an instance of BaseDocument from a dict
base_document_from_dict = BaseDocument.from_dict(base_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


