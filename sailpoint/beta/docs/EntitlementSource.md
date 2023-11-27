# EntitlementSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source ID | [optional] 
**type** | **str** | The source type, will always be \&quot;SOURCE\&quot; | [optional] 
**name** | **str** | The source name | [optional] 

## Example

```python
from sailpoint.beta.models.entitlement_source import EntitlementSource

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementSource from a JSON string
entitlement_source_instance = EntitlementSource.from_json(json)
# print the JSON string representation of the object
print EntitlementSource.to_json()

# convert the object into a dict
entitlement_source_dict = entitlement_source_instance.to_dict()
# create an instance of EntitlementSource from a dict
entitlement_source_form_dict = entitlement_source.from_dict(entitlement_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


