import typing_extensions

from beget_openapi_vps-image.paths import PathValues
from beget_openapi_vps-image.apis.paths.v1_image import V1Image
from beget_openapi_vps-image.apis.paths.v1_image_calculation import V1ImageCalculation
from beget_openapi_vps-image.apis.paths.v1_image_region import V1ImageRegion
from beget_openapi_vps-image.apis.paths.v1_image_id import V1ImageId
from beget_openapi_vps-image.apis.paths.v1_image_id_link import V1ImageIdLink
from beget_openapi_vps-image.apis.paths.v1_image_id_restore import V1ImageIdRestore

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_IMAGE: V1Image,
        PathValues.V1_IMAGE_CALCULATION: V1ImageCalculation,
        PathValues.V1_IMAGE_REGION: V1ImageRegion,
        PathValues.V1_IMAGE_ID: V1ImageId,
        PathValues.V1_IMAGE_ID_LINK: V1ImageIdLink,
        PathValues.V1_IMAGE_ID_RESTORE: V1ImageIdRestore,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_IMAGE: V1Image,
        PathValues.V1_IMAGE_CALCULATION: V1ImageCalculation,
        PathValues.V1_IMAGE_REGION: V1ImageRegion,
        PathValues.V1_IMAGE_ID: V1ImageId,
        PathValues.V1_IMAGE_ID_LINK: V1ImageIdLink,
        PathValues.V1_IMAGE_ID_RESTORE: V1ImageIdRestore,
    }
)
