# CertificationReference1

Previous certification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of certification for review. | [optional] 
**id** | **str** | ID of certification for review. | [optional] 
**name** | **str** | Display name of certification for review. | [optional] 
**reviewer** | [**Reviewer1**](Reviewer1.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.certification_reference1 import CertificationReference1

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationReference1 from a JSON string
certification_reference1_instance = CertificationReference1.from_json(json)
# print the JSON string representation of the object
print CertificationReference1.to_json()

# convert the object into a dict
certification_reference1_dict = certification_reference1_instance.to_dict()
# create an instance of CertificationReference1 from a dict
certification_reference1_form_dict = certification_reference1.from_dict(certification_reference1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


