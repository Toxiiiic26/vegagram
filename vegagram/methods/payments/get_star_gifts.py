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
from typing import List

import vegagram
from vegagram import raw, types


class GetStarGifts:
    async def get_star_gifts(
        self: "vegagram.Client",
    ) -> List["types.StarGift"]:
        """Get all available star gifts to send.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~vegagram.types.StarGift`: On success, a list of star gifts is returned.

        Example:
            .. code-block:: python

                app.get_star_gifts()
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGifts(hash=0)
        )

        return types.List([await types.StarGift._parse(self, gift) for gift in r.gifts])
