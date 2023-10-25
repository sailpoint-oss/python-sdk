# BulkDeleteWorkGroups200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **List[str]** |  | [optional] 
**in_use** | **List[str]** |  | [optional] 
**not_found** | **List[str]** |  | [optional] 

## Example

```python
from v2.models.bulk_delete_work_groups200_response import BulkDeleteWorkGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteWorkGroups200Response from a JSON string
bulk_delete_work_groups200_response_instance = BulkDeleteWorkGroups200Response.from_json(json)
# print the JSON string representation of the object
print BulkDeleteWorkGroups200Response.to_json()

# convert the object into a dict
bulk_delete_work_groups200_response_dict = bulk_delete_work_groups200_response_instance.to_dict()
# create an instance of BulkDeleteWorkGroups200Response from a dict
bulk_delete_work_groups200_response_form_dict = bulk_delete_work_groups200_response.from_dict(bulk_delete_work_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


