# CreateDomainDkim405Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_name** | **object** | A message describing the error | [optional] 
**error_message** | **object** | Description of the error | [optional] 
**tracking_id** | **str** | Unique tracking id for the error. | [optional] 

## Example

```python
from sailpoint.beta.models.create_domain_dkim405_response import CreateDomainDkim405Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainDkim405Response from a JSON string
create_domain_dkim405_response_instance = CreateDomainDkim405Response.from_json(json)
# print the JSON string representation of the object
print(CreateDomainDkim405Response.to_json())

# convert the object into a dict
create_domain_dkim405_response_dict = create_domain_dkim405_response_instance.to_dict()
# create an instance of CreateDomainDkim405Response from a dict
create_domain_dkim405_response_from_dict = CreateDomainDkim405Response.from_dict(create_domain_dkim405_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


