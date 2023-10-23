# DomainStatusDto

Domain status DTO containing everything required to verify via DKIM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | New UUID associated with domain to be verified | [optional] 
**domain** | **str** | A domain address | [optional] 
**dkim_enabled** | **object** | DKIM is enabled for this domain | [optional] 
**dkim_tokens** | **List[str]** | DKIM tokens required for authentication | [optional] 
**dkim_verification_status** | **str** | Status of DKIM authentication | [optional] 

## Example

```python
from beta.models.domain_status_dto import DomainStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of DomainStatusDto from a JSON string
domain_status_dto_instance = DomainStatusDto.from_json(json)
# print the JSON string representation of the object
print DomainStatusDto.to_json()

# convert the object into a dict
domain_status_dto_dict = domain_status_dto_instance.to_dict()
# create an instance of DomainStatusDto from a dict
domain_status_dto_form_dict = domain_status_dto.from_dict(domain_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


