# AccountSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**type** | **str** | Type of source returned. | [optional] 

## Example

```python
from sailpoint.v3.models.account_source import AccountSource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSource from a JSON string
account_source_instance = AccountSource.from_json(json)
# print the JSON string representation of the object
print AccountSource.to_json()

# convert the object into a dict
account_source_dict = account_source_instance.to_dict()
# create an instance of AccountSource from a dict
account_source_form_dict = account_source.from_dict(account_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


