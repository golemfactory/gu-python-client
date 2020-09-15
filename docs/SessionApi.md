# gu_rest_api.SessionApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_session_peers**](SessionApi.md#add_session_peers) | **POST** /sessions/{sessionId}/peers | Manually adds peers to hub session
[**create_blob**](SessionApi.md#create_blob) | **POST** /sessions/{sessionId}/blobs | Creates new lob
[**create_deployment**](SessionApi.md#create_deployment) | **POST** /sessions/{sessionId}/peers/{nodeId}/deployments | Creates new deployment
[**create_session**](SessionApi.md#create_session) | **POST** /sessions | Creates new hub session.
[**delete_blob**](SessionApi.md#delete_blob) | **DELETE** /sessions/{sessionId}/blobs/{blobId} | 
[**delete_deployment**](SessionApi.md#delete_deployment) | **DELETE** /sessions/{sessionId}/peers/{nodeId}/deployments/{deploymentId} | 
[**delete_session**](SessionApi.md#delete_session) | **DELETE** /sessions/{sessionId} | 
[**download_blob**](SessionApi.md#download_blob) | **GET** /sessions/{sessionId}/blobs/{blobId} | Downloads binary content from the hub
[**get_config**](SessionApi.md#get_config) | **GET** /sessions/{sessionId}/config | Gets configuration from stash
[**get_hub_info**](SessionApi.md#get_hub_info) | **GET** /info | 
[**get_session**](SessionApi.md#get_session) | **GET** /sessions/{sessionId} | Gets hub session info
[**list_blobs**](SessionApi.md#list_blobs) | **GET** /sessions/{sessionId}/blobs | Lists currently allocated lobs
[**list_session_peers**](SessionApi.md#list_session_peers) | **GET** /sessions/{sessionId}/peers | List session peers
[**list_sessions**](SessionApi.md#list_sessions) | **GET** /sessions | Lists current hub sessions.
[**set_config**](SessionApi.md#set_config) | **PUT** /sessions/{sessionId}/config | Sets configuration stash
[**update_deployment**](SessionApi.md#update_deployment) | **PATCH** /sessions/{sessionId}/peers/{nodeId}/deployments/{deploymentId} | Sends multiple commands for peer
[**update_session**](SessionApi.md#update_session) | **PATCH** /sessions/{sessionId} | Hub session update
[**upload_blob**](SessionApi.md#upload_blob) | **PUT** /sessions/{sessionId}/blobs/{blobId} | Uploads a binary content to the hub.


# **add_session_peers**
> list[str] add_session_peers(session_id, peer_set)

Manually adds peers to hub session

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
peer_set = NULL # list[str] | 

try:
    # Manually adds peers to hub session
    api_response = api_instance.add_session_peers(session_id, peer_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->add_session_peers: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
peer_set = NULL # list[str] | 

try:
    # Manually adds peers to hub session
    api_response = api_instance.add_session_peers(session_id, peer_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->add_session_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **peer_set** | [**list[str]**](list.md)|  | 

### Return type

**list[str]**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blob**
> object create_blob(session_id, body=body)

Creates new lob

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
body = '/path/to/file' # file |  (optional)

try:
    # Creates new lob
    api_response = api_instance.create_blob(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_blob: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
body = '/path/to/file' # file |  (optional)

try:
    # Creates new lob
    api_response = api_instance.create_blob(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **body** | **file**|  | [optional] 

### Return type

**object**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment**
> str create_deployment(session_id, node_id, deployment_spec)

Creates new deployment

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_spec = gu_rest_api.DeploymentSpec() # DeploymentSpec | 

try:
    # Creates new deployment
    api_response = api_instance.create_deployment(session_id, node_id, deployment_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_deployment: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_spec = gu_rest_api.DeploymentSpec() # DeploymentSpec | 

try:
    # Creates new deployment
    api_response = api_instance.create_deployment(session_id, node_id, deployment_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **node_id** | **str**| GU Network node identifier | 
 **deployment_spec** | [**DeploymentSpec**](DeploymentSpec.md)|  | 

### Return type

**str**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> int create_session(body)

Creates new hub session.

Allowed fileds:  * name        - human readable session name * expires     - session expiration timestamp * allocation  - resource allocation mode.

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
body = gu_rest_api.HubSession() # HubSession | 

try:
    # Creates new hub session.
    api_response = api_instance.create_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_session: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
body = gu_rest_api.HubSession() # HubSession | 

try:
    # Creates new hub session.
    api_response = api_instance.create_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HubSession**](HubSession.md)|  | 

### Return type

**int**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blob**
> delete_blob(session_id, blob_id)



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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 56 # int | Blob identifier

try:
    api_instance.delete_blob(session_id, blob_id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_blob: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 56 # int | Blob identifier

try:
    api_instance.delete_blob(session_id, blob_id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **blob_id** | **int**| Blob identifier | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment**
> delete_deployment(session_id, node_id, deployment_id)



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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    api_instance.delete_deployment(session_id, node_id, deployment_id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_deployment: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    api_instance.delete_deployment(session_id, node_id, deployment_id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
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

# **delete_session**
> delete_session(session_id)



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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    api_instance.delete_session(session_id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_session: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    api_instance.delete_session(session_id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_blob**
> file download_blob(session_id, blob_id)

Downloads binary content from the hub

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 56 # int | Blob identifier

try:
    # Downloads binary content from the hub
    api_response = api_instance.download_blob(session_id, blob_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->download_blob: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 56 # int | Blob identifier

try:
    # Downloads binary content from the hub
    api_response = api_instance.download_blob(session_id, blob_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->download_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **blob_id** | **int**| Blob identifier | 

### Return type

**file**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> dict(str, object) get_config(session_id)

Gets configuration from stash

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets configuration from stash
    api_response = api_instance.get_config(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_config: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets configuration from stash
    api_response = api_instance.get_config(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

**dict(str, object)**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))

try:
    api_response = api_instance.get_hub_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_hub_info: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))

try:
    api_response = api_instance.get_hub_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_hub_info: %s\n" % e)
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

# **get_session**
> HubSession get_session(session_id)

Gets hub session info

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets hub session info
    api_response = api_instance.get_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_session: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets hub session info
    api_response = api_instance.get_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

[**HubSession**](HubSession.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blobs**
> list[BlobInfo] list_blobs(session_id)

Lists currently allocated lobs

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Lists currently allocated lobs
    api_response = api_instance.list_blobs(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_blobs: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Lists currently allocated lobs
    api_response = api_instance.list_blobs(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_blobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

[**list[BlobInfo]**](BlobInfo.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_session_peers**
> list[PeerInfo] list_session_peers(session_id)

List session peers

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # List session peers
    api_response = api_instance.list_session_peers(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_session_peers: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # List session peers
    api_response = api_instance.list_session_peers(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_session_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

[**list[PeerInfo]**](PeerInfo.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> list[HubSession] list_sessions(limit=limit, offset=offset)

Lists current hub sessions.

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
limit = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # Lists current hub sessions.
    api_response = api_instance.list_sessions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_sessions: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
limit = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # Lists current hub sessions.
    api_response = api_instance.list_sessions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**list[HubSession]**](HubSession.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_config**
> int set_config(session_id, config)

Sets configuration stash

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
config = NULL # dict(str, object) | New config stash value

try:
    # Sets configuration stash
    api_response = api_instance.set_config(session_id, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->set_config: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
config = NULL # dict(str, object) | New config stash value

try:
    # Sets configuration stash
    api_response = api_instance.set_config(session_id, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->set_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **config** | [**dict(str, object)**](object.md)| New config stash value | 

### Return type

**int**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment**
> update_deployment(session_id, node_id, deployment_id, commands)

Sends multiple commands for peer

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
commands = NULL # list[Command] | 

try:
    # Sends multiple commands for peer
    api_instance.update_deployment(session_id, node_id, deployment_id, commands)
except ApiException as e:
    print("Exception when calling SessionApi->update_deployment: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
commands = NULL # list[Command] | 

try:
    # Sends multiple commands for peer
    api_instance.update_deployment(session_id, node_id, deployment_id, commands)
except ApiException as e:
    print("Exception when calling SessionApi->update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 
 **commands** | [**list[Command]**](list.md)|  | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_session**
> update_session(session_id, changes=changes)

Hub session update

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
changes = gu_rest_api.HubSessionCommand() # HubSessionCommand |  (optional)

try:
    # Hub session update
    api_instance.update_session(session_id, changes=changes)
except ApiException as e:
    print("Exception when calling SessionApi->update_session: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
changes = gu_rest_api.HubSessionCommand() # HubSessionCommand |  (optional)

try:
    # Hub session update
    api_instance.update_session(session_id, changes=changes)
except ApiException as e:
    print("Exception when calling SessionApi->update_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **changes** | [**HubSessionCommand**](HubSessionCommand.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_blob**
> upload_blob(session_id, blob_id, body=body)

Uploads a binary content to the hub.

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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 56 # int | Blob identifier
body = '/path/to/file' # file |  (optional)

try:
    # Uploads a binary content to the hub.
    api_instance.upload_blob(session_id, blob_id, body=body)
except ApiException as e:
    print("Exception when calling SessionApi->upload_blob: %s\n" % e)
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
api_instance = gu_rest_api.SessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 56 # int | Blob identifier
body = '/path/to/file' # file |  (optional)

try:
    # Uploads a binary content to the hub.
    api_instance.upload_blob(session_id, blob_id, body=body)
except ApiException as e:
    print("Exception when calling SessionApi->upload_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **blob_id** | **int**| Blob identifier | 
 **body** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

