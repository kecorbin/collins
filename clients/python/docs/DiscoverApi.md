# swagger_client.DiscoverApi

All URIs are relative to *https://test.interthings.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scans_create**](DiscoverApi.md#scans_create) | **POST** /api/v1/discover/scans/ | create a scan
[**scans_delete**](DiscoverApi.md#scans_delete) | **DELETE** /api/v1/discover/scans/{id}/ | delete a scan
[**scans_list**](DiscoverApi.md#scans_list) | **GET** /api/v1/discover/scans/ | get all scans
[**scans_partial_update**](DiscoverApi.md#scans_partial_update) | **PATCH** /api/v1/discover/scans/{id}/ | update fields on a scan
[**scans_read**](DiscoverApi.md#scans_read) | **GET** /api/v1/discover/scans/{id}/ | get a scan
[**scans_update**](DiscoverApi.md#scans_update) | **PUT** /api/v1/discover/scans/{id}/ | update a scan
[**speedtests_create**](DiscoverApi.md#speedtests_create) | **POST** /api/v1/discover/speedtests/ | create a speed test
[**speedtests_delete**](DiscoverApi.md#speedtests_delete) | **DELETE** /api/v1/discover/speedtests/{id}/ | delete a speed test
[**speedtests_list**](DiscoverApi.md#speedtests_list) | **GET** /api/v1/discover/speedtests/ | list all speed tests
[**speedtests_partial_update**](DiscoverApi.md#speedtests_partial_update) | **PATCH** /api/v1/discover/speedtests/{id}/ | update fields on a speed test
[**speedtests_read**](DiscoverApi.md#speedtests_read) | **GET** /api/v1/discover/speedtests/{id}/ | get a speed test
[**speedtests_update**](DiscoverApi.md#speedtests_update) | **PUT** /api/v1/discover/speedtests/{id}/ | update a speed test


# **scans_create**
> scans_create(data=data)

create a scan

create a scan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
data = swagger_client.Data33() # Data33 |  (optional)

try: 
    # create a scan
    api_instance.scans_create(data=data)
except ApiException as e:
    print("Exception when calling DiscoverApi->scans_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data33**](Data33.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_delete**
> scans_delete(id)

delete a scan

delete a scan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 

try: 
    # delete a scan
    api_instance.scans_delete(id)
except ApiException as e:
    print("Exception when calling DiscoverApi->scans_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_list**
> scans_list(processed=processed, type=type)

get all scans

get all scans

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
processed = 'processed_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try: 
    # get all scans
    api_instance.scans_list(processed=processed, type=type)
except ApiException as e:
    print("Exception when calling DiscoverApi->scans_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_partial_update**
> scans_partial_update(id, data=data)

update fields on a scan

update fields on a scan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 
data = swagger_client.Data35() # Data35 |  (optional)

try: 
    # update fields on a scan
    api_instance.scans_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling DiscoverApi->scans_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data35**](Data35.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_read**
> scans_read(id)

get a scan

get a scan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 

try: 
    # get a scan
    api_instance.scans_read(id)
except ApiException as e:
    print("Exception when calling DiscoverApi->scans_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_update**
> scans_update(id, data=data)

update a scan

update a scan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 
data = swagger_client.Data34() # Data34 |  (optional)

try: 
    # update a scan
    api_instance.scans_update(id, data=data)
except ApiException as e:
    print("Exception when calling DiscoverApi->scans_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data34**](Data34.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speedtests_create**
> speedtests_create(data=data)

create a speed test

create a speed test

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
data = swagger_client.Data36() # Data36 |  (optional)

try: 
    # create a speed test
    api_instance.speedtests_create(data=data)
except ApiException as e:
    print("Exception when calling DiscoverApi->speedtests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data36**](Data36.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speedtests_delete**
> speedtests_delete(id)

delete a speed test

delete a speed test

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 

try: 
    # delete a speed test
    api_instance.speedtests_delete(id)
except ApiException as e:
    print("Exception when calling DiscoverApi->speedtests_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speedtests_list**
> speedtests_list(processed=processed, type=type)

list all speed tests

list all speed tests

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
processed = 'processed_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try: 
    # list all speed tests
    api_instance.speedtests_list(processed=processed, type=type)
except ApiException as e:
    print("Exception when calling DiscoverApi->speedtests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speedtests_partial_update**
> speedtests_partial_update(id, data=data)

update fields on a speed test

update fields on a speed test

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 
data = swagger_client.Data38() # Data38 |  (optional)

try: 
    # update fields on a speed test
    api_instance.speedtests_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling DiscoverApi->speedtests_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data38**](Data38.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speedtests_read**
> speedtests_read(id)

get a speed test

get a speed test

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 

try: 
    # get a speed test
    api_instance.speedtests_read(id)
except ApiException as e:
    print("Exception when calling DiscoverApi->speedtests_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speedtests_update**
> speedtests_update(id, data=data)

update a speed test

update a speed test

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoverApi()
id = 'id_example' # str | 
data = swagger_client.Data37() # Data37 |  (optional)

try: 
    # update a speed test
    api_instance.speedtests_update(id, data=data)
except ApiException as e:
    print("Exception when calling DiscoverApi->speedtests_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data37**](Data37.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

