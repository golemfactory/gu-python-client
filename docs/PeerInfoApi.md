# gu_rest_api.PeerInfoApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_peer_details**](PeerInfoApi.md#get_peer_details) | **GET** /peer/{nodeId} | Returns detailed peer info
[**list_peers**](PeerInfoApi.md#list_peers) | **GET** /peer | Returns a list hub peers.


# **get_peer_details**
> PeerInfo get_peer_details(node_id)

Returns detailed peer info

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerInfoApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier

try:
    # Returns detailed peer info
    api_response = api_instance.get_peer_details(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerInfoApi->get_peer_details: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerInfoApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier

try:
    # Returns detailed peer info
    api_response = api_instance.get_peer_details(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerInfoApi->get_peer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 

### Return type

[**PeerInfo**](PeerInfo.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_peers**
> list[PeerInfo] list_peers(offset=offset, limit=limit)

Returns a list hub peers.

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerInfoApi(gu_rest_api.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 50 # int |  (optional) (default to 50)

try:
    # Returns a list hub peers.
    api_response = api_instance.list_peers(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerInfoApi->list_peers: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerInfoApi(gu_rest_api.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 50 # int |  (optional) (default to 50)

try:
    # Returns a list hub peers.
    api_response = api_instance.list_peers(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerInfoApi->list_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**list[PeerInfo]**](PeerInfo.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

