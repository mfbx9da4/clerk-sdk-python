"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateOrganizationPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    
    

class UpdateOrganizationPublicMetadata(BaseModel):
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    
    

class UpdateOrganizationPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization that is only visible to your backend."""
    
    

class UpdateOrganizationPrivateMetadata(BaseModel):
    r"""Metadata saved on the organization that is only visible to your backend."""
    
    

class UpdateOrganizationRequestBodyTypedDict(TypedDict):
    public_metadata: NotRequired[UpdateOrganizationPublicMetadataTypedDict]
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    private_metadata: NotRequired[UpdateOrganizationPrivateMetadataTypedDict]
    r"""Metadata saved on the organization that is only visible to your backend."""
    name: NotRequired[Nullable[str]]
    r"""The new name of the organization.
    May not contain URLs or HTML.
    """
    slug: NotRequired[Nullable[str]]
    r"""The new slug of the organization, which needs to be unique in the instance"""
    max_allowed_memberships: NotRequired[Nullable[int]]
    r"""The maximum number of memberships allowed for this organization"""
    admin_delete_enabled: NotRequired[Nullable[bool]]
    r"""If true, an admin can delete this organization with the Frontend API."""
    created_at: NotRequired[str]
    r"""A custom date/time denoting _when_ the organization was created, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""
    

class UpdateOrganizationRequestBody(BaseModel):
    public_metadata: Optional[UpdateOrganizationPublicMetadata] = None
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    private_metadata: Optional[UpdateOrganizationPrivateMetadata] = None
    r"""Metadata saved on the organization that is only visible to your backend."""
    name: OptionalNullable[str] = UNSET
    r"""The new name of the organization.
    May not contain URLs or HTML.
    """
    slug: OptionalNullable[str] = UNSET
    r"""The new slug of the organization, which needs to be unique in the instance"""
    max_allowed_memberships: OptionalNullable[int] = UNSET
    r"""The maximum number of memberships allowed for this organization"""
    admin_delete_enabled: OptionalNullable[bool] = UNSET
    r"""If true, an admin can delete this organization with the Frontend API."""
    created_at: Optional[str] = None
    r"""A custom date/time denoting _when_ the organization was created, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["public_metadata", "private_metadata", "name", "slug", "max_allowed_memberships", "admin_delete_enabled", "created_at"]
        nullable_fields = ["name", "slug", "max_allowed_memberships", "admin_delete_enabled"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class UpdateOrganizationRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization to update"""
    request_body: UpdateOrganizationRequestBodyTypedDict
    

class UpdateOrganizationRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the organization to update"""
    request_body: Annotated[UpdateOrganizationRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
