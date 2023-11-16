"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import story as shared_story
from typing import Optional


@dataclasses.dataclass
class GetItemRequest:
    item_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'item_id', 'style': 'simple', 'explode': False }})
    r"""Numeric ID of the item to get"""
    



@dataclasses.dataclass
class GetItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    story: Optional[shared_story.Story] = dataclasses.field(default=None)
    r"""Successful operation"""
    

