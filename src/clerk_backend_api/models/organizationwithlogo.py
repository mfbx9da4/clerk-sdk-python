"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class OrganizationWithLogoObject(str, Enum):
    ORGANIZATION = "organization"


class OrganizationWithLogoPublicMetadataTypedDict(TypedDict):
    pass
    

class OrganizationWithLogoPublicMetadata(BaseModel):
    pass
    

class OrganizationWithLogoPrivateMetadataTypedDict(TypedDict):
    pass
    

class OrganizationWithLogoPrivateMetadata(BaseModel):
    pass
    

class OrganizationWithLogoTypedDict(TypedDict):
    object: OrganizationWithLogoObject
    id: str
    name: str
    slug: str
    max_allowed_memberships: int
    public_metadata: OrganizationWithLogoPublicMetadataTypedDict
    private_metadata: OrganizationWithLogoPrivateMetadataTypedDict
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    image_url: str
    members_count: NotRequired[Nullable[int]]
    admin_delete_enabled: NotRequired[bool]
    created_by: NotRequired[str]
    logo_url: NotRequired[str]
    has_image: NotRequired[bool]
    

class OrganizationWithLogo(BaseModel):
    object: OrganizationWithLogoObject
    id: str
    name: str
    slug: str
    max_allowed_memberships: int
    public_metadata: OrganizationWithLogoPublicMetadata
    private_metadata: OrganizationWithLogoPrivateMetadata
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    image_url: str
    members_count: Optional[Nullable[int]] = None
    admin_delete_enabled: Optional[bool] = None
    created_by: Optional[str] = None
    logo_url: Annotated[Optional[str], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.")] = None
    has_image: Optional[bool] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["members_count", "admin_delete_enabled", "created_by", "logo_url", "has_image"]
        nullable_fields = ["members_count"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        