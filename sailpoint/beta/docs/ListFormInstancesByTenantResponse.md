# ListFormInstancesByTenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count number of Results | [optional] 
**results** | [**List[FormInstanceResponse]**](FormInstanceResponse.md) | Results holds a list of FormInstanceResponse items | [optional] 

## Example

```python
from sailpoint.beta.models.list_form_instances_by_tenant_response import ListFormInstancesByTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFormInstancesByTenantResponse from a JSON string
list_form_instances_by_tenant_response_instance = ListFormInstancesByTenantResponse.from_json(json)
# print the JSON string representation of the object
print ListFormInstancesByTenantResponse.to_json()

# convert the object into a dict
list_form_instances_by_tenant_response_dict = list_form_instances_by_tenant_response_instance.to_dict()
# create an instance of ListFormInstancesByTenantResponse from a dict
list_form_instances_by_tenant_response_form_dict = list_form_instances_by_tenant_response.from_dict(list_form_instances_by_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


