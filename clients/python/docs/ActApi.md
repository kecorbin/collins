# swagger_client.ActApi

All URIs are relative to *https://test.interthings.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environments_create**](ActApi.md#environments_create) | **POST** /api/v1/act/environments/ | 
[**environments_delete**](ActApi.md#environments_delete) | **DELETE** /api/v1/act/environments/{id}/ | 
[**environments_list**](ActApi.md#environments_list) | **GET** /api/v1/act/environments/ | 
[**environments_partial_update**](ActApi.md#environments_partial_update) | **PATCH** /api/v1/act/environments/{id}/ | 
[**environments_read**](ActApi.md#environments_read) | **GET** /api/v1/act/environments/{id}/ | 
[**environments_update**](ActApi.md#environments_update) | **PUT** /api/v1/act/environments/{id}/ | 
[**intervals_create**](ActApi.md#intervals_create) | **POST** /api/v1/act/intervals/ | create an interval schedule
[**intervals_delete**](ActApi.md#intervals_delete) | **DELETE** /api/v1/act/intervals/{id}/ | delete an interval schedule
[**intervals_list**](ActApi.md#intervals_list) | **GET** /api/v1/act/intervals/ | list interval schedules
[**intervals_partial_update**](ActApi.md#intervals_partial_update) | **PATCH** /api/v1/act/intervals/{id}/ | update fields on an interval schedule
[**intervals_read**](ActApi.md#intervals_read) | **GET** /api/v1/act/intervals/{id}/ | get a interval schedule
[**intervals_update**](ActApi.md#intervals_update) | **PUT** /api/v1/act/intervals/{id}/ | update an interval schedule
[**jobs_create**](ActApi.md#jobs_create) | **POST** /api/v1/act/jobs/ | create a job
[**jobs_delete**](ActApi.md#jobs_delete) | **DELETE** /api/v1/act/jobs/{id}/ | delete a job
[**jobs_list**](ActApi.md#jobs_list) | **GET** /api/v1/act/jobs/ | list all jobs
[**jobs_partial_update**](ActApi.md#jobs_partial_update) | **PATCH** /api/v1/act/jobs/{id}/ | update fields on a job
[**jobs_read**](ActApi.md#jobs_read) | **GET** /api/v1/act/jobs/{id}/ | get a job
[**jobs_update**](ActApi.md#jobs_update) | **PUT** /api/v1/act/jobs/{id}/ | update a job
[**plugins_create**](ActApi.md#plugins_create) | **POST** /api/v1/act/plugins/ | This is the API endpoint for working with Plugins.
[**plugins_delete**](ActApi.md#plugins_delete) | **DELETE** /api/v1/act/plugins/{id}/ | This is the API endpoint for working with Plugins.
[**plugins_list**](ActApi.md#plugins_list) | **GET** /api/v1/act/plugins/ | This is the API endpoint for working with Plugins.
[**plugins_partial_update**](ActApi.md#plugins_partial_update) | **PATCH** /api/v1/act/plugins/{id}/ | This is the API endpoint for working with Plugins.
[**plugins_read**](ActApi.md#plugins_read) | **GET** /api/v1/act/plugins/{id}/ | This is the API endpoint for working with Plugins.
[**plugins_update**](ActApi.md#plugins_update) | **PUT** /api/v1/act/plugins/{id}/ | This is the API endpoint for working with Plugins.
[**results_create**](ActApi.md#results_create) | **POST** /api/v1/act/results/ | This is the API endpoint for working with results.
[**results_delete**](ActApi.md#results_delete) | **DELETE** /api/v1/act/results/{id}/ | This is the API endpoint for working with results.
[**results_list**](ActApi.md#results_list) | **GET** /api/v1/act/results/ | This is the API endpoint for working with results.
[**results_partial_update**](ActApi.md#results_partial_update) | **PATCH** /api/v1/act/results/{id}/ | This is the API endpoint for working with results.
[**results_read**](ActApi.md#results_read) | **GET** /api/v1/act/results/{id}/ | This is the API endpoint for working with results.
[**results_update**](ActApi.md#results_update) | **PUT** /api/v1/act/results/{id}/ | This is the API endpoint for working with results.
[**schedulers_create**](ActApi.md#schedulers_create) | **POST** /api/v1/act/schedulers/ | This is the API endpoint for working with Schedulers.
[**schedulers_delete**](ActApi.md#schedulers_delete) | **DELETE** /api/v1/act/schedulers/{id}/ | This is the API endpoint for working with Schedulers.
[**schedulers_list**](ActApi.md#schedulers_list) | **GET** /api/v1/act/schedulers/ | This is the API endpoint for working with Schedulers.
[**schedulers_partial_update**](ActApi.md#schedulers_partial_update) | **PATCH** /api/v1/act/schedulers/{id}/ | This is the API endpoint for working with Schedulers.
[**schedulers_read**](ActApi.md#schedulers_read) | **GET** /api/v1/act/schedulers/{id}/ | This is the API endpoint for working with Schedulers.
[**schedulers_update**](ActApi.md#schedulers_update) | **PUT** /api/v1/act/schedulers/{id}/ | This is the API endpoint for working with Schedulers.


# **environments_create**
> environments_create(data=data)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
data = swagger_client.Data() # Data |  (optional)

try: 
    api_instance.environments_create(data=data)
except ApiException as e:
    print("Exception when calling ActApi->environments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environments_delete**
> environments_delete(id)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this environment.

try: 
    api_instance.environments_delete(id)
except ApiException as e:
    print("Exception when calling ActApi->environments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this environment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environments_list**
> environments_list()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()

try: 
    api_instance.environments_list()
except ApiException as e:
    print("Exception when calling ActApi->environments_list: %s\n" % e)
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

# **environments_partial_update**
> environments_partial_update(id, data=data)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this environment.
data = swagger_client.Data2() # Data2 |  (optional)

try: 
    api_instance.environments_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->environments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this environment. | 
 **data** | [**Data2**](Data2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environments_read**
> environments_read(id)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this environment.

try: 
    api_instance.environments_read(id)
except ApiException as e:
    print("Exception when calling ActApi->environments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this environment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environments_update**
> environments_update(id, data=data)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this environment.
data = swagger_client.Data1() # Data1 |  (optional)

try: 
    api_instance.environments_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->environments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this environment. | 
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intervals_create**
> intervals_create(data=data)

create an interval schedule

create an interval schedule

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
data = swagger_client.Data3() # Data3 |  (optional)

try: 
    # create an interval schedule
    api_instance.intervals_create(data=data)
except ApiException as e:
    print("Exception when calling ActApi->intervals_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data3**](Data3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intervals_delete**
> intervals_delete(id)

delete an interval schedule

delete an interval schedule

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this interval.

try: 
    # delete an interval schedule
    api_instance.intervals_delete(id)
except ApiException as e:
    print("Exception when calling ActApi->intervals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interval. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intervals_list**
> intervals_list()

list interval schedules

list interval schedules

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()

try: 
    # list interval schedules
    api_instance.intervals_list()
except ApiException as e:
    print("Exception when calling ActApi->intervals_list: %s\n" % e)
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

# **intervals_partial_update**
> intervals_partial_update(id, data=data)

update fields on an interval schedule

update fields on an interval schedule

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this interval.
data = swagger_client.Data5() # Data5 |  (optional)

try: 
    # update fields on an interval schedule
    api_instance.intervals_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->intervals_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interval. | 
 **data** | [**Data5**](Data5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intervals_read**
> intervals_read(id)

get a interval schedule

get a interval schedule

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this interval.

try: 
    # get a interval schedule
    api_instance.intervals_read(id)
except ApiException as e:
    print("Exception when calling ActApi->intervals_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interval. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intervals_update**
> intervals_update(id, data=data)

update an interval schedule

update an interval schedule

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this interval.
data = swagger_client.Data4() # Data4 |  (optional)

try: 
    # update an interval schedule
    api_instance.intervals_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->intervals_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interval. | 
 **data** | [**Data4**](Data4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_create**
> jobs_create(data=data)

create a job

create a job

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
data = swagger_client.Data6() # Data6 |  (optional)

try: 
    # create a job
    api_instance.jobs_create(data=data)
except ApiException as e:
    print("Exception when calling ActApi->jobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data6**](Data6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_delete**
> jobs_delete(id)

delete a job

delete a job

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this docker job.

try: 
    # delete a job
    api_instance.jobs_delete(id)
except ApiException as e:
    print("Exception when calling ActApi->jobs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this docker job. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_list**
> jobs_list()

list all jobs

list all jobs

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()

try: 
    # list all jobs
    api_instance.jobs_list()
except ApiException as e:
    print("Exception when calling ActApi->jobs_list: %s\n" % e)
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

# **jobs_partial_update**
> jobs_partial_update(id, data=data)

update fields on a job

update fields on a job

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this docker job.
data = swagger_client.Data8() # Data8 |  (optional)

try: 
    # update fields on a job
    api_instance.jobs_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->jobs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this docker job. | 
 **data** | [**Data8**](Data8.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_read**
> jobs_read(id)

get a job

get a job

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this docker job.

try: 
    # get a job
    api_instance.jobs_read(id)
except ApiException as e:
    print("Exception when calling ActApi->jobs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this docker job. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_update**
> jobs_update(id, data=data)

update a job

update a job

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this docker job.
data = swagger_client.Data7() # Data7 |  (optional)

try: 
    # update a job
    api_instance.jobs_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->jobs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this docker job. | 
 **data** | [**Data7**](Data7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_create**
> plugins_create(data=data)

This is the API endpoint for working with Plugins.

This is the API endpoint for working with Plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
data = swagger_client.Data9() # Data9 |  (optional)

try: 
    # This is the API endpoint for working with Plugins.
    api_instance.plugins_create(data=data)
except ApiException as e:
    print("Exception when calling ActApi->plugins_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data9**](Data9.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_delete**
> plugins_delete(id)

This is the API endpoint for working with Plugins.

This is the API endpoint for working with Plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this plugin.

try: 
    # This is the API endpoint for working with Plugins.
    api_instance.plugins_delete(id)
except ApiException as e:
    print("Exception when calling ActApi->plugins_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this plugin. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_list**
> plugins_list()

This is the API endpoint for working with Plugins.

This is the API endpoint for working with Plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()

try: 
    # This is the API endpoint for working with Plugins.
    api_instance.plugins_list()
except ApiException as e:
    print("Exception when calling ActApi->plugins_list: %s\n" % e)
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

# **plugins_partial_update**
> plugins_partial_update(id, data=data)

This is the API endpoint for working with Plugins.

This is the API endpoint for working with Plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this plugin.
data = swagger_client.Data11() # Data11 |  (optional)

try: 
    # This is the API endpoint for working with Plugins.
    api_instance.plugins_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->plugins_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this plugin. | 
 **data** | [**Data11**](Data11.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_read**
> plugins_read(id)

This is the API endpoint for working with Plugins.

This is the API endpoint for working with Plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this plugin.

try: 
    # This is the API endpoint for working with Plugins.
    api_instance.plugins_read(id)
except ApiException as e:
    print("Exception when calling ActApi->plugins_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this plugin. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_update**
> plugins_update(id, data=data)

This is the API endpoint for working with Plugins.

This is the API endpoint for working with Plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this plugin.
data = swagger_client.Data10() # Data10 |  (optional)

try: 
    # This is the API endpoint for working with Plugins.
    api_instance.plugins_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->plugins_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this plugin. | 
 **data** | [**Data10**](Data10.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_create**
> results_create(data=data)

This is the API endpoint for working with results.

This is the API endpoint for working with results.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
data = swagger_client.Data12() # Data12 |  (optional)

try: 
    # This is the API endpoint for working with results.
    api_instance.results_create(data=data)
except ApiException as e:
    print("Exception when calling ActApi->results_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data12**](Data12.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_delete**
> results_delete(id)

This is the API endpoint for working with results.

This is the API endpoint for working with results.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this result.

try: 
    # This is the API endpoint for working with results.
    api_instance.results_delete(id)
except ApiException as e:
    print("Exception when calling ActApi->results_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this result. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_list**
> results_list()

This is the API endpoint for working with results.

This is the API endpoint for working with results.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()

try: 
    # This is the API endpoint for working with results.
    api_instance.results_list()
except ApiException as e:
    print("Exception when calling ActApi->results_list: %s\n" % e)
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

# **results_partial_update**
> results_partial_update(id, data=data)

This is the API endpoint for working with results.

This is the API endpoint for working with results.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this result.
data = swagger_client.Data14() # Data14 |  (optional)

try: 
    # This is the API endpoint for working with results.
    api_instance.results_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->results_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this result. | 
 **data** | [**Data14**](Data14.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_read**
> results_read(id)

This is the API endpoint for working with results.

This is the API endpoint for working with results.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this result.

try: 
    # This is the API endpoint for working with results.
    api_instance.results_read(id)
except ApiException as e:
    print("Exception when calling ActApi->results_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this result. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_update**
> results_update(id, data=data)

This is the API endpoint for working with results.

This is the API endpoint for working with results.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this result.
data = swagger_client.Data13() # Data13 |  (optional)

try: 
    # This is the API endpoint for working with results.
    api_instance.results_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->results_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this result. | 
 **data** | [**Data13**](Data13.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedulers_create**
> schedulers_create(data=data)

This is the API endpoint for working with Schedulers.

This is the API endpoint for working with Schedulers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
data = swagger_client.Data15() # Data15 |  (optional)

try: 
    # This is the API endpoint for working with Schedulers.
    api_instance.schedulers_create(data=data)
except ApiException as e:
    print("Exception when calling ActApi->schedulers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data15**](Data15.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedulers_delete**
> schedulers_delete(id)

This is the API endpoint for working with Schedulers.

This is the API endpoint for working with Schedulers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this scheduler.

try: 
    # This is the API endpoint for working with Schedulers.
    api_instance.schedulers_delete(id)
except ApiException as e:
    print("Exception when calling ActApi->schedulers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scheduler. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedulers_list**
> schedulers_list()

This is the API endpoint for working with Schedulers.

This is the API endpoint for working with Schedulers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()

try: 
    # This is the API endpoint for working with Schedulers.
    api_instance.schedulers_list()
except ApiException as e:
    print("Exception when calling ActApi->schedulers_list: %s\n" % e)
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

# **schedulers_partial_update**
> schedulers_partial_update(id, data=data)

This is the API endpoint for working with Schedulers.

This is the API endpoint for working with Schedulers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this scheduler.
data = swagger_client.Data17() # Data17 |  (optional)

try: 
    # This is the API endpoint for working with Schedulers.
    api_instance.schedulers_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->schedulers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scheduler. | 
 **data** | [**Data17**](Data17.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedulers_read**
> schedulers_read(id)

This is the API endpoint for working with Schedulers.

This is the API endpoint for working with Schedulers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this scheduler.

try: 
    # This is the API endpoint for working with Schedulers.
    api_instance.schedulers_read(id)
except ApiException as e:
    print("Exception when calling ActApi->schedulers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scheduler. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedulers_update**
> schedulers_update(id, data=data)

This is the API endpoint for working with Schedulers.

This is the API endpoint for working with Schedulers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
id = 56 # int | A unique integer value identifying this scheduler.
data = swagger_client.Data16() # Data16 |  (optional)

try: 
    # This is the API endpoint for working with Schedulers.
    api_instance.schedulers_update(id, data=data)
except ApiException as e:
    print("Exception when calling ActApi->schedulers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scheduler. | 
 **data** | [**Data16**](Data16.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

