# coding: utf-8

"""
    Golem unlimited low level hub API

    API description in Markdown.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gu_rest_api.api_client import ApiClient


class HubSessionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_hub_session_peers(self, session_id, request_body, **kwargs):  # noqa: E501
        """Manually adds peers to hub session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_hub_session_peers(session_id, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :param list[str] request_body: (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_hub_session_peers_with_http_info(session_id, request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_hub_session_peers_with_http_info(session_id, request_body, **kwargs)  # noqa: E501
            return data

    def add_hub_session_peers_with_http_info(self, session_id, request_body, **kwargs):  # noqa: E501
        """Manually adds peers to hub session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_hub_session_peers_with_http_info(session_id, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :param list[str] request_body: (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id', 'request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_hub_session_peers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `add_hub_session_peers`")  # noqa: E501
        # verify the required parameter 'request_body' is set
        if ('request_body' not in local_var_params or
                local_var_params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `add_hub_session_peers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['sessionId'] = local_var_params['session_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions/{sessionId}/peer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_hub_session(self, **kwargs):  # noqa: E501
        """create_hub_session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hub_session(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HubSession hub_session:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_hub_session_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_hub_session_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_hub_session_with_http_info(self, **kwargs):  # noqa: E501
        """create_hub_session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hub_session_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HubSession hub_session:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['hub_session']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hub_session" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hub_session' in local_var_params:
            body_params = local_var_params['hub_session']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hub_session(self, session_id, **kwargs):  # noqa: E501
        """Gets hub session info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hub_session(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :return: HubSession
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hub_session_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_hub_session_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def get_hub_session_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """Gets hub session info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hub_session_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :return: HubSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hub_session" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_hub_session`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['sessionId'] = local_var_params['session_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions/{sessionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HubSession',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hub_session_config(self, session_id, **kwargs):  # noqa: E501
        """Gets configuration from stash  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hub_session_config(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :return: ConfigStash
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hub_session_config_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_hub_session_config_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def get_hub_session_config_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """Gets configuration from stash  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hub_session_config_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :return: ConfigStash
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hub_session_config" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_hub_session_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['sessionId'] = local_var_params['session_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions/{sessionId}/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigStash',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_hub_sessions(self, **kwargs):  # noqa: E501
        """Lists current hub sessions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_hub_sessions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :return: list[HubSession]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_hub_sessions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_hub_sessions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_hub_sessions_with_http_info(self, **kwargs):  # noqa: E501
        """Lists current hub sessions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_hub_sessions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :return: list[HubSession]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_hub_sessions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[HubSession]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sessions_session_id_delete(self, session_id, **kwargs):  # noqa: E501
        """sessions_session_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sessions_session_id_delete(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sessions_session_id_delete_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sessions_session_id_delete_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def sessions_session_id_delete_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """sessions_session_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sessions_session_id_delete_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_session_id_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `sessions_session_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['sessionId'] = local_var_params['session_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions/{sessionId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sessions_session_id_patch(self, session_id, **kwargs):  # noqa: E501
        """Hub session update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sessions_session_id_patch(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :param HubSessionCommand hub_session_command:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sessions_session_id_patch_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sessions_session_id_patch_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def sessions_session_id_patch_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """Hub session update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sessions_session_id_patch_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :param HubSessionCommand hub_session_command:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id', 'hub_session_command']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_session_id_patch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `sessions_session_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['sessionId'] = local_var_params['session_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hub_session_command' in local_var_params:
            body_params = local_var_params['hub_session_command']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions/{sessionId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_hub_session_configuration(self, session_id, request_body, **kwargs):  # noqa: E501
        """Sets configuration stash  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_hub_session_configuration(session_id, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :param dict(str, object) request_body: New config stash value (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_hub_session_configuration_with_http_info(session_id, request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.set_hub_session_configuration_with_http_info(session_id, request_body, **kwargs)  # noqa: E501
            return data

    def set_hub_session_configuration_with_http_info(self, session_id, request_body, **kwargs):  # noqa: E501
        """Sets configuration stash  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_hub_session_configuration_with_http_info(session_id, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: (required)
        :param dict(str, object) request_body: New config stash value (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id', 'request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_hub_session_configuration" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `set_hub_session_configuration`")  # noqa: E501
        # verify the required parameter 'request_body' is set
        if ('request_body' not in local_var_params or
                local_var_params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `set_hub_session_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['sessionId'] = local_var_params['session_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/sessions/{sessionId}/config', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
