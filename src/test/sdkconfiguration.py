"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass


SERVERS = [
    'https://hacker-news.firebaseio.com/v0',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '1.3.1'
    gen_version: str = '2.61.5'

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
