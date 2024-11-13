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
from vegagram import raw, utils
from vegagram import types, enums


class SendPoll:
    async def send_poll(
        self: "vegagram.Client",
        chat_id: Union[int, str],
        question: str,
        options: List[str],
        is_anonymous: bool = True,
        type: "enums.PollType" = enums.PollType.REGULAR,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        question_parse_mode: Optional["enums.ParseMode"] = None,
        question_entities: Optional[List["types.MessageEntity"]] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional["enums.ParseMode"] = None,
        explanation_entities: Optional[List["types.MessageEntity"]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[datetime] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        effect_id: Optional[int] = None,
        reply_to_message_id: Optional[int] = None,
        reply_to_chat_id: Optional[Union[int, str]] = None,
        quote_text: Optional[str] = None,
        quote_parse_mode: Optional["enums.ParseMode"] = None,
        quote_entities: Optional[List["types.MessageEntity"]] = None,
        quote_offset: Optional[int] = None,
        schedule_date: Optional[datetime] = None,
        business_connection_id: Optional[str] = None,
        options_parse_mode: Optional["enums.ParseMode"] = None,
        allow_paid_broadcast: bool = None,
        reply_markup: Optional[
            Union[
                "types.InlineKeyboardMarkup",
                "types.ReplyKeyboardMarkup",
                "types.ReplyKeyboardRemove",
                "types.ForceReply"
            ]
        ] = None
    ) -> "types.Message":
        """Send a new poll.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            question (``str``):
                Poll question, 1-255 characters.

            options (List of ``str``):
                List of answer options, 2-10 strings 1-100 characters each.

            is_anonymous (``bool``, *optional*):
                True, if the poll needs to be anonymous.
                Defaults to True.

            type (:obj`~vegagram.enums.PollType`, *optional*):
                Poll type, :obj:`~vegagram.enums.PollType.QUIZ` or :obj:`~vegagram.enums.PollType.REGULAR`.
                Defaults to :obj:`~vegagram.enums.PollType.REGULAR`.

            allows_multiple_answers (``bool``, *optional*):
                True, if the poll allows multiple answers, ignored for polls in quiz mode.
                Defaults to False.

            correct_option_id (``int``, *optional*):
                0-based identifier of the correct answer option, required for polls in quiz mode.

            question_parse_mode (:obj:`~vegagram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            question_entities (List of :obj:`~vegagram.types.MessageEntity`):
                List of special entities that appear in the poll question, which can be specified instead of
                *parse_mode*.

            explanation (``str``, *optional*):
                Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style
                poll, 0-200 characters with at most 2 line feeds after entities parsing.

            explanation_parse_mode (:obj:`~vegagram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            explanation_entities (List of :obj:`~vegagram.types.MessageEntity`):
                List of special entities that appear in the poll explanation, which can be specified instead of
                *parse_mode*.

            open_period (``int``, *optional*):
                Amount of time in seconds the poll will be active after creation, 5-600.
                Can't be used together with *close_date*.

            close_date (:py:obj:`~datetime.datetime`, *optional*):
                Point in time when the poll will be automatically closed.
                Must be at least 5 and no more than 600 seconds in the future.
                Can't be used together with *open_period*.

            is_closed (``bool``, *optional*):
                Pass True, if the poll needs to be immediately closed.
                This can be useful for poll preview.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.
                For supergroups only.

            effect_id (``int``, *optional*):
                Unique identifier of the message effect.
                For private chats only.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            reply_to_chat_id (``int``, *optional*):
                If the message is a reply, ID of the original chat.

            quote_text (``str``, *optional*):
                Text of the quote to be sent.

            quote_parse_mode (:obj:`~vegagram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            quote_entities (List of :obj:`~vegagram.types.MessageEntity`, *optional*):
                List of special entities that appear in quote text, which can be specified instead of *parse_mode*.

            quote_offset (``int``, *optional*):
                Offset for quote in original message.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            business_connection_id (``str``, *optional*):
                Unique identifier of the business connection on behalf of which the message will be sent.

            options_parse_mode (:obj:`~vegagram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            allow_paid_broadcast (``bool``, *optional*):
                If True, you will be allowed to send up to 1000 messages per second.
                Ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
                The relevant Stars will be withdrawn from the bot's balance.
                For bots only.

            reply_markup (:obj:`~vegagram.types.InlineKeyboardMarkup` | :obj:`~vegagram.types.ReplyKeyboardMarkup` | :obj:`~vegagram.types.ReplyKeyboardRemove` | :obj:`~vegagram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            :obj:`~vegagram.types.Message`: On success, the sent poll message is returned.

        Example:
            .. code-block:: python

                await app.send_poll(chat_id, "Is this a poll question?", ["Yes", "No", "Maybe"])
        """
        question, question_entities = (await utils.parse_text_entities(
            self, question, question_parse_mode, question_entities
        )).values()

        solution, solution_entities = (await utils.parse_text_entities(
            self, explanation, explanation_parse_mode, explanation_entities
        )).values()

        quote_text, quote_entities = (await utils.parse_text_entities(
            self, quote_text, quote_parse_mode, quote_entities
        )).values()

        answers = []

        for i, opt in enumerate(options):
            option, option_entities = (await utils.parse_text_entities(
                self, opt, options_parse_mode, None
            )).values()

            answers.append(
                raw.types.PollAnswer(
                    text=raw.types.TextWithEntities(text=option, entities=option_entities or []),
                    option=bytes([i]),
                )
            )

        r = await self.invoke(
            raw.functions.messages.SendMedia(
                peer=await self.resolve_peer(chat_id),
                media=raw.types.InputMediaPoll(
                    poll=raw.types.Poll(
                        id=self.rnd_id(),
                        question=raw.types.TextWithEntities(
                            text=question,
                            entities=question_entities or []
                        ),
                        answers=answers,
                        closed=is_closed,
                        public_voters=not is_anonymous,
                        multiple_choice=allows_multiple_answers,
                        quiz=type == enums.PollType.QUIZ or False,
                        close_period=open_period,
                        close_date=utils.datetime_to_timestamp(close_date)
                    ),
                    correct_answers=[bytes([correct_option_id])] if correct_option_id is not None else None,
                    solution=solution,
                    solution_entities=solution_entities or []
                ),
                message="",
                silent=disable_notification,
                reply_to=utils.get_reply_to(
                    reply_to_message_id=reply_to_message_id,
                    message_thread_id=message_thread_id,
                    reply_to_peer=await self.resolve_peer(reply_to_chat_id) if reply_to_chat_id else None,
                    quote_text=quote_text,
                    quote_entities=quote_entities,
                    quote_offset=quote_offset,
                ),
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                noforwards=protect_content,
                allow_paid_floodskip=allow_paid_broadcast,
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                effect=effect_id
            ),
            business_connection_id=business_connection_id
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage,
                              raw.types.UpdateNewScheduledMessage,
                              raw.types.UpdateBotNewBusinessMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                    business_connection_id=getattr(i, "connection_id", None)
                )