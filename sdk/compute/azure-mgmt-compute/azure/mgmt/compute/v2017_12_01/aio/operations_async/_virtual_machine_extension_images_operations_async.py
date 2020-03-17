# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class VirtualMachineExtensionImagesOperations:
    """VirtualMachineExtensionImagesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2017_12_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        location: str,
        publisher_name: str,
        type: str,
        version: str,
        **kwargs
    ) -> "models.VirtualMachineExtensionImage":
        """Gets a virtual machine extension image.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name:
        :type publisher_name: str
        :param type:
        :type type: str
        :param version:
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineExtensionImage or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineExtensionImage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VirtualMachineExtensionImage"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'publisherName': self._serialize.url("publisher_name", publisher_name, 'str'),
            'type': self._serialize.url("type", type, 'str'),
            'version': self._serialize.url("version", version, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VirtualMachineExtensionImage', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions/{version}'}

    async def list_types(
        self,
        location: str,
        publisher_name: str,
        **kwargs
    ) -> List["VirtualMachineExtensionImage"]:
        """Gets a list of virtual machine extension image types.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name:
        :type publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2017_12_01.models.VirtualMachineExtensionImage]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["VirtualMachineExtensionImage"]]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"

        # Construct URL
        url = self.list_types.metadata['url']
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'publisherName': self._serialize.url("publisher_name", publisher_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[VirtualMachineExtensionImage]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_types.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types'}

    async def list_versions(
        self,
        location: str,
        publisher_name: str,
        type: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs
    ) -> List["VirtualMachineExtensionImage"]:
        """Gets a list of virtual machine extension image versions.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name:
        :type publisher_name: str
        :param type:
        :type type: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :param top:
        :type top: int
        :param orderby:
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2017_12_01.models.VirtualMachineExtensionImage]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["VirtualMachineExtensionImage"]]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"

        # Construct URL
        url = self.list_versions.metadata['url']
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'publisherName': self._serialize.url("publisher_name", publisher_name, 'str'),
            'type': self._serialize.url("type", type, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query("orderby", orderby, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[VirtualMachineExtensionImage]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_versions.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions'}
