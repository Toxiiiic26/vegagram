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

from typing import Optional, List

import vegagram
from vegagram import raw
from vegagram import types


class AnswerShippingQuery:
    async def answer_shipping_query(
        self: "vegagram.Client",
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[List["types.ShippingOption"]] = None,
        error_message: Optional[str] = None
    ):
        """If you sent an invoice requesting a shipping address and the parameter ``is_flexible`` was specified, the API sends the confirmation in the form of an :obj:`~vegagram.handlers.ShippingQueryHandler`.

        Use this method to reply to shipping queries.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            shipping_query_id (``str``):
                Unique identifier for the query to be answered.

            ok (``bool``):
                Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.

            shipping_options (List of :obj:`~vegagram.types.ShippingOptions`, *optional*):
                Required if ok is True. A array of available shipping options.

            error_message (``str``, *optional*):
                Required if ok is False.
                Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable"). Telegram will display this message to the user.

        Returns:
            ``bool``: True, on success.

        Example:
            .. code-block:: python

                # Proceed with the order
                await app.answer_shipping_query(query_id, ok=True, shipping_options=shipping_options)

                # Answer with error message
                await app.answer_shipping_query(query_id, ok=False, error_message="Error Message displayed to the user")

        """
        if ok and not shipping_options:
            raise ValueError("Shipping options required.")

        r = await self.invoke(
            raw.functions.messages.SetBotShippingResults(
                query_id=int(shipping_query_id),
                shipping_options=[
                    so.write()
                    for so in shipping_options
                ] if shipping_options else None,
                error=error_message
            )
        )

        return r
