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

from typing import Dict

import vegagram
from vegagram import raw, utils
from vegagram import types
from ..object import Object
from ..update import Update


class ChatBoostUpdated(Object, Update):
    """A channel/supergroup boost has changed (bots only).

    Parameters:
        chat (:obj:`~vegagram.types.Chat`):
            The chat where boost was changed.

        boost (:obj:`~vegagram.types.ChatBoost`):
            New boost information.
    """

    def __init__(
        self,
        *,
        client: "vegagram.Client" = None,
        chat: "types.Chat",
        boost: "types.ChatBoost"
    ):
        super().__init__(client)

        self.chat = chat
        self.boost = boost

    @staticmethod
    def _parse(
        client: "vegagram.Client",
        update: "raw.types.UpdateBotChatBoost",
        users: Dict[int, "raw.types.User"],
        chats: Dict[int, "raw.types.Channel"],
    ) -> "ChatBoostUpdated":
        return ChatBoostUpdated(
            chat=types.Chat._parse_channel_chat(client, chats.get(utils.get_raw_peer_id(update.peer))),
            boost=types.ChatBoost._parse(client, update.boost, users),
            client=client
        )
