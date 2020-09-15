# gu_rest_api.PeerApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment**](PeerApi.md#create_deployment) | **POST** /peers/{nodeId}/deployments | 
[**drop_deployment**](PeerApi.md#drop_deployment) | **DELETE** /peers/{nodeId}/deployments/{deploymentId} | Removes deployment
[**get_hub_info**](PeerApi.md#get_hub_info) | **GET** /info | 
[**get_peer_details**](PeerApi.md#get_peer_details) | **GET** /peers/{nodeId} | Returns detailed peer info
[**list_deployments**](PeerApi.md#list_deployments) | **GET** /peers/{nodeId}/deployments | 
[**list_peers**](PeerApi.md#list_peers) | **GET** /peers | Returns a list hub peers.
[**update_deployment**](PeerApi.md#update_deployment) | **PATCH** /peers/{nodeId}/deployments/{deploymentId} | 


# **create_deployment**
> str create_deployment(node_id, spec)



### Example

* Api Key Authentication (serviceToken):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
spec = gu_rest_api.DeploymentSpec() # DeploymentSpec | 

try:
    api_response = api_instance.create_deployment(node_id, spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->create_deployment: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
spec = gu_rest_api.DeploymentSpec() # DeploymentSpec | 

try:
    api_response = api_instance.create_deployment(node_id, spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 
 **spec** | [**DeploymentSpec**](DeploymentSpec.md)|  | 

### Return type

**str**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drop_deployment**
> drop_deployment(node_id, deployment_id)

Removes deployment

### Example

* Api Key Authentication (serviceToken):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    # Removes deployment
    api_instance.drop_deployment(node_id, deployment_id)
except ApiException as e:
    print("Exception when calling PeerApi->drop_deployment: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    # Removes deployment
    api_instance.drop_deployment(node_id, deployment_id)
except ApiException as e:
    print("Exception when calling PeerApi->drop_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_info**
> HubInfo get_hub_info()



### Example

* Api Key Authentication (serviceToken):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))

try:
    api_response = api_instance.get_hub_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->get_hub_info: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))

try:
    api_response = api_instance.get_hub_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->get_hub_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HubInfo**](HubInfo.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_details**
> PeerDetails get_peer_details(node_id)

Returns detailed peer info

### Example

* Api Key Authentication (serviceToken):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier

try:
    # Returns detailed peer info
    api_response = api_instance.get_peer_details(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->get_peer_details: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier

try:
    # Returns detailed peer info
    api_response = api_instance.get_peer_details(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->get_peer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 

### Return type

[**PeerDetails**](PeerDetails.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> list[DeploymentInfo] list_deployments(node_id)



### Example

* Api Key Authentication (serviceToken):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier

try:
    api_response = api_instance.list_deployments(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->list_deployments: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier

try:
    api_response = api_instance.list_deployments(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->list_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 

### Return type

[**list[DeploymentInfo]**](DeploymentInfo.md)

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
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 50 # int |  (optional) (default to 50)

try:
    # Returns a list hub peers.
    api_response = api_instance.list_peers(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->list_peers: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 50 # int |  (optional) (default to 50)

try:
    # Returns a list hub peers.
    api_response = api_instance.list_peers(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->list_peers: %s\n" % e)
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

# **update_deployment**
> list[str] update_deployment(node_id, deployment_id, commands=commands)



### Example

* Api Key Authentication (serviceToken):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
commands = NULL # list[Command] |  (optional)

try:
    api_response = api_instance.update_deployment(node_id, deployment_id, commands=commands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->update_deployment: %s\n" % e)
```

* Api Key Authentication (systemName):
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
configuration = gu_rest_api.Configuration()
# Configure API key authorization: serviceToken
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'
configuration = gu_rest_api.Configuration()
# Configure API key authorization: systemName
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.PeerApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
commands = NULL # list[Command] |  (optional)

try:
    api_response = api_instance.update_deployment(node_id, deployment_id, commands=commands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerApi->update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 
 **commands** | [**list[Command]**](list.md)|  | [optional] 

### Return type

**list[str]**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

