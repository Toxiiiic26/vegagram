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


class SearchContacts:
    async def search_contacts(
        self: "vegagram.Client",
        query: str,
        limit: int = 0
    ):
        """Returns users or channels found by name substring and auxiliary data.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            query (``str``):
                Target substring.

            limit (``int``, *optional*):
                Maximum number of users to be returned.

        Returns:
            :obj:`~vegagram.types.FoundContacts`: On success, a list of chats is returned.

        Example:
            .. code-block:: python

                await app.search_contacts("vegagram")
        """
        total = limit or (1 << 31) - 1
        limit = min(100, total)

        r = await self.invoke(
            raw.functions.contacts.Search(
                q=query,
                limit=limit
            )
        )

        return types.FoundContacts._parse(self, r)
