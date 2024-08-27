# DkimAttributes

DKIM attributes for a domain or identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID associated with domain to be verified | [optional] 
**address** | **str** | The identity or domain address | [optional] 
**dkim_enabled** | **bool** | Whether or not DKIM has been enabled for this domain / identity | [optional] [default to False]
**dkim_tokens** | **List[str]** | The tokens to be added to a DNS for verification | [optional] 
**dkim_verification_status** | **str** | The current status if the domain /identity has been verified. Ie Success, Failed, Pending | [optional] 

## Example

```python
from sailpoint.v2024.models.dkim_attributes import DkimAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DkimAttributes from a JSON string
dkim_attributes_instance = DkimAttributes.from_json(json)
# print the JSON string representation of the object
print(DkimAttributes.to_json())

# convert the object into a dict
dkim_attributes_dict = dkim_attributes_instance.to_dict()
# create an instance of DkimAttributes from a dict
dkim_attributes_from_dict = DkimAttributes.from_dict(dkim_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


