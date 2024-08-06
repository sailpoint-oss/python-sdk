# ResourceObject

Representation of the object which is returned from source connectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** | Identifier of the specific instance where this object resides. | [optional] [readonly] 
**identity** | **str** | Native identity of the object in the Source. | [optional] [readonly] 
**uuid** | **str** | Universal unique identifier of the object in the Source. | [optional] [readonly] 
**previous_identity** | **str** | Native identity that the object has previously. | [optional] [readonly] 
**name** | **str** | Display name for this object. | [optional] [readonly] 
**object_type** | **str** | Type of object. | [optional] [readonly] 
**incomplete** | **bool** | A flag indicating that this is an incomplete object. Used in special cases where the connector has to return account information in several phases and the objects might not have a complete set of all account attributes. The attributes in this object will replace the corresponding attributes in the Link, but no other Link attributes will be changed. | [optional] [readonly] 
**incremental** | **bool** | A flag indicating that this is an incremental change object. This is similar to incomplete but it also means that the values of any multi-valued attributes in this object should be merged with the existing values in the Link rather than replacing the existing Link value. | [optional] [readonly] 
**delete** | **bool** | A flag indicating that this object has been deleted. This is set only when doing delta aggregation and the connector supports detection of native deletes. | [optional] [readonly] 
**remove** | **bool** | A flag set indicating that the values in the attributes represent things to remove rather than things to add. Setting this implies incremental. The values which are always for multi-valued attributes are removed from the current values. | [optional] [readonly] 
**missing** | **List[str]** | A list of attribute names that are not included in this object. This is only used with SMConnector and will only contain \&quot;groups\&quot;. | [optional] [readonly] 
**attributes** | **object** | Attributes of this ResourceObject. | [optional] [readonly] 
**final_update** | **bool** | In Aggregation, for sparse object the count for total accounts scanned identities updated is not incremented. | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.resource_object import ResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceObject from a JSON string
resource_object_instance = ResourceObject.from_json(json)
# print the JSON string representation of the object
print ResourceObject.to_json()

# convert the object into a dict
resource_object_dict = resource_object_instance.to_dict()
# create an instance of ResourceObject from a dict
resource_object_form_dict = resource_object.from_dict(resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


