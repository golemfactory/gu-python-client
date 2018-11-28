# gu-python-client
API description in Markdown.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/prekucki/gu-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/prekucki/gu-python-client.git`)

Then import the package:
```python
import gu_rest_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gu_rest_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 'session_id_example' # str | 
request_body = NULL # list[str] | 

try:
    # Manually adds peers to hub session
    api_response = api_instance.add_hub_session_peers(session_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->add_hub_session_peers: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:61622*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HubSessionApi* | [**add_hub_session_peers**](docs/HubSessionApi.md#add_hub_session_peers) | **POST** /sessions/{sessionId}/peer | Manually adds peers to hub session
*HubSessionApi* | [**create_hub_session**](docs/HubSessionApi.md#create_hub_session) | **POST** /sessions | 
*HubSessionApi* | [**get_hub_session**](docs/HubSessionApi.md#get_hub_session) | **GET** /sessions/{sessionId} | Gets hub session info
*HubSessionApi* | [**get_hub_session_config**](docs/HubSessionApi.md#get_hub_session_config) | **GET** /sessions/{sessionId}/config | Gets configuration from stash
*HubSessionApi* | [**list_hub_sessions**](docs/HubSessionApi.md#list_hub_sessions) | **GET** /sessions | Lists current hub sessions.
*HubSessionApi* | [**sessions_session_id_delete**](docs/HubSessionApi.md#sessions_session_id_delete) | **DELETE** /sessions/{sessionId} | 
*HubSessionApi* | [**sessions_session_id_patch**](docs/HubSessionApi.md#sessions_session_id_patch) | **PATCH** /sessions/{sessionId} | Hub session update
*HubSessionApi* | [**set_hub_session_configuration**](docs/HubSessionApi.md#set_hub_session_configuration) | **PUT** /sessions/{sessionId}/config | Sets configuration stash
*LobManApi* | [**create_blob**](docs/LobManApi.md#create_blob) | **POST** /sessions/{sessionId}/blob | Creates new lob
*LobManApi* | [**download_blob**](docs/LobManApi.md#download_blob) | **GET** /sessions/{sessionId}/blob/{blobId} | 
*LobManApi* | [**list_hub_session_blobs**](docs/LobManApi.md#list_hub_session_blobs) | **GET** /sessions/{sessionId}/blob | Lists currently allocated lobs
*LobManApi* | [**upload_blob**](docs/LobManApi.md#upload_blob) | **PUT** /sessions/{sessionId}/blob/{blobId} | 
*PeerInfoApi* | [**get_peer_details**](docs/PeerInfoApi.md#get_peer_details) | **GET** /peer/{nodeId} | Returns detailed peer info
*PeerInfoApi* | [**list_peers**](docs/PeerInfoApi.md#list_peers) | **GET** /peer | Returns a list hub peers.
*PeerSessionApi* | [**create_peer_session**](docs/PeerSessionApi.md#create_peer_session) | **POST** /sessions/{sessionId}/peer/{nodeId}/peer-sessions | 
*PeerSessionApi* | [**delete_peer_session**](docs/PeerSessionApi.md#delete_peer_session) | **DELETE** /sessions/{sessionId}/peer/{nodeId}/peer-sessions/{hubSession} | 
*PeerSessionApi* | [**update_peer_session**](docs/PeerSessionApi.md#update_peer_session) | **PATCH** /sessions/{sessionId}/peer/{nodeId}/peer-sessions/{hubSession} | Sends multiple commands for peer


## Documentation For Models

 - [BlobInfo](docs/BlobInfo.md)
 - [Command](docs/Command.md)
 - [ConfigStash](docs/ConfigStash.md)
 - [DownloadFileCommand](docs/DownloadFileCommand.md)
 - [EnvType](docs/EnvType.md)
 - [ExecCommand](docs/ExecCommand.md)
 - [HubSession](docs/HubSession.md)
 - [HubSessionCommand](docs/HubSessionCommand.md)
 - [HubSessionTouchCommand](docs/HubSessionTouchCommand.md)
 - [PeerInfo](docs/PeerInfo.md)
 - [PeerSessionSpec](docs/PeerSessionSpec.md)
 - [PeerSessionSpecImage](docs/PeerSessionSpecImage.md)
 - [StartCommand](docs/StartCommand.md)
 - [StopCommand](docs/StopCommand.md)
 - [UploadFileCommand](docs/UploadFileCommand.md)


## Documentation For Authorization


## serviceToken

- **Type**: API key
- **API key parameter name**: X-GU-APIKEY
- **Location**: HTTP header

## systemName

- **Type**: API key
- **API key parameter name**: X-GU-APPNAME
- **Location**: HTTP header


## Author




