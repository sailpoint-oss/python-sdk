---
id: consolidation
title: Consolidation
pagination_label: consolidation
sidebar_label: consolidation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'consolidation', 'consolidation'] 
slug: /tools/sdk/python//methods/consolidation
tags: ['SDK', 'Software Development Kit', 'consolidation', 'consolidation']
---

# sailpoint.nerm.ConsolidationApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-master-record**](#delete-master-record) | **DELETE** `/idproxy/identities/{id}` | Delete a master record
[**patch-data-record**](#patch-data-record) | **PATCH** `/idproxy/data_records/{id}/reassign` | Reassign data record


## delete-master-record
Delete a master record
Consolidation is a deprecated feature, this endpoint provides a mechanism to delete a master record to assist customers.

[API Spec](https://developer.sailpoint.com/docs/api//delete-master-record)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Master record deleted. |  |  -  |
400 | Error deleting master record | DeleteMasterRecord400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.consolidation_api import ConsolidationApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a master record
        
        ConsolidationApi(api_client).delete_master_record(id=id)
        # Below is a request that includes all optional parameters
        # ConsolidationApi(api_client).delete_master_record(id)
    except Exception as e:
        print("Exception when calling ConsolidationApi->delete_master_record: %s\n" % e)
```



[[Back to top]](#) 

## patch-data-record
Reassign data record
Consolidation is a deprecated feature, this endpoint provides a mechanism to reassign a data record to a new master record to assist customers.

[API Spec](https://developer.sailpoint.com/docs/api//patch-data-record)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | data_records | [**DataRecords**](../models/data-records) | True  | 

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | The data record has been reassigned. |  |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.consolidation_api import ConsolidationApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.data_records import DataRecords
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    data_records = '''{
          "master_record_id" : "456738c9ba999a0076cf8a9b"
        }''' # DataRecords | 

    try:
        # Reassign data record
        new_data_records = DataRecords.from_json(data_records)
        ConsolidationApi(api_client).patch_data_record(id=id, data_records=new_data_records)
        # Below is a request that includes all optional parameters
        # ConsolidationApi(api_client).patch_data_record(id, new_data_records)
    except Exception as e:
        print("Exception when calling ConsolidationApi->patch_data_record: %s\n" % e)
```



[[Back to top]](#) 



