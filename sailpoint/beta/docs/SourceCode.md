# SourceCode

SourceCode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | the version of the code | 
**script** | **str** | The code | 

## Example

```python
from sailpoint.beta.models.source_code import SourceCode

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCode from a JSON string
source_code_instance = SourceCode.from_json(json)
# print the JSON string representation of the object
print SourceCode.to_json()

# convert the object into a dict
source_code_dict = source_code_instance.to_dict()
# create an instance of SourceCode from a dict
source_code_form_dict = source_code.from_dict(source_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


