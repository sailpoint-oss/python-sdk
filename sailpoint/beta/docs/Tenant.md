# Tenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the Tenant | [optional] [readonly] 
**name** | **str** | Abbreviated name of the Tenant | [optional] 
**full_name** | **str** | Human-readable name of the Tenant | [optional] 
**pod** | **str** | Deployment pod for the Tenant | [optional] 
**region** | **str** | Deployment region for the Tenant | [optional] 
**description** | **str** | Description of the Tenant | [optional] 
**products** | [**List[Product]**](Product.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print(Tenant.to_json())

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_from_dict = Tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


