# CertificationReferenceDto

Certification for review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of certification for review. | [optional] 
**id** | **str** | ID of certification for review. | [optional] 
**name** | **str** | Display name of certification for review. | [optional] 

## Example

```python
from sailpoint.beta.models.certification_reference_dto import CertificationReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationReferenceDto from a JSON string
certification_reference_dto_instance = CertificationReferenceDto.from_json(json)
# print the JSON string representation of the object
print(CertificationReferenceDto.to_json())

# convert the object into a dict
certification_reference_dto_dict = certification_reference_dto_instance.to_dict()
# create an instance of CertificationReferenceDto from a dict
certification_reference_dto_from_dict = CertificationReferenceDto.from_dict(certification_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


