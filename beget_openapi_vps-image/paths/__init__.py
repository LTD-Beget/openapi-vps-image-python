# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_vps-image.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_IMAGE = "/v1/image"
    V1_IMAGE_CALCULATION = "/v1/image/calculation"
    V1_IMAGE_REGION = "/v1/image/region"
    V1_IMAGE_ID = "/v1/image/{id}"
    V1_IMAGE_ID_LINK = "/v1/image/{id}/link"
    V1_IMAGE_ID_RESTORE = "/v1/image/{id}/restore"
