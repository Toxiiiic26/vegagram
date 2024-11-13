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

from vegagram import raw, types

from ..object import Object


class ActiveSessions(Object):
    """Contains a list of currently active sessions

    Parameters:
        inactive_session_ttl_days (``int``):
            Number of days of inactivity before sessions will automatically be terminated; 1-366 days.

        active_sessions (List of :obj:`~vegagram.types.ActiveSession`):
            List of sessions.
    """

    def __init__(
        self,
        *,
        inactive_session_ttl_days: int = None,
        active_sessions: List["types.ActiveSession"] = None
    ):
        super().__init__()

        self.inactive_session_ttl_days = inactive_session_ttl_days
        self.active_sessions = active_sessions

    @staticmethod
    def _parse(authorizations: "raw.types.account.Authorizations") -> "ActiveSessions":
        return ActiveSessions(
            inactive_session_ttl_days=authorizations.authorization_ttl_days,
            active_sessions=types.List([
                types.ActiveSession._parse(active)
                for active in authorizations.authorizations
            ])
        )
