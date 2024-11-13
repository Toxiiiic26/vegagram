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

from datetime import datetime
from typing import Union, List, Optional

import vegagram
from vegagram import raw, enums
from vegagram import types
from vegagram import utils


class EditMessageText:
    async def edit_message_text(
        self: "vegagram.Client",
        chat_id: Union[int, str],
        message_id: int,
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: List["types.MessageEntity"] = None,
        disable_web_page_preview: bool = None,
        show_caption_above_media: bool = None,
        schedule_date: datetime = None,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> "types.Message":
        """Edit the text of messages.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Message identifier in the chat specified in chat_id.

            text (``str``):
                New text of the message.

            parse_mode (:obj:`~vegagram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            entities (List of :obj:`~vegagram.types.MessageEntity`):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message.

            show_caption_above_media (``bool``, *optional*):
                Pass True, if the caption must be shown above the message media.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            reply_markup (:obj:`~vegagram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~vegagram.types.Message`: On success, the edited message is returned.

        Example:
            .. code-block:: python

                # Simple edit text
                await app.edit_message_text(chat_id, message_id, "new text")

                # Take the same text message, remove the web page preview only
                await app.edit_message_text(
                    chat_id, message_id, message.text,
                    disable_web_page_preview=True)
        """

        r = await self.invoke(
            raw.functions.messages.EditMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                no_webpage=disable_web_page_preview or None,
                invert_media=show_caption_above_media or None,
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                **await utils.parse_text_entities(self, text, parse_mode, entities)
            )
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateEditMessage, raw.types.UpdateEditChannelMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )
