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


class AnswerWebAppQuery:
    async def answer_web_app_query(
        self: "vegagram.Client",
        web_app_query_id: str,
        result: "types.InlineQueryResult"
    ) -> "types.SentWebAppMessage":
        """Set the result of an interaction with a `Web App <https://core.telegram.org/bots/webapps>`_ and send a
        corresponding message on behalf of the user to the chat from which the query originated.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            web_app_query_id (``str``):
                Unique identifier for the answered query.

            result (:obj:`~vegagram.types.InlineQueryResult`):
                A list of results for the inline query.

        Returns:
            :obj:`~vegagram.types.SentWebAppMessage`: On success the sent web app message is returned.
        """

        r = await self.invoke(
            raw.functions.messages.SendWebViewResultMessage(
                bot_query_id=web_app_query_id,
                result=await result.write(self)
            )
        )

        return types.SentWebAppMessage._parse(r)