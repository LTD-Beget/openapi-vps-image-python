import typing_extensions

from beget_openapi_vps-image.apis.tags import TagValues
from beget_openapi_vps-image.apis.tags.manage_service_api import ManageServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.MANAGE_SERVICE: ManageServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.MANAGE_SERVICE: ManageServiceApi,
    }
)
