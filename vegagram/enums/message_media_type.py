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

from enum import auto

from .auto_name import AutoName


class MessageMediaType(AutoName):
    """Message media type enumeration used in :obj:`~vegagram.types.Message`."""

    AUDIO = auto()
    "Audio media"

    DOCUMENT = auto()
    "Document media"

    PHOTO = auto()
    "Photo media"

    STICKER = auto()
    "Sticker media"

    VIDEO = auto()
    "Video media"

    ANIMATION = auto()
    "Animation media"

    VOICE = auto()
    "Voice media"

    VIDEO_NOTE = auto()
    "Video note media"

    CONTACT = auto()
    "Contact media"

    LOCATION = auto()
    "Location media"

    VENUE = auto()
    "Venue media"

    POLL = auto()
    "Poll media"

    WEB_PAGE = auto()
    "Web page media"

    DICE = auto()
    "Dice media"

    GAME = auto()
    "Game media"

    GIVEAWAY = auto()
    "Giveaway media"

    GIVEAWAY_WINNERS = auto()
    "Giveaway winners media"

    STORY = auto()
    "Story media"

    INVOICE = auto()
    "Invoice media"

    PAID_MEDIA = auto()
    "Paid media"