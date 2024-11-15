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

from typing import Union

import vegagram
from vegagram import raw
from vegagram import types


class StartBot:
    async def start_bot(
        self: "vegagram.Client",
        chat_id: Union[int, str],
        param: str = ""
    ) -> "types.Message":
        """Start bot

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier of the bot you want to be started. You can specify
                a @username (str) or a bot ID (int).

            param (``str``):
                Text of the deep linking parameter (up to 64 characters).
                Defaults to "" (empty string).

        Returns:
            :obj:`~vegagram.types.Message`: On success, the sent message is returned.

        Example:
            .. code-block:: python

                # Start bot
                await app.start_bot("vegagrambot")

                # Start bot with param
                await app.start_bot("vegagrambot", "ref123456")
        """
        if not param:
            return await self.send_message(chat_id, "/start")

        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.messages.StartBot(
                bot=peer,
                peer=peer,
                random_id=self.rnd_id(),
                start_param=param
            )
        )

        for i in r.updates:
            if isinstance(i, raw.types.UpdateNewMessage):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )
