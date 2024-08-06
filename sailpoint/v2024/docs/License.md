# License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** | Name of the license | [optional] 
**legacy_feature_name** | **str** | Legacy name of the license | [optional] 

## Example

```python
from sailpoint.v2024.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print License.to_json()

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_form_dict = license.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


