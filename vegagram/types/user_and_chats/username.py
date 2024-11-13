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

from vegagram import raw
from ..object import Object


class Username(Object):
    """A Telegram user's or chat's username.

    Parameters:
        username (``str``):
            User's or chat's username.
        editable (``bool``, *optional*):
            True, if it's a basic username; False, if it's a collectible username.
        active (``bool``, *optional*):
            True, if the collectible username is active.
    """

    def __init__(self, *, username: str, editable: bool = None, active: bool = None):
        super().__init__(None)

        self.username = username
        self.editable = editable
        self.active = active

    @staticmethod
    def _parse(username: "raw.types.Username") -> "Username":
        return Username(
            username=username.username,
            editable=username.editable,
            active=username.active
        )
