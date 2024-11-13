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

import vegagram
from vegagram import raw
from vegagram import types
from vegagram import utils
from ..object import Object
from ..update import Update


class ChosenInlineResult(Object, Update):
    """A :doc:`result <InlineQueryResult>` of an inline query chosen by the user and sent to their chat partner.

    .. note::

        In order to receive these updates, your bot must have "inline feedback" enabled. You can enable this feature
        with `@BotFather <https://t.me/botfather>`_.

    Parameters:
        result_id (``str``):
            The unique identifier for the result that was chosen.

        from_user (:obj:`~vegagram.types.User`):
            The user that chose the result.

        query (``str``):
            The query that was used to obtain the result.

        location (:obj:`~vegagram.types.Location`, *optional*):
            Sender location, only for bots that require user location.

        inline_message_id (``str``, *optional*):
            Identifier of the sent inline message.
            Available only if there is an :doc:`inline keyboard <InlineKeyboardMarkup>` attached to the message.
            Will be also received in :doc:`callback queries <CallbackQuery>` and can be used to edit the message.
    """

    def __init__(
        self,
        *,
        client: "vegagram.Client" = None,
        result_id: str,
        from_user: "types.User",
        query: str,
        location: "types.Location" = None,
        inline_message_id: str = None
    ):
        super().__init__(client)

        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        self.location = location
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(client, chosen_inline_result: raw.types.UpdateBotInlineSend, users) -> "ChosenInlineResult":
        return ChosenInlineResult(
            result_id=str(chosen_inline_result.id),
            from_user=types.User._parse(client, users[chosen_inline_result.user_id]),
            query=chosen_inline_result.query,
            location=types.Location(
                longitude=chosen_inline_result.geo.long,
                latitude=chosen_inline_result.geo.lat,
                client=client
            ) if chosen_inline_result.geo else None,
            inline_message_id=utils.pack_inline_message_id(
                chosen_inline_result.msg_id
            ) if getattr(chosen_inline_result, "msg_id", None) else None
        )
