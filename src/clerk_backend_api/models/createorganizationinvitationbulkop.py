"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateOrganizationInvitationBulkPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""


class CreateOrganizationInvitationBulkPublicMetadata(BaseModel):
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""


class CreateOrganizationInvitationBulkPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""


class CreateOrganizationInvitationBulkPrivateMetadata(BaseModel):
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""


class RequestBodyTypedDict(TypedDict):
    email_address: str
    r"""The email address of the new member that is going to be invited to the organization"""
    role: str
    r"""The role of the new member in the organization."""
    inviter_user_id: NotRequired[Nullable[str]]
    r"""The ID of the user that invites the new member to the organization.
    Must be an administrator in the organization.
    """
    public_metadata: NotRequired[
        CreateOrganizationInvitationBulkPublicMetadataTypedDict
    ]
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""
    private_metadata: NotRequired[
        CreateOrganizationInvitationBulkPrivateMetadataTypedDict
    ]
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""
    redirect_url: NotRequired[str]
    r"""Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email."""


class RequestBody(BaseModel):
    email_address: str
    r"""The email address of the new member that is going to be invited to the organization"""

    role: str
    r"""The role of the new member in the organization."""

    inviter_user_id: OptionalNullable[str] = UNSET
    r"""The ID of the user that invites the new member to the organization.
    Must be an administrator in the organization.
    """

    public_metadata: Optional[CreateOrganizationInvitationBulkPublicMetadata] = None
    r"""Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API."""

    private_metadata: Optional[CreateOrganizationInvitationBulkPrivateMetadata] = None
    r"""Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API."""

    redirect_url: Optional[str] = None
    r"""Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "inviter_user_id",
            "public_metadata",
            "private_metadata",
            "redirect_url",
        ]
        nullable_fields = ["inviter_user_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class CreateOrganizationInvitationBulkRequestTypedDict(TypedDict):
    organization_id: str
    r"""The organization ID."""
    request_body: List[RequestBodyTypedDict]


class CreateOrganizationInvitationBulkRequest(BaseModel):
    organization_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The organization ID."""

    request_body: Annotated[
        List[RequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
