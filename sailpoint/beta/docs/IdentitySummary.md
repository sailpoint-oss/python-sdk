# IdentitySummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of this identity summary | [optional] 
**name** | **str** | Human-readable display name of identity | [optional] 
**identity_id** | **str** | ID of the identity that this summary represents | [optional] 
**completed** | **bool** | Indicates if all access items for this summary have been decided on | [optional] 

## Example

```python
from beta.models.identity_summary import IdentitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySummary from a JSON string
identity_summary_instance = IdentitySummary.from_json(json)
# print the JSON string representation of the object
print IdentitySummary.to_json()

# convert the object into a dict
identity_summary_dict = identity_summary_instance.to_dict()
# create an instance of IdentitySummary from a dict
identity_summary_form_dict = identity_summary.from_dict(identity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


