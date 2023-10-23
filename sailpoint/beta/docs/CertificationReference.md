# CertificationReference

The previous certification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that the reviewer is. | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
**reviewer** | [**Reviewer**](Reviewer.md) |  | [optional] 

## Example

```python
from beta.models.certification_reference import CertificationReference

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationReference from a JSON string
certification_reference_instance = CertificationReference.from_json(json)
# print the JSON string representation of the object
print CertificationReference.to_json()

# convert the object into a dict
certification_reference_dict = certification_reference_instance.to_dict()
# create an instance of CertificationReference from a dict
certification_reference_form_dict = certification_reference.from_dict(certification_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


