#  vegagram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of vegagram.
#
#  vegagram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  vegagram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with vegagram.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from typing import Union, List, Optional, AsyncGenerator, BinaryIO

import vegagram
from vegagram import raw, enums
from vegagram import types
from vegagram import utils
from ..object import Object


class Chat(Object):
    """A chat.

    Parameters:
        id (``int``, *optional*):
            Unique identifier for this chat.

        type (:obj:`~vegagram.enums.ChatType`, *optional*):
            Type of chat.

        is_forum (``bool``, *optional*):
            True, if the supergroup chat is a forum.

        is_verified (``bool``, *optional*):
            True, if this chat has been verified by Telegram. Supergroups, channels and bots only.

        is_members_hidden (``bool``, *optional*):
            True, if the chat members are hidden.

        is_restricted (``bool``, *optional*):
            True, if this chat has been restricted. Supergroups, channels and bots only.
            See *restriction_reason* for details.

        is_creator (``bool``, *optional*):
            True, if this chat owner is the current user. Supergroups, channels and groups only.

        is_admin (``bool``, *optional*):
            True, if the current user is admin. Supergroups, channels and groups only.

        is_scam (``bool``, *optional*):
            True, if this chat has been flagged for scam.

        is_fake (``bool``, *optional*):
            True, if this chat has been flagged for impersonation.

        is_deactivated (``bool``, *optional*):
            True, if this chat has been flagged for deactivated.

        is_support (``bool``, *optional*):
            True, if this chat is part of the Telegram support team. Users and bots only.

        is_stories_hidden (``bool``, *optional*):
            True, if this chat has hidden stories.

        is_stories_unavailable (``bool``, *optional*):
            True, if this chat stories is unavailable.

        is_business_bot (``bool``, *optional*):
            True, if this bot can connect to business account.

        is_preview (``bool``, *optional*):
            True, if this chat is a preview.

        is_banned (``bool``, *optional*):
            True, if you are banned in this chat.

        is_call_active (``bool``, *optional*):
            True, if a group call is currently active.

        is_call_not_empty (``bool``, *optional*):
            True, if there's anyone in the group call.

        is_public (``bool``, *optional*):
            True, if this chat is public.

        is_paid_reactions_available (``bool``, *optional*):
            True, if paid reactions enabled in this chat.

        title (``str``, *optional*):
            Title, for supergroups, channels and basic group chats.

        username (``str``, *optional*):
            Username, for private chats, bots, supergroups and channels if available.

        usernames (List of :obj:`~vegagram.types.Username`, *optional*):
            The list of chat's collectible (and basic) usernames if available.

        first_name (``str``, *optional*):
            First name of the other party in a private chat, for private chats and bots.

        last_name (``str``, *optional*):
            Last name of the other party in a private chat, for private chats.

        photo (:obj:`~vegagram.types.ChatPhoto`, *optional*):
            Chat photo. Suitable for downloads only.

        stories (List of :obj:`~vegagram.types.Story`, *optional*):
            The list of chat's stories if available.

        wallpaper (:obj:`~vegagram.types.Document`, *optional*):
            Chat wallpaper.

        bio (``str``, *optional*):
            Bio of the other party in a private chat.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        description (``str``, *optional*):
            Description, for groups, supergroups and channel chats.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        dc_id (``int``, *optional*):
            The chat assigned DC (data center). Available only in case the chat has a photo.
            Note that this information is approximate; it is based on where Telegram stores the current chat photo.
            It is accurate only in case the owner has set the chat photo, otherwise the dc_id will be the one assigned
            to the administrator who set the current chat photo.

        folder_id (``int``, *optional*):
            The folder identifier where the chat is located.

        has_protected_content (``bool``, *optional*):
            True, if messages from the chat can't be forwarded to other chats.

        has_visible_history (``bool``, *optional*):
            True, if new chat members will have access to old messages; available only to chat administrators.

        has_aggressive_anti_spam_enabled (``bool``, *optional*):
            True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.

        invite_link (``str``, *optional*):
            Chat invite link, for groups, supergroups and channels.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        pinned_message (:obj:`~vegagram.types.Message`, *optional*):
            Pinned message, for groups, supergroups channels and own chat.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        sticker_set_name (``str``, *optional*):
            For supergroups, name of group sticker set.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        custom_emoji_sticker_set_name (``str``, *optional*):
            For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.

        can_set_sticker_set (``bool``, *optional*):
            True, if the group sticker set can be changed by you.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        can_send_paid_media (``bool``, *optional*):
            True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.

        members (List of :obj:`~vegagram.types.User`, *optional*):
            A few of the participants that are in the group.

        members_count (``int``, *optional*):
            Chat members count, for groups, supergroups and channels only.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        restrictions (List of :obj:`~vegagram.types.Restriction`, *optional*):
            The list of reasons why this chat might be unavailable to some users.
            This field is available only in case *is_restricted* is True.

        permissions (:obj:`~vegagram.types.ChatPermissions` *optional*):
            Default chat member permissions, for groups and supergroups.

        personal_channel (:obj:`~vegagram.types.Chat`, *optional*):
            The personal channel linked to this chat.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        personal_channel_message (:obj:`~vegagram.types.Message`, *optional*):
            The last message in the personal channel of this chat.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        linked_chat (:obj:`~vegagram.types.Chat`, *optional*):
            The linked discussion group (in case of channels) or the linked channel (in case of supergroups).
            Returned only in :meth:`~vegagram.Client.get_chat`.

        send_as_chat (:obj:`~vegagram.types.Chat`, *optional*):
            The default "send_as" chat.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        available_reactions (:obj:`~vegagram.types.ChatReactions`, *optional*):
            Available reactions in the chat.
            Returned only in :meth:`~vegagram.Client.get_chat`.

        level (``int``, *optional*):
            Channel boosts level.

        reply_color (:obj:`~vegagram.types.ChatColor`, *optional*):
            Chat reply color.

        profile_color (:obj:`~vegagram.types.ChatColor`, *optional*):
            Chat profile color.

        business_info (:obj:`~vegagram.types.BusinessInfo`, *optional*):
            Business information of a chat.

        business_intro (:obj:`~vegagram.types.BusinessIntro`, *optional*):
            For private chats with business accounts, the intro of the business.

        birthday (:obj:`~vegagram.types.Birthday`, *optional*):
            Information about user birthday.

        message_auto_delete_time (``int``, *optional*):
            The time after which all messages sent to the chat will be automatically deleted; in seconds.

        unrestrict_boost_count (``int``, *optional*):
            For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions.

        slow_mode_delay (``int``, *optional*):
            For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds.

        slowmode_next_send_date (:py:obj:`~datetime.datetime`, *optional*):
            Indicates when the user will be allowed to send another message in the chat. For supergroups only.

        join_by_request (``bool``, *optional*):
            True, if all users directly joining the supergroup need to be approved by supergroup administrators.

        join_requests_count (``int``, *optional*):
            Number of users who requested to join the chat.

        banned_until_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the user will be unbanned.

        subscription_until_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the the subscription will end.

        reactions_limit (``int``, *optional*):
            This flag may be used to impose a custom limit of unique reactions (i.e. a customizable version of appConfig.reactions_uniq_max).

        raw (:obj:`~vegagram.raw.base.Chat` | :obj:`~vegagram.raw.base.User` | :obj:`~vegagram.raw.base.ChatFull` | :obj:`~vegagram.raw.base.UserFull`, *optional*):
            The raw chat or user object, as received from the Telegram API.

        full_name (``str``, *property*):
            Full name of the other party in a private chat, for private chats and bots.
    """

    def __init__(
        self,
        *,
        client: "vegagram.Client" = None,
        id: int = None,
        type: "enums.ChatType" = None,
        is_forum: bool = None,
        is_verified: bool = None,
        is_members_hidden: bool = None,
        is_restricted: bool = None,
        is_creator: bool = None,
        is_admin: bool = None,
        is_scam: bool = None,
        is_fake: bool = None,
        is_deactivated: bool = None,
        is_support: bool = None,
        is_stories_hidden: bool = None,
        is_stories_unavailable: bool = None,
        is_business_bot: bool = None,
        is_preview: bool = None,
        is_banned: bool = None,
        is_call_active: bool = None,
        is_call_not_empty: bool = None,
        is_public: bool = None,
        is_paid_reactions_available: bool = None,
        title: str = None,
        username: str = None,
        usernames: List["types.Username"] = None,
        first_name: str = None,
        last_name: str = None,
        photo: "types.ChatPhoto" = None,
        stories: List["types.Story"] = None,
        wallpaper: "types.Document" = None,
        bio: str = None,
        description: str = None,
        dc_id: int = None,
        folder_id: int = None,
        has_protected_content: bool = None,
        has_visible_history: bool = None,
        has_aggressive_anti_spam_enabled: bool = None,
        invite_link: str = None,
        pinned_message=None,
        sticker_set_name: str = None,
        custom_emoji_sticker_set_name = None,
        can_set_sticker_set: bool = None,
        can_send_paid_media: bool = None,
        members: List["types.User"] = None,
        members_count: int = None,
        restrictions: List["types.Restriction"] = None,
        permissions: "types.ChatPermissions" = None,
        personal_channel: "types.Chat" = None,
        personal_channel_message: "types.Message" = None,
        linked_chat: "types.Chat" = None,
        send_as_chat: "types.Chat" = None,
        available_reactions: Optional["types.ChatReactions"] = None,
        level: int = None,
        reply_color: "types.ChatColor" = None,
        profile_color: "types.ChatColor" = None,
        business_info: "types.BusinessInfo" = None,
        business_intro: "types.BusinessIntro" = None,
        birthday: "types.Birthday" = None,
        message_auto_delete_time = None,
        unrestrict_boost_count = None,
        slow_mode_delay = None,
        slowmode_next_send_date: datetime = None,
        join_by_request: bool = None,
        join_requests_count: int = None,
        banned_until_date: datetime = None,
        subscription_until_date: datetime = None,
        reactions_limit: int = None,
        raw: Union["raw.base.Chat", "raw.base.User", "raw.base.ChatFull", "raw.base.UserFull"] = None
    ):
        super().__init__(client)

        self.id = id
        self.type = type
        self.is_forum = is_forum
        self.is_verified = is_verified
        self.is_members_hidden = is_members_hidden
        self.is_restricted = is_restricted
        self.is_creator = is_creator
        self.is_admin = is_admin
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_deactivated = is_deactivated
        self.is_support = is_support
        self.is_stories_hidden = is_stories_hidden
        self.is_stories_unavailable = is_stories_unavailable
        self.is_business_bot = is_business_bot
        self.is_preview = is_preview
        self.is_banned = is_banned
        self.is_call_active = is_call_active
        self.is_call_not_empty = is_call_not_empty
        self.is_public = is_public
        self.is_paid_reactions_available = is_paid_reactions_available
        self.title = title
        self.username = username
        self.usernames = usernames
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.stories = stories
        self.wallpaper = wallpaper
        self.bio = bio
        self.description = description
        self.dc_id = dc_id
        self.folder_id = folder_id
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.sticker_set_name = sticker_set_name
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.can_send_paid_media = can_send_paid_media
        self.members = members
        self.members_count = members_count
        self.restrictions = restrictions
        self.permissions = permissions
        self.personal_channel = personal_channel
        self.personal_channel_message = personal_channel_message
        self.linked_chat = linked_chat
        self.send_as_chat = send_as_chat
        self.available_reactions = available_reactions
        self.level = level
        self.reply_color = reply_color
        self.profile_color = profile_color
        self.business_info = business_info
        self.business_intro = business_intro
        self.birthday = birthday
        self.message_auto_delete_time = message_auto_delete_time
        self.unrestrict_boost_count = unrestrict_boost_count
        self.slow_mode_delay = slow_mode_delay
        self.slowmode_next_send_date = slowmode_next_send_date
        self.join_by_request = join_by_request
        self.join_requests_count = join_requests_count
        self.banned_until_date = banned_until_date
        self.subscription_until_date = subscription_until_date
        self.reactions_limit = reactions_limit
        self.raw = raw

    @staticmethod
    def _parse_user_chat(client, user: raw.types.User) -> "Chat":
        peer_id = user.id

        return Chat(
            id=peer_id,
            type=enums.ChatType.BOT if user.bot else enums.ChatType.PRIVATE,
            is_verified=getattr(user, "verified", None),
            is_restricted=getattr(user, "restricted", None),
            is_scam=getattr(user, "scam", None),
            is_fake=getattr(user, "fake", None),
            is_support=getattr(user, "support", None),
            is_stories_hidden=getattr(user, "stories_hidden", None),
            is_stories_unavailable=getattr(user, "stories_unavailable", None),
            is_business_bot=getattr(user, "bot_business", None),
            username=user.username or (user.usernames[0].username if user.usernames else None),
            usernames=types.List([types.Username._parse(r) for r in user.usernames]) or None,
            first_name=user.first_name,
            last_name=user.last_name,
            photo=types.ChatPhoto._parse(client, user.photo, peer_id, user.access_hash),
            restrictions=types.List([types.Restriction._parse(r) for r in user.restriction_reason]) or None,
            dc_id=getattr(getattr(user, "photo", None), "dc_id", None),
            reply_color=types.ChatColor._parse(getattr(user, "color", None)),
            profile_color=types.ChatColor._parse_profile_color(getattr(user, "profile_color", None)),
            raw=user,
            client=client
        )

    @staticmethod
    def _parse_chat_chat(client, chat: raw.types.Chat) -> "Chat":
        peer_id = -chat.id
        usernames = getattr(chat, "usernames", [])
        admin_rights = getattr(chat, "admin_rights", None)

        if isinstance(chat, raw.types.ChatForbidden):
            return Chat(
                id=peer_id,
                type=enums.ChatType.GROUP,
                title=chat.title,
                is_banned=True,
                raw=chat,
                client=client
            )

        return Chat(
            id=peer_id,
            type=enums.ChatType.GROUP,
            title=chat.title,
            is_creator=getattr(chat, "creator", None),
            is_admin=True if admin_rights else None,
            is_deactivated=getattr(chat, "deactivated", None),
            is_call_active=getattr(chat, "call_active", None),
            is_call_not_empty=getattr(chat, "call_not_empty", None),
            usernames=types.List([types.Username._parse(r) for r in usernames]) or None,
            photo=types.ChatPhoto._parse(client, getattr(chat, "photo", None), peer_id, 0),
            permissions=types.ChatPermissions._parse(getattr(chat, "default_banned_rights", None)),
            members_count=getattr(chat, "participants_count", None),
            dc_id=getattr(getattr(chat, "photo", None), "dc_id", None),
            has_protected_content=getattr(chat, "noforwards", None),
            raw=chat,
            client=client
        )

    @staticmethod
    def _parse_channel_chat(client, channel: raw.types.Channel) -> "Chat":
        peer_id = utils.get_channel_id(channel.id)
        restriction_reason = getattr(channel, "restriction_reason", [])
        usernames = getattr(channel, "usernames", [])
        admin_rights = getattr(channel, "admin_rights", None)

        if isinstance(channel, raw.types.ChannelForbidden):
            return Chat(
                id=peer_id,
                type=enums.ChatType.SUPERGROUP if getattr(channel, "megagroup", None) else enums.ChatType.CHANNEL,
                title=channel.title,
                is_banned=True,
                banned_until_date=utils.timestamp_to_datetime(getattr(channel, "until_date", None)),
                raw=channel,
                client=client,
            )

        return Chat(
            id=peer_id,
            type=enums.ChatType.SUPERGROUP if getattr(channel, "megagroup", None) else enums.ChatType.CHANNEL,
            is_forum=getattr(channel, "forum", None) if getattr(channel, "megagroup", None) else None,
            is_verified=getattr(channel, "verified", None),
            is_restricted=getattr(channel, "restricted", None),
            is_creator=getattr(channel, "creator", None),
            is_admin=True if admin_rights else None,
            is_scam=getattr(channel, "scam", None),
            is_fake=getattr(channel, "fake", None),
            is_stories_hidden=getattr(channel, "stories_hidden", None),
            is_stories_unavailable=getattr(channel, "stories_unavailable", None),
            is_call_active=getattr(channel, "call_active", None),
            is_call_not_empty=getattr(channel, "call_not_empty", None),
            title=channel.title,
            username=getattr(channel, "username", None),
            usernames=types.List([types.Username._parse(r) for r in usernames]) or None,
            photo=types.ChatPhoto._parse(client, getattr(channel, "photo", None), peer_id,
                                         getattr(channel, "access_hash", 0)),
            restrictions=types.List([types.Restriction._parse(r) for r in restriction_reason]) or None,
            permissions=types.ChatPermissions._parse(getattr(channel, "default_banned_rights", None)),
            members_count=getattr(channel, "participants_count", None),
            dc_id=getattr(getattr(channel, "photo", None), "dc_id", None),
            has_protected_content=getattr(channel, "noforwards", None),
            level=getattr(channel, "level", None),
            reply_color=types.ChatColor._parse(getattr(channel, "color", None)),
            profile_color=types.ChatColor._parse(getattr(channel, "profile_color", None)),
            subscription_until_date=utils.timestamp_to_datetime(getattr(channel, "subscription_until_date", None)),
            raw=channel,
            client=client
        )

    @staticmethod
    def _parse(
        client,
        message: Union[raw.types.Message, raw.types.MessageService],
        users: dict,
        chats: dict,
        is_chat: bool
    ) -> "Chat":
        from_id = utils.get_raw_peer_id(message.from_id)
        peer_id = utils.get_raw_peer_id(message.peer_id)
        chat_id = (peer_id or from_id) if is_chat else (from_id or peer_id)

        if isinstance(message.peer_id, raw.types.PeerUser):
            return Chat._parse_user_chat(client, users[chat_id])

        if isinstance(message.peer_id, raw.types.PeerChat):
            return Chat._parse_chat_chat(client, chats[chat_id])

        return Chat._parse_channel_chat(client, chats[chat_id])

    @staticmethod
    def _parse_dialog(client, peer, users: dict, chats: dict):
        if isinstance(peer, (raw.types.PeerUser, raw.types.InputPeerUser)):
            return Chat._parse_user_chat(client, users[peer.user_id])
        elif isinstance(peer, (raw.types.PeerChat, raw.types.InputPeerChat)):
            return Chat._parse_chat_chat(client, chats[peer.chat_id])
        else:
            return Chat._parse_channel_chat(client, chats[peer.channel_id])

    @staticmethod
    async def _parse_full(client, chat_full: Union[raw.types.messages.ChatFull, raw.types.users.UserFull]) -> "Chat":
        users = {u.id: u for u in chat_full.users}
        chats = {c.id: c for c in chat_full.chats}

        if isinstance(chat_full, raw.types.users.UserFull):
            full_user: "raw.types.UserFull" = chat_full.full_user

            parsed_chat = Chat._parse_user_chat(client, users[full_user.id])
            parsed_chat.bio = full_user.about
            parsed_chat.folder_id = getattr(full_user, "folder_id", None)
            parsed_chat.business_info = types.BusinessInfo._parse(client, full_user, users)
            parsed_chat.business_intro = await types.BusinessIntro._parse(client, getattr(full_user, "business_intro", None))
            parsed_chat.birthday = types.Birthday._parse(getattr(full_user, "birthday", None))
            parsed_chat.raw = full_user

            if full_user.pinned_msg_id:
                parsed_chat.pinned_message = await client.get_messages(
                    parsed_chat.id,
                    message_ids=full_user.pinned_msg_id
                )

            if full_user.personal_channel_id:
                parsed_chat.personal_channel = Chat._parse_channel_chat(client, chats[full_user.personal_channel_id])
                parsed_chat.personal_channel_message = await client.get_messages(
                    parsed_chat.personal_channel.id,
                    message_ids=full_user.personal_channel_message
                )

            if full_user.stories:
                peer_stories: raw.types.PeerStories = full_user.stories
                parsed_chat.stories = types.List(
                    [
                        await types.Story._parse(
                            client, story, users, chats, peer_stories.peer
                        )
                        for story in peer_stories.stories
                    ]
                ) or None

            if getattr(full_user, "wallpaper") and isinstance(full_user.wallpaper, raw.types.WallPaper):
                parsed_chat.wallpaper = types.Document._parse(client, full_user.wallpaper.document, "wallpaper.jpg")
        else:
            full_chat: Union["raw.types.ChatFull", "raw.types.ChannelFull"] = chat_full.full_chat
            chat_raw = chats[full_chat.id]

            if isinstance(full_chat, raw.types.ChatFull):
                parsed_chat = Chat._parse_chat_chat(client, chat_raw)
                parsed_chat.description = full_chat.about or None

                if isinstance(full_chat.participants, raw.types.ChatParticipants):
                    parsed_chat.members_count = len(full_chat.participants.participants)
            else:
                parsed_chat = Chat._parse_channel_chat(client, chat_raw)
                parsed_chat.members_count = full_chat.participants_count
                parsed_chat.description = full_chat.about or None
                # TODO: Add StickerSet type
                parsed_chat.can_set_sticker_set = full_chat.can_set_stickers
                parsed_chat.sticker_set_name = getattr(full_chat.stickerset, "short_name", None)
                parsed_chat.custom_emoji_sticker_set_name = getattr(full_chat.emojiset, "short_name", None)
                parsed_chat.is_members_hidden = full_chat.participants_hidden
                parsed_chat.has_visible_history = not getattr(full_chat, "hidden_prehistory", False)
                parsed_chat.has_aggressive_anti_spam_enabled = getattr(full_chat, "antispam", False)
                parsed_chat.slow_mode_delay = getattr(full_chat, "slowmode_seconds", None)
                parsed_chat.slowmode_next_send_date = utils.timestamp_to_datetime(
                    getattr(full_chat, "slowmode_next_send_date", None)
                )
                parsed_chat.can_send_paid_media = getattr(full_chat, "paid_media_allowed", None)
                parsed_chat.is_paid_reactions_available = getattr(full_chat, "paid_reactions_available", None)

                linked_chat_raw = chats.get(full_chat.linked_chat_id, None)

                if linked_chat_raw:
                    parsed_chat.linked_chat = Chat._parse_channel_chat(client, linked_chat_raw)

                default_send_as = full_chat.default_send_as

                if default_send_as:
                    if isinstance(default_send_as, raw.types.PeerUser):
                        send_as_raw = users[default_send_as.user_id]
                    else:
                        send_as_raw = chats[default_send_as.channel_id]

                    parsed_chat.send_as_chat = Chat._parse_chat(client, send_as_raw)

                if full_chat.stories:
                    peer_stories: raw.types.PeerStories = full_chat.stories
                    parsed_chat.stories = types.List(
                        [
                            await types.Story._parse(
                                client, story, users, chats, peer_stories.peer
                            )
                            for story in peer_stories.stories
                        ]
                    ) or None


                if full_chat.wallpaper and isinstance(full_chat.wallpaper, raw.types.WallPaper):
                    parsed_chat.wallpaper = types.Document._parse(client, full_chat.wallpaper.document, "wallpaper.jpg")

            if full_chat.pinned_msg_id:
                parsed_chat.pinned_message = await client.get_messages(
                    parsed_chat.id,
                    message_ids=full_chat.pinned_msg_id
                )

            if isinstance(full_chat.exported_invite, raw.types.ChatInviteExported):
                parsed_chat.invite_link = full_chat.exported_invite.link

            parsed_chat.available_reactions = types.ChatReactions._parse(client, full_chat.available_reactions)
            parsed_chat.folder_id = getattr(full_chat, "folder_id", None)
            parsed_chat.message_auto_delete_time = getattr(full_chat, "ttl_period", None)
            parsed_chat.unrestrict_boost_count = getattr(full_chat, "boosts_unrestrict", None)
            parsed_chat.join_requests_count = getattr(full_chat, "requests_pending", None)
            parsed_chat.reactions_limit = getattr(full_chat, "reactions_limit", None)

            parsed_chat.raw = full_chat

        return parsed_chat

    @staticmethod
    def _parse_chat(client, chat: Union[raw.types.Chat, raw.types.User, raw.types.Channel]) -> "Chat":
        if isinstance(chat, raw.types.Chat):
            return Chat._parse_chat_chat(client, chat)
        elif isinstance(chat, raw.types.User):
            return Chat._parse_user_chat(client, chat)
        else:
            return Chat._parse_channel_chat(client, chat)

    @staticmethod
    def _parse_preview(client, chat_invite: "raw.types.ChatInvite") -> "Chat":
        return Chat(
            type=(
                enums.ChatType.SUPERGROUP if getattr(chat_invite, "megagroup", None) else
                enums.ChatType.CHANNEL if getattr(chat_invite, "broadcast", None) else
                enums.ChatType.GROUP
            ),
            is_verified=getattr(chat_invite, "verified", None),
            is_scam=getattr(chat_invite, "scam", None),
            is_fake=getattr(chat_invite, "fake", None),
            is_public=getattr(chat_invite, "public", None),
            is_preview=True,
            title=chat_invite.title,
            photo=types.Photo._parse(client, chat_invite.photo),
            members_count=chat_invite.participants_count,
            members=[
                types.User._parse(client, user)
                for user in getattr(chat_invite, "participants", [])
            ] or None,
            description=getattr(chat_invite, "about", None),
            join_by_request=getattr(chat_invite, "request_needed", None),
            profile_color=types.ChatColor._parse(getattr(chat_invite, "color", None)),
            raw=chat_invite,
            client=client
        )

    @property
    def full_name(self) -> str:
        return " ".join(filter(None, [self.first_name, self.last_name])) or self.title or None

    async def archive(self):
        """Bound method *archive* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.archive_chats(-100123456789)

        Example:
            .. code-block:: python

                await chat.archive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.archive_chats(self.id)

    async def unarchive(self):
        """Bound method *unarchive* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unarchive_chats(-100123456789)

        Example:
            .. code-block:: python

                await chat.unarchive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unarchive_chats(self.id)

    # TODO: Remove notes about "All Members Are Admins" for basic groups, the attribute doesn't exist anymore
    async def set_title(self, title: str) -> bool:
        """Bound method *set_title* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_title(
                chat_id=chat_id,
                title=title
            )

        Example:
            .. code-block:: python

                await chat.set_title("Lounge")

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins"
            setting is off.

        Parameters:
            title (``str``):
                New chat title, 1-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of Telegram RPC error.
            ValueError: In case a chat_id belongs to user.
        """

        return await self._client.set_chat_title(
            chat_id=self.id,
            title=title
        )

    async def set_description(self, description: str) -> bool:
        """Bound method *set_description* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_description(
                chat_id=chat_id,
                description=description
            )

        Example:
            .. code-block:: python

                await chat.set_chat_description("Don't spam!")

        Parameters:
            description (``str``):
                New chat description, 0-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of Telegram RPC error.
            ValueError: If a chat_id doesn't belong to a supergroup or a channel.
        """

        return await self._client.set_chat_description(
            chat_id=self.id,
            description=description
        )

    async def set_photo(
        self,
        *,
        photo: Union[str, BinaryIO] = None,
        video: Union[str, BinaryIO] = None,
        video_start_ts: float = None,
    ) -> bool:
        """Bound method *set_photo* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_photo(
                chat_id=chat_id,
                photo=photo
            )

        Example:
            .. code-block:: python

                # Set chat photo using a local file
                await chat.set_photo(photo="photo.jpg")

                # Set chat photo using an existing Photo file_id
                await chat.set_photo(photo=photo.file_id)


                # Set chat video using a local file
                await chat.set_photo(video="video.mp4")

                # Set chat photo using an existing Video file_id
                await chat.set_photo(video=video.file_id)

        Parameters:
            photo (``str`` | ``BinaryIO``, *optional*):
                New chat photo. You can pass a :obj:`~vegagram.types.Photo` file_id, a file path to upload a new photo
                from your local machine or a binary file-like object with its attribute
                ".name" set for in-memory uploads.

            video (``str`` | ``BinaryIO``, *optional*):
                New chat video. You can pass a :obj:`~vegagram.types.Video` file_id, a file path to upload a new video
                from your local machine or a binary file-like object with its attribute
                ".name" set for in-memory uploads.

            video_start_ts (``float``, *optional*):
                The timestamp in seconds of the video frame to use as photo profile preview.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
            ValueError: if a chat_id belongs to user.
        """

        return await self._client.set_chat_photo(
            chat_id=self.id,
            photo=photo,
            video=video,
            video_start_ts=video_start_ts
        )

    async def set_ttl(self, ttl_seconds: int) -> "types.Message":
        """Bound method *set_ttl* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_ttl(
                chat_id=chat_id,
                ttl_seconds=ttl_seconds
            )

        Example:
            .. code-block:: python

                await chat.set_ttl(86400)

        Returns:
            :obj:`~vegagram.types.Message`: On success, the generated service message is returned.
        """
        return await self._client.set_chat_ttl(
            chat_id=self.id,
            ttl_seconds=ttl_seconds
        )

    async def ban_member(
        self,
        user_id: Union[int, str],
        until_date: datetime = utils.zero_datetime()
    ) -> Union["types.Message", bool]:
        """Bound method *ban_member* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.ban_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:
            .. code-block:: python

                await chat.ban_member(123456789)

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins" setting is
            off in the target group. Otherwise members may only be removed by the group's creator or by the member
            that added them.

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

        Returns:
            :obj:`~vegagram.types.Message` | ``bool``: On success, a service message will be returned (when applicable), otherwise, in
            case a message object couldn't be returned, True is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.ban_chat_member(
            chat_id=self.id,
            user_id=user_id,
            until_date=until_date
        )

    async def unban_member(
        self,
        user_id: Union[int, str]
    ) -> bool:
        """Bound method *unban_member* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unban_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:
            .. code-block:: python

                await chat.unban_member(123456789)

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unban_chat_member(
            chat_id=self.id,
            user_id=user_id,
        )

    async def restrict_member(
        self,
        user_id: Union[int, str],
        permissions: "types.ChatPermissions",
        until_date: datetime = utils.zero_datetime(),
    ) -> "types.Chat":
        """Bound method *unban_member* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.restrict_chat_member(
                chat_id=chat_id,
                user_id=user_id,
                permissions=ChatPermissions()
            )

        Example:
            .. code-block:: python

                await chat.restrict_member(user_id, ChatPermissions())

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            permissions (:obj:`~vegagram.types.ChatPermissions`):
                New user permissions.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

        Returns:
            :obj:`~vegagram.types.Chat`: On success, a chat object is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.restrict_chat_member(
            chat_id=self.id,
            user_id=user_id,
            permissions=permissions,
            until_date=until_date,
        )

    # Set None as privileges default due to issues with partially initialized module, because at the time Chat
    # is being initialized, ChatPrivileges would be required here, but was not initialized yet.
    async def promote_member(
        self,
        user_id: Union[int, str],
        privileges: "types.ChatPrivileges" = None
    ) -> bool:
        """Bound method *promote_member* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.promote_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:

            .. code-block:: python

                await chat.promote_member(123456789)

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            privileges (:obj:`~vegagram.types.ChatPrivileges`, *optional*):
                New user privileges.

        Returns:
            ``bool``: True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.promote_chat_member(
            chat_id=self.id,
            user_id=user_id,
            privileges=privileges
        )

    async def join(self):
        """Bound method *join* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.join_chat(123456789)

        Example:
            .. code-block:: python

                await chat.join()

        Note:
            This only works for public groups, channels that have set a username or linked chats.

        Returns:
            :obj:`~vegagram.types.Chat`: On success, a chat object is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.join_chat(self.username or self.id)

    async def leave(self):
        """Bound method *leave* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.leave_chat(123456789)

        Example:
            .. code-block:: python

                await chat.leave()

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.leave_chat(self.id)

    async def export_invite_link(self):
        """Bound method *export_invite_link* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.export_chat_invite_link(123456789)

        Example:
            .. code-block:: python

                chat.export_invite_link()

        Returns:
            ``str``: On success, the exported invite link is returned.

        Raises:
            ValueError: In case the chat_id belongs to a user.
        """

        return await self._client.export_chat_invite_link(self.id)

    async def get_member(
        self,
        user_id: Union[int, str],
    ) -> "types.ChatMember":
        """Bound method *get_member* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.get_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )

        Example:
            .. code-block:: python

                await chat.get_member(user_id)

        Returns:
            :obj:`~vegagram.types.ChatMember`: On success, a chat member is returned.
        """

        return await self._client.get_chat_member(
            self.id,
            user_id=user_id
        )

    def get_members(
        self,
        query: str = "",
        limit: int = 0,
        filter: "enums.ChatMembersFilter" = enums.ChatMembersFilter.SEARCH
    ) -> AsyncGenerator["types.ChatMember", None]:
        """Bound method *get_members* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            async for member in client.get_chat_members(chat_id):
                print(member)

        Example:
            .. code-block:: python

                async for member in chat.get_members():
                    print(member)

        Parameters:
            query (``str``, *optional*):
                Query string to filter members based on their display names and usernames.
                Only applicable to supergroups and channels. Defaults to "" (empty string).
                A query string is applicable only for :obj:`~vegagram.enums.ChatMembersFilter.SEARCH`,
                :obj:`~vegagram.enums.ChatMembersFilter.BANNED` and :obj:`~vegagram.enums.ChatMembersFilter.RESTRICTED`
                filters only.

            limit (``int``, *optional*):
                Limits the number of members to be retrieved.

            filter (:obj:`~vegagram.enums.ChatMembersFilter`, *optional*):
                Filter used to select the kind of members you want to retrieve. Only applicable for supergroups
                and channels.

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~vegagram.types.ChatMember` objects is returned.
        """

        return self._client.get_chat_members(
            self.id,
            query=query,
            limit=limit,
            filter=filter
        )

    async def add_members(
        self,
        user_ids: Union[Union[int, str], List[Union[int, str]]],
        forward_limit: int = 100
    ) -> bool:
        """Bound method *add_members* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.add_chat_members(chat_id, user_id)

        Example:
            .. code-block:: python

                await chat.add_members(user_id)

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.add_chat_members(
            self.id,
            user_ids=user_ids,
            forward_limit=forward_limit
        )

    async def mark_unread(self, ) -> bool:
        """Bound method *mark_unread* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.mark_unread(chat_id)

        Example:
            .. code-block:: python

                await chat.mark_unread()

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.mark_chat_unread(self.id)

    async def set_protected_content(self, enabled: bool) -> bool:
        """Bound method *set_protected_content* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            await client.set_chat_protected_content(chat_id, enabled)

        Parameters:
            enabled (``bool``):
                Pass True to enable the protected content setting, False to disable.

        Example:
            .. code-block:: python

                await chat.set_protected_content(enabled)

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.set_chat_protected_content(
            self.id,
            enabled=enabled
        )

    async def unpin_all_messages(self) -> bool:
        """Bound method *unpin_all_messages* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.unpin_all_chat_messages(chat_id)

        Example:
            .. code-block:: python

                chat.unpin_all_messages()

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.unpin_all_chat_messages(self.id)

    async def mute(self, mute_until: datetime = None) -> bool:
        """Bound method *mute* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.update_chat_notifications(chat_id, mute=True, mute_until=mute_until)

        Parameters:
            mute (``bool``, *optional*):
                Pass True if you want to mute chat.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unmuted. Defaults to forever.

        Example:
            .. code-block:: python

                chat.mute()

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.update_chat_notifications(self.id, mute=True, mute_until=mute_until)

    async def unmute(self) -> bool:
        """Bound method *unmute* of :obj:`~vegagram.types.Chat`.

        Use as a shortcut for:

        .. code-block:: python

            client.update_chat_notifications(chat_id, mute=False)

        Example:
            .. code-block:: python

                chat.unmute()

        Returns:
            ``bool``: On success, True is returned.
        """

        return await self._client.update_chat_notifications(self.id, mute=False)
