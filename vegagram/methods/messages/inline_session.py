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
from vegagram.errors import AuthBytesInvalid
from vegagram.session import Session
from vegagram.session.auth import Auth


async def get_session(client: "vegagram.Client", dc_id: int) -> Session:
    if dc_id == await client.storage.dc_id():
        return client.session

    async with client.media_sessions_lock:
        if client.media_sessions.get(dc_id):
            return client.media_sessions[dc_id]

        session = client.media_sessions[dc_id] = Session(
            client, dc_id,
            await Auth(client, dc_id, await client.storage.test_mode()).create(),
            await client.storage.test_mode(), is_media=True
        )

        await session.start()

        for _ in range(3):
            exported_auth = await client.invoke(
                raw.functions.auth.ExportAuthorization(
                    dc_id=dc_id
                )
            )

            try:
                await session.invoke(
                    raw.functions.auth.ImportAuthorization(
                        id=exported_auth.id,
                        bytes=exported_auth.bytes
                    )
                )
            except AuthBytesInvalid:
                continue
            else:
                break
        else:
            await session.stop()
            raise AuthBytesInvalid

        return session
