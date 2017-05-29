# swagger_client.InventoryApi

All URIs are relative to *https://test.interthings.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_create**](InventoryApi.md#devices_create) | **POST** /api/v1/inventory/devices/ | create a device
[**devices_delete**](InventoryApi.md#devices_delete) | **DELETE** /api/v1/inventory/devices/{id}/ | delete a device
[**devices_list**](InventoryApi.md#devices_list) | **GET** /api/v1/inventory/devices/ | list all devices
[**devices_partial_update**](InventoryApi.md#devices_partial_update) | **PATCH** /api/v1/inventory/devices/{id}/ | update fields on a device
[**devices_read**](InventoryApi.md#devices_read) | **GET** /api/v1/inventory/devices/{id}/ | get a device
[**devices_update**](InventoryApi.md#devices_update) | **PUT** /api/v1/inventory/devices/{id}/ | update a device
[**systems_create**](InventoryApi.md#systems_create) | **POST** /api/v1/inventory/systems/ | create a system
[**systems_delete**](InventoryApi.md#systems_delete) | **DELETE** /api/v1/inventory/systems/{id}/ | delete a system
[**systems_list**](InventoryApi.md#systems_list) | **GET** /api/v1/inventory/systems/ | list all systems
[**systems_partial_update**](InventoryApi.md#systems_partial_update) | **PATCH** /api/v1/inventory/systems/{id}/ | update fields on a system
[**systems_read**](InventoryApi.md#systems_read) | **GET** /api/v1/inventory/systems/{id}/ | get a system
[**systems_update**](InventoryApi.md#systems_update) | **PUT** /api/v1/inventory/systems/{id}/ | update a system


# **devices_create**
> devices_create(data=data)

create a device

create a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
data = swagger_client.Data39() # Data39 |  (optional)

try: 
    # create a device
    api_instance.devices_create(data=data)
except ApiException as e:
    print("Exception when calling InventoryApi->devices_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data39**](Data39.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_delete**
> devices_delete(id)

delete a device

delete a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 

try: 
    # delete a device
    api_instance.devices_delete(id)
except ApiException as e:
    print("Exception when calling InventoryApi->devices_delete: %s\n" % e)
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

# **devices_list**
> devices_list()

list all devices

list all devices

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()

try: 
    # list all devices
    api_instance.devices_list()
except ApiException as e:
    print("Exception when calling InventoryApi->devices_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_partial_update**
> devices_partial_update(id, data=data)

update fields on a device

update fields on a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 
data = swagger_client.Data41() # Data41 |  (optional)

try: 
    # update fields on a device
    api_instance.devices_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling InventoryApi->devices_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data41**](Data41.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_read**
> devices_read(id)

get a device

get a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 

try: 
    # get a device
    api_instance.devices_read(id)
except ApiException as e:
    print("Exception when calling InventoryApi->devices_read: %s\n" % e)
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

# **devices_update**
> devices_update(id, data=data)

update a device

update a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 
data = swagger_client.Data40() # Data40 |  (optional)

try: 
    # update a device
    api_instance.devices_update(id, data=data)
except ApiException as e:
    print("Exception when calling InventoryApi->devices_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data40**](Data40.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_create**
> systems_create(data=data)

create a system

create a system

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
data = swagger_client.Data42() # Data42 |  (optional)

try: 
    # create a system
    api_instance.systems_create(data=data)
except ApiException as e:
    print("Exception when calling InventoryApi->systems_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data42**](Data42.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_delete**
> systems_delete(id)

delete a system

delete a system

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 

try: 
    # delete a system
    api_instance.systems_delete(id)
except ApiException as e:
    print("Exception when calling InventoryApi->systems_delete: %s\n" % e)
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

# **systems_list**
> systems_list()

list all systems

list all systems

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()

try: 
    # list all systems
    api_instance.systems_list()
except ApiException as e:
    print("Exception when calling InventoryApi->systems_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_partial_update**
> systems_partial_update(id, data=data)

update fields on a system

update fields on a system

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 
data = swagger_client.Data44() # Data44 |  (optional)

try: 
    # update fields on a system
    api_instance.systems_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling InventoryApi->systems_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data44**](Data44.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_read**
> systems_read(id)

get a system

get a system

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 

try: 
    # get a system
    api_instance.systems_read(id)
except ApiException as e:
    print("Exception when calling InventoryApi->systems_read: %s\n" % e)
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

# **systems_update**
> systems_update(id, data=data)

update a system

update a system

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
id = 'id_example' # str | 
data = swagger_client.Data43() # Data43 |  (optional)

try: 
    # update a system
    api_instance.systems_update(id, data=data)
except ApiException as e:
    print("Exception when calling InventoryApi->systems_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data43**](Data43.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

