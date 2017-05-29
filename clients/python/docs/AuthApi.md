# swagger_client.AuthApi

All URIs are relative to *https://test.interthings.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AuthApi.md#create) | **POST** /api/v1/auth/ | 


# **create**
> create()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try: 
    api_instance.create()
except ApiException as e:
    print("Exception when calling AuthApi->create: %s\n" % e)
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

