"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class RevokeSessionRequestTypedDict(TypedDict):
    session_id: str
    r"""The ID of the session"""


class RevokeSessionRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the session"""
