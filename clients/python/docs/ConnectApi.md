# swagger_client.ConnectApi

All URIs are relative to *https://test.interthings.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createtunnel_create**](ConnectApi.md#createtunnel_create) | **POST** /api/v1/connect/createtunnel/ | create a tunnel
[**createtunnel_delete**](ConnectApi.md#createtunnel_delete) | **DELETE** /api/v1/connect/createtunnel/{id}/ | delete a tunnel
[**createtunnel_list**](ConnectApi.md#createtunnel_list) | **GET** /api/v1/connect/createtunnel/ | 
[**createtunnel_partial_update**](ConnectApi.md#createtunnel_partial_update) | **PATCH** /api/v1/connect/createtunnel/{id}/ | update fields on a tunnel
[**createtunnel_read**](ConnectApi.md#createtunnel_read) | **GET** /api/v1/connect/createtunnel/{id}/ | 
[**createtunnel_update**](ConnectApi.md#createtunnel_update) | **PUT** /api/v1/connect/createtunnel/{id}/ | update a tunnel
[**gateway_create**](ConnectApi.md#gateway_create) | **POST** /api/v1/connect/gateway/ | create a gateway
[**gateway_delete**](ConnectApi.md#gateway_delete) | **DELETE** /api/v1/connect/gateway/{hostname}/ | delete a gateway
[**gateway_list**](ConnectApi.md#gateway_list) | **GET** /api/v1/connect/gateway/ | list all gateways
[**gateway_partial_update**](ConnectApi.md#gateway_partial_update) | **PATCH** /api/v1/connect/gateway/{hostname}/ | update fields on a gateway
[**gateway_read**](ConnectApi.md#gateway_read) | **GET** /api/v1/connect/gateway/{hostname}/ | get a gateway
[**gateway_update**](ConnectApi.md#gateway_update) | **PUT** /api/v1/connect/gateway/{hostname}/ | update a Gateway
[**gateways_create**](ConnectApi.md#gateways_create) | **POST** /api/v1/connect/gateways/ | create a gateway
[**gateways_delete**](ConnectApi.md#gateways_delete) | **DELETE** /api/v1/connect/gateways/{hostname}/ | delete a gateway
[**gateways_list**](ConnectApi.md#gateways_list) | **GET** /api/v1/connect/gateways/ | list all gateways
[**gateways_partial_update**](ConnectApi.md#gateways_partial_update) | **PATCH** /api/v1/connect/gateways/{hostname}/ | update fields on a gateway
[**gateways_read**](ConnectApi.md#gateways_read) | **GET** /api/v1/connect/gateways/{hostname}/ | get a gateway
[**gateways_update**](ConnectApi.md#gateways_update) | **PUT** /api/v1/connect/gateways/{hostname}/ | update a Gateway
[**tunnel_create**](ConnectApi.md#tunnel_create) | **POST** /api/v1/connect/tunnel/ | create a tunnel
[**tunnel_delete**](ConnectApi.md#tunnel_delete) | **DELETE** /api/v1/connect/tunnel/{id}/ | delete a tunnel
[**tunnel_list**](ConnectApi.md#tunnel_list) | **GET** /api/v1/connect/tunnel/ | list all tunnels
[**tunnel_partial_update**](ConnectApi.md#tunnel_partial_update) | **PATCH** /api/v1/connect/tunnel/{id}/ | update fields on a tunnel
[**tunnel_read**](ConnectApi.md#tunnel_read) | **GET** /api/v1/connect/tunnel/{id}/ | get a tunnel
[**tunnel_update**](ConnectApi.md#tunnel_update) | **PUT** /api/v1/connect/tunnel/{id}/ | update a tunnel
[**tunnels_create**](ConnectApi.md#tunnels_create) | **POST** /api/v1/connect/tunnels/ | create a tunnel
[**tunnels_delete**](ConnectApi.md#tunnels_delete) | **DELETE** /api/v1/connect/tunnels/{id}/ | delete a tunnel
[**tunnels_list**](ConnectApi.md#tunnels_list) | **GET** /api/v1/connect/tunnels/ | list all tunnels
[**tunnels_partial_update**](ConnectApi.md#tunnels_partial_update) | **PATCH** /api/v1/connect/tunnels/{id}/ | update fields on a tunnel
[**tunnels_read**](ConnectApi.md#tunnels_read) | **GET** /api/v1/connect/tunnels/{id}/ | get a tunnel
[**tunnels_update**](ConnectApi.md#tunnels_update) | **PUT** /api/v1/connect/tunnels/{id}/ | update a tunnel


# **createtunnel_create**
> createtunnel_create(data=data)

create a tunnel

create a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
data = swagger_client.Data18() # Data18 |  (optional)

try: 
    # create a tunnel
    api_instance.createtunnel_create(data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->createtunnel_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data18**](Data18.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createtunnel_delete**
> createtunnel_delete(id)

delete a tunnel

delete a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 

try: 
    # delete a tunnel
    api_instance.createtunnel_delete(id)
except ApiException as e:
    print("Exception when calling ConnectApi->createtunnel_delete: %s\n" % e)
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

# **createtunnel_list**
> createtunnel_list()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()

try: 
    api_instance.createtunnel_list()
except ApiException as e:
    print("Exception when calling ConnectApi->createtunnel_list: %s\n" % e)
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

# **createtunnel_partial_update**
> createtunnel_partial_update(id, data=data)

update fields on a tunnel

update fields on a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 
data = swagger_client.Data20() # Data20 |  (optional)

try: 
    # update fields on a tunnel
    api_instance.createtunnel_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->createtunnel_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data20**](Data20.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createtunnel_read**
> createtunnel_read(id)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 

try: 
    api_instance.createtunnel_read(id)
except ApiException as e:
    print("Exception when calling ConnectApi->createtunnel_read: %s\n" % e)
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

# **createtunnel_update**
> createtunnel_update(id, data=data)

update a tunnel

update a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 
data = swagger_client.Data19() # Data19 |  (optional)

try: 
    # update a tunnel
    api_instance.createtunnel_update(id, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->createtunnel_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data19**](Data19.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_create**
> gateway_create(data=data)

create a gateway

create a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
data = swagger_client.Data21() # Data21 |  (optional)

try: 
    # create a gateway
    api_instance.gateway_create(data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->gateway_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data21**](Data21.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_delete**
> gateway_delete(hostname)

delete a gateway

delete a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 

try: 
    # delete a gateway
    api_instance.gateway_delete(hostname)
except ApiException as e:
    print("Exception when calling ConnectApi->gateway_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_list**
> gateway_list()

list all gateways

list all gateways

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()

try: 
    # list all gateways
    api_instance.gateway_list()
except ApiException as e:
    print("Exception when calling ConnectApi->gateway_list: %s\n" % e)
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

# **gateway_partial_update**
> gateway_partial_update(hostname, data=data)

update fields on a gateway

update fields on a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 
data = swagger_client.Data23() # Data23 |  (optional)

try: 
    # update fields on a gateway
    api_instance.gateway_partial_update(hostname, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->gateway_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 
 **data** | [**Data23**](Data23.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_read**
> gateway_read(hostname)

get a gateway

get a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 

try: 
    # get a gateway
    api_instance.gateway_read(hostname)
except ApiException as e:
    print("Exception when calling ConnectApi->gateway_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_update**
> gateway_update(hostname, data=data)

update a Gateway

update a Gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 
data = swagger_client.Data22() # Data22 |  (optional)

try: 
    # update a Gateway
    api_instance.gateway_update(hostname, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->gateway_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 
 **data** | [**Data22**](Data22.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways_create**
> gateways_create(data=data)

create a gateway

create a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
data = swagger_client.Data24() # Data24 |  (optional)

try: 
    # create a gateway
    api_instance.gateways_create(data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->gateways_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data24**](Data24.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways_delete**
> gateways_delete(hostname)

delete a gateway

delete a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 

try: 
    # delete a gateway
    api_instance.gateways_delete(hostname)
except ApiException as e:
    print("Exception when calling ConnectApi->gateways_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways_list**
> gateways_list()

list all gateways

list all gateways

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()

try: 
    # list all gateways
    api_instance.gateways_list()
except ApiException as e:
    print("Exception when calling ConnectApi->gateways_list: %s\n" % e)
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

# **gateways_partial_update**
> gateways_partial_update(hostname, data=data)

update fields on a gateway

update fields on a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 
data = swagger_client.Data26() # Data26 |  (optional)

try: 
    # update fields on a gateway
    api_instance.gateways_partial_update(hostname, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->gateways_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 
 **data** | [**Data26**](Data26.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways_read**
> gateways_read(hostname)

get a gateway

get a gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 

try: 
    # get a gateway
    api_instance.gateways_read(hostname)
except ApiException as e:
    print("Exception when calling ConnectApi->gateways_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateways_update**
> gateways_update(hostname, data=data)

update a Gateway

update a Gateway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
hostname = 'hostname_example' # str | 
data = swagger_client.Data25() # Data25 |  (optional)

try: 
    # update a Gateway
    api_instance.gateways_update(hostname, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->gateways_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 
 **data** | [**Data25**](Data25.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_create**
> tunnel_create(data=data)

create a tunnel

create a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
data = swagger_client.Data27() # Data27 |  (optional)

try: 
    # create a tunnel
    api_instance.tunnel_create(data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnel_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data27**](Data27.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_delete**
> tunnel_delete(id)

delete a tunnel

delete a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 

try: 
    # delete a tunnel
    api_instance.tunnel_delete(id)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnel_delete: %s\n" % e)
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

# **tunnel_list**
> tunnel_list(processed=processed)

list all tunnels

list all tunnels

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
processed = 'processed_example' # str |  (optional)

try: 
    # list all tunnels
    api_instance.tunnel_list(processed=processed)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnel_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_partial_update**
> tunnel_partial_update(id, data=data)

update fields on a tunnel

update fields on a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 
data = swagger_client.Data29() # Data29 |  (optional)

try: 
    # update fields on a tunnel
    api_instance.tunnel_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnel_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data29**](Data29.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_read**
> tunnel_read(id)

get a tunnel

get a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 

try: 
    # get a tunnel
    api_instance.tunnel_read(id)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnel_read: %s\n" % e)
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

# **tunnel_update**
> tunnel_update(id, data=data)

update a tunnel

update a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 
data = swagger_client.Data28() # Data28 |  (optional)

try: 
    # update a tunnel
    api_instance.tunnel_update(id, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnel_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data28**](Data28.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnels_create**
> tunnels_create(data=data)

create a tunnel

create a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
data = swagger_client.Data30() # Data30 |  (optional)

try: 
    # create a tunnel
    api_instance.tunnels_create(data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnels_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data30**](Data30.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnels_delete**
> tunnels_delete(id)

delete a tunnel

delete a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 

try: 
    # delete a tunnel
    api_instance.tunnels_delete(id)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnels_delete: %s\n" % e)
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

# **tunnels_list**
> tunnels_list(processed=processed)

list all tunnels

list all tunnels

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
processed = 'processed_example' # str |  (optional)

try: 
    # list all tunnels
    api_instance.tunnels_list(processed=processed)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnels_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processed** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnels_partial_update**
> tunnels_partial_update(id, data=data)

update fields on a tunnel

update fields on a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 
data = swagger_client.Data32() # Data32 |  (optional)

try: 
    # update fields on a tunnel
    api_instance.tunnels_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnels_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data32**](Data32.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnels_read**
> tunnels_read(id)

get a tunnel

get a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 

try: 
    # get a tunnel
    api_instance.tunnels_read(id)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnels_read: %s\n" % e)
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

# **tunnels_update**
> tunnels_update(id, data=data)

update a tunnel

update a tunnel

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
id = 'id_example' # str | 
data = swagger_client.Data31() # Data31 |  (optional)

try: 
    # update a tunnel
    api_instance.tunnels_update(id, data=data)
except ApiException as e:
    print("Exception when calling ConnectApi->tunnels_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Data31**](Data31.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

