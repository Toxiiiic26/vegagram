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

import vegagram
from vegagram import raw

log = logging.getLogger(__name__)


class Terminate:
    async def terminate(
        self: "vegagram.Client",
    ):
        """Terminate the client by shutting down workers.

        This method does the opposite of :meth:`~vegagram.Client.initialize`.
        It will stop the dispatcher and shut down updates and download workers.

        Raises:
            ConnectionError: In case you try to terminate a client that is already terminated.
        """
        if not self.is_initialized:
            raise ConnectionError("Client is already terminated")

        if self.takeout_id:
            await self.invoke(raw.functions.account.FinishTakeoutSession())
            log.info("Takeout session %s finished", self.takeout_id)

        await self.storage.save()
        await self.dispatcher.stop()

        for media_session in self.media_sessions.values():
            await media_session.stop()

        self.media_sessions.clear()

        self.updates_watchdog_event.set()

        if self.updates_watchdog_task is not None:
            await self.updates_watchdog_task

        self.updates_watchdog_event.clear()

        self.is_initialized = False
