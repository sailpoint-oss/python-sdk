# SourceAccountCorrelationConfig

Reference to an Account Correlation Config object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the account correlation config | [optional] 
**name** | **str** | Human-readable display name of the account correlation config | [optional] 

## Example

```python
from beta.models.source_account_correlation_config import SourceAccountCorrelationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAccountCorrelationConfig from a JSON string
source_account_correlation_config_instance = SourceAccountCorrelationConfig.from_json(json)
# print the JSON string representation of the object
print SourceAccountCorrelationConfig.to_json()

# convert the object into a dict
source_account_correlation_config_dict = source_account_correlation_config_instance.to_dict()
# create an instance of SourceAccountCorrelationConfig from a dict
source_account_correlation_config_form_dict = source_account_correlation_config.from_dict(source_account_correlation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


