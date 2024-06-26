from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ChannelTopic(BaseModel):
    model_config = ConfigDict(extra="allow")

    value: str
    creator: str
    last_set: int


class Channel(BaseModel):
    model_config = ConfigDict(extra="allow")

    created: int
    id: str
    is_archived: bool
    is_channel: bool
    is_general: bool
    is_group: bool
    is_member: bool
    is_mpim: bool
    is_org_shared: bool
    is_pending_ext_shared: bool
    is_private: bool
    is_shared: bool
    name: str
    name_normalized: str
    num_members: int
    purpose: ChannelTopic
    topic: ChannelTopic
    unlinked: int


class Message(BaseModel):
    model_config = ConfigDict(extra="allow")

    client_msg_id: str
    text: str
    ts: str
    type: str
    user: str


class ResponseMetadata(BaseModel):
    next_cursor: str | None
