# EntitlementAccessModelMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AttributeDTO]**](AttributeDTO.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.entitlement_access_model_metadata import EntitlementAccessModelMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementAccessModelMetadata from a JSON string
entitlement_access_model_metadata_instance = EntitlementAccessModelMetadata.from_json(json)
# print the JSON string representation of the object
print EntitlementAccessModelMetadata.to_json()

# convert the object into a dict
entitlement_access_model_metadata_dict = entitlement_access_model_metadata_instance.to_dict()
# create an instance of EntitlementAccessModelMetadata from a dict
entitlement_access_model_metadata_form_dict = entitlement_access_model_metadata.from_dict(entitlement_access_model_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


