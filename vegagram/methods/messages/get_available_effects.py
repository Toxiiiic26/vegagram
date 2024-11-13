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

import logging
from typing import List

import vegagram
from vegagram import raw
from vegagram import types

log = logging.getLogger(__name__)


class GetAvailableEffects:
    async def get_available_effects(
        self: "vegagram.Client"
    ) -> List["types.AvailableEffect"]:
        """Get all available effects.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~vegagram.types.AvailableEffect`: A list of available effects is returned.

        Example:
            .. code-block:: python

                # Get all available effects
                await app.get_available_effects()
        """
        r = await self.invoke(
            raw.functions.messages.GetAvailableEffects(
                hash=0
            )
        )

        documents = {d.id: d for d in r.documents}

        return types.List(
            [
                await types.AvailableEffect._parse(self, effect, documents.get(effect.effect_sticker_id, None))
                for effect in r.effects
            ]
        )