"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CreateOrganizationPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization, accessible only from the Backend API"""
    
    

class CreateOrganizationPrivateMetadata(BaseModel):
    r"""Metadata saved on the organization, accessible only from the Backend API"""
    
    

class CreateOrganizationPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API"""
    
    

class CreateOrganizationPublicMetadata(BaseModel):
    r"""Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API"""
    
    

class CreateOrganizationRequestBodyTypedDict(TypedDict):
    name: str
    r"""The name of the new organization"""
    created_by: str
    r"""The ID of the User who will become the administrator for the new organization"""
    private_metadata: NotRequired[CreateOrganizationPrivateMetadataTypedDict]
    r"""Metadata saved on the organization, accessible only from the Backend API"""
    public_metadata: NotRequired[CreateOrganizationPublicMetadataTypedDict]
    r"""Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API"""
    slug: NotRequired[str]
    r"""A slug for the new organization.
    Can contain only lowercase alphanumeric characters and the dash \"-\".
    Must be unique for the instance.
    """
    max_allowed_memberships: NotRequired[int]
    r"""The maximum number of memberships allowed for this organization"""
    

class CreateOrganizationRequestBody(BaseModel):
    name: str
    r"""The name of the new organization"""
    created_by: str
    r"""The ID of the User who will become the administrator for the new organization"""
    private_metadata: Optional[CreateOrganizationPrivateMetadata] = None
    r"""Metadata saved on the organization, accessible only from the Backend API"""
    public_metadata: Optional[CreateOrganizationPublicMetadata] = None
    r"""Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API"""
    slug: Optional[str] = None
    r"""A slug for the new organization.
    Can contain only lowercase alphanumeric characters and the dash \"-\".
    Must be unique for the instance.
    """
    max_allowed_memberships: Optional[int] = None
    r"""The maximum number of memberships allowed for this organization"""
    