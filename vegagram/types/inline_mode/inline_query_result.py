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

from uuid import uuid4

import vegagram
from vegagram import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~vegagram.types.InlineQueryResultCachedAudio`
    - :obj:`~vegagram.types.InlineQueryResultCachedDocument`
    - :obj:`~vegagram.types.InlineQueryResultCachedAnimation`
    - :obj:`~vegagram.types.InlineQueryResultCachedPhoto`
    - :obj:`~vegagram.types.InlineQueryResultCachedSticker`
    - :obj:`~vegagram.types.InlineQueryResultCachedVideo`
    - :obj:`~vegagram.types.InlineQueryResultCachedVoice`
    - :obj:`~vegagram.types.InlineQueryResultArticle`
    - :obj:`~vegagram.types.InlineQueryResultAudio`
    - :obj:`~vegagram.types.InlineQueryResultContact`
    - :obj:`~vegagram.types.InlineQueryResultDocument`
    - :obj:`~vegagram.types.InlineQueryResultAnimation`
    - :obj:`~vegagram.types.InlineQueryResultLocation`
    - :obj:`~vegagram.types.InlineQueryResultPhoto`
    - :obj:`~vegagram.types.InlineQueryResultVenue`
    - :obj:`~vegagram.types.InlineQueryResultVideo`
    - :obj:`~vegagram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "vegagram.Client"):
        pass
