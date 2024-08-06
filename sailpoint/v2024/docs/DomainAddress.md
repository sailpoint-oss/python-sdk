# DomainAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | A domain address | [optional] 

## Example

```python
from sailpoint.v2024.models.domain_address import DomainAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAddress from a JSON string
domain_address_instance = DomainAddress.from_json(json)
# print the JSON string representation of the object
print DomainAddress.to_json()

# convert the object into a dict
domain_address_dict = domain_address_instance.to_dict()
# create an instance of DomainAddress from a dict
domain_address_form_dict = domain_address.from_dict(domain_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


