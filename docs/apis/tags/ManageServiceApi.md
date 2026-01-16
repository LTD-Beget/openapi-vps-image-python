<a name="__pageTop"></a>
# beget_openapi_vps-image.apis.tags.manage_service_api.ManageServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manage_service_create_image**](#manage_service_create_image) | **post** /v1/image | 
[**manage_service_delete_image**](#manage_service_delete_image) | **delete** /v1/image/{id} | 
[**manage_service_get_calculation**](#manage_service_get_calculation) | **get** /v1/image/calculation | 
[**manage_service_get_download_link**](#manage_service_get_download_link) | **get** /v1/image/{id}/link | 
[**manage_service_get_list**](#manage_service_get_list) | **get** /v1/image | 
[**manage_service_get_region_list**](#manage_service_get_region_list) | **get** /v1/image/region | 
[**manage_service_restore_image**](#manage_service_restore_image) | **post** /v1/image/{id}/restore | 
[**manage_service_update_image**](#manage_service_update_image) | **put** /v1/image/{id} | 

# **manage_service_create_image**
<a name="manage_service_create_image"></a>
> ImageCreateImageResponse manage_service_create_image(image_create_image_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_create_image_response import ImageCreateImageResponse
from beget_openapi_vps-image.model.image_create_image_request import ImageCreateImageRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only required values which don't have defaults set
    body = ImageCreateImageRequest(
        source=ImageImageSource(
            link=ImageImageSourceLinkSource(
                link="link_example",
            ),
            vps=ImageImageSourceVpsSource(
                id="id_example",
                stop=True,
            ),
        ),
        name="name_example",
        region="region_example",
    )
    try:
        api_response = api_instance.manage_service_create_image(
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_create_image: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageCreateImageRequest**](../../models/ImageCreateImageRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_create_image.ApiResponseFor200) | OK

#### manage_service_create_image.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageCreateImageResponse**](../../models/ImageCreateImageResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_delete_image**
<a name="manage_service_delete_image"></a>
> ImageDeleteImageResponse manage_service_delete_image(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_delete_image_response import ImageDeleteImageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.manage_service_delete_image(
            path_params=path_params,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_delete_image: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_delete_image.ApiResponseFor200) | OK

#### manage_service_delete_image.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageDeleteImageResponse**](../../models/ImageDeleteImageResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_get_calculation**
<a name="manage_service_get_calculation"></a>
> ImageGetCalculationResponse manage_service_get_calculation()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_get_calculation_response import ImageGetCalculationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'file_size': "file_size_example",
        'link': "link_example",
        'vps_id': "vps_id_example",
    }
    try:
        api_response = api_instance.manage_service_get_calculation(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_calculation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_size | FileSizeSchema | | optional
link | LinkSchema | | optional
vps_id | VpsIdSchema | | optional


# FileSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VpsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_get_calculation.ApiResponseFor200) | OK

#### manage_service_get_calculation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageGetCalculationResponse**](../../models/ImageGetCalculationResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_get_download_link**
<a name="manage_service_get_download_link"></a>
> ImageGetDownloadLinkResponse manage_service_get_download_link(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_get_download_link_response import ImageGetDownloadLinkResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.manage_service_get_download_link(
            path_params=path_params,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_download_link: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_get_download_link.ApiResponseFor200) | OK

#### manage_service_get_download_link.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageGetDownloadLinkResponse**](../../models/ImageGetDownloadLinkResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_get_list**
<a name="manage_service_get_list"></a>
> ImageGetListResponse manage_service_get_list()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_get_list_response import ImageGetListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 1,
        'limit': 1,
        'filter': "filter_example",
        'sort': "sort_example",
    }
    try:
        api_response = api_instance.manage_service_get_list(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional
sort | SortSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_get_list.ApiResponseFor200) | OK

#### manage_service_get_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageGetListResponse**](../../models/ImageGetListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_get_region_list**
<a name="manage_service_get_region_list"></a>
> ImageGetRegionListResponse manage_service_get_region_list()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_get_region_list_response import ImageGetRegionListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.manage_service_get_region_list()
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_region_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_get_region_list.ApiResponseFor200) | OK

#### manage_service_get_region_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageGetRegionListResponse**](../../models/ImageGetRegionListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_restore_image**
<a name="manage_service_restore_image"></a>
> ImageRestoreImageResponse manage_service_restore_image(idimage_restore_image_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_restore_image_request import ImageRestoreImageRequest
from beget_openapi_vps-image.model.image_restore_image_response import ImageRestoreImageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = ImageRestoreImageRequest(
        id="id_example",
        vps_id="vps_id_example",
    )
    try:
        api_response = api_instance.manage_service_restore_image(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_restore_image: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageRestoreImageRequest**](../../models/ImageRestoreImageRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_restore_image.ApiResponseFor200) | OK

#### manage_service_restore_image.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageRestoreImageResponse**](../../models/ImageRestoreImageResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **manage_service_update_image**
<a name="manage_service_update_image"></a>
> ImageUpdateImageResponse manage_service_update_image(idimage_update_image_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps-image
from beget_openapi_vps-image.apis.tags import manage_service_api
from beget_openapi_vps-image.model.image_update_image_response import ImageUpdateImageResponse
from beget_openapi_vps-image.model.image_update_image_request import ImageUpdateImageRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps-image.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps-image.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps-image.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = ImageUpdateImageRequest(
        id="id_example",
        name="name_example",
        region="region_example",
    )
    try:
        api_response = api_instance.manage_service_update_image(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps-image.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_update_image: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageUpdateImageRequest**](../../models/ImageUpdateImageRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#manage_service_update_image.ApiResponseFor200) | OK

#### manage_service_update_image.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImageUpdateImageResponse**](../../models/ImageUpdateImageResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

