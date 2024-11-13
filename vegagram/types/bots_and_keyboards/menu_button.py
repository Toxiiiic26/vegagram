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
from ..object import Object


class MenuButton(Object):
    """Describes the bot's menu button in a private chat.

    It should be one of:

    - :obj:`~vegagram.types.MenuButtonCommands`
    - :obj:`~vegagram.types.MenuButtonWebApp`
    - :obj:`~vegagram.types.MenuButtonDefault`

    If a menu button other than :obj:`~vegagram.types.MenuButtonDefault` is set for a private chat, then it is applied
    in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot
    commands.
    """

    def __init__(self, type: str):
        super().__init__()

        self.type = type

    async def write(self, client: "vegagram.Client") -> "raw.base.BotMenuButton":
        raise NotImplementedError
