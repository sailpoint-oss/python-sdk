# SourceHealthDto

Dto for source health data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of the Source | [optional] [readonly] 
**type** | **str** | Specifies the type of system being managed e.g. Active Directory, Workday, etc.. If you are creating a Delimited File source, you must set the &#x60;provisionasCsv&#x60; query parameter to &#x60;true&#x60;.  | [optional] 
**name** | **str** | the name of the source | [optional] 
**org** | **str** | source&#39;s org | [optional] 
**is_authoritative** | **bool** | Is the source authoritative | [optional] 
**is_cluster** | **bool** | Is the source in a cluster | [optional] 
**hostname** | **str** | source&#39;s hostname | [optional] 
**pod** | **str** | source&#39;s pod | [optional] 
**iq_service_version** | **str** | The version of the iqService | [optional] 
**status** | **str** | connection test result | [optional] 

## Example

```python
from sailpoint.v3.models.source_health_dto import SourceHealthDto

# TODO update the JSON string below
json = "{}"
# create an instance of SourceHealthDto from a JSON string
source_health_dto_instance = SourceHealthDto.from_json(json)
# print the JSON string representation of the object
print(SourceHealthDto.to_json())

# convert the object into a dict
source_health_dto_dict = source_health_dto_instance.to_dict()
# create an instance of SourceHealthDto from a dict
source_health_dto_from_dict = SourceHealthDto.from_dict(source_health_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


