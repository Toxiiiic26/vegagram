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
from vegagram.parser.markdown import Markdown


# expected: the expected unparsed Markdown
# text: original text without entities
# entities: message entities coming from the server

def test_markdown_unparse_bold():
    expected = "**bold**"
    text = "bold"
    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.BOLD, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_italic():
    expected = "__italic__"
    text = "italic"
    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.ITALIC, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_strike():
    expected = "~~strike~~"
    text = "strike"
    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.STRIKETHROUGH, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_spoiler():
    expected = "||spoiler||"
    text = "spoiler"
    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.SPOILER, offset=0, length=7)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_url():
    expected = '[URL](https://vegagram.org/)'
    text = "URL"
    entities = vegagram.types.List([vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.TEXT_LINK,
                                                                 offset=0, length=3, url='https://vegagram.org/')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_emoji():
    expected = '![🥲](tg://emoji?id=5195264424893488796) im crying'
    text = "🥲 im crying"
    entities = vegagram.types.List([vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.CUSTOM_EMOJI,
                                                                 offset=0, length=2, custom_emoji_id=5195264424893488796)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_code():
    expected = '`code`'
    text = "code"
    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.CODE, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_pre():
    expected = """```python
for i in range(10):
    print(i)
```"""

    text = """for i in range(10):
    print(i)"""

    entities = vegagram.types.List([vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.PRE, offset=0,
                                                                 length=32, language='python')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_blockquote():
    expected = """> Hello
> from

> vegagram!"""

    text = """Hello\nfrom\n\nvegagram!"""

    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.BLOCKQUOTE, offset=0, length=10),
         vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.BLOCKQUOTE, offset=12, length=9)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_mixed():
    expected = "**aaaaaaa__aaabbb**__~~dddddddd||ddeee~~||||eeeeeeefff||ffff`fffggggggg`ggghhhhhhhhhh"
    text = "aaaaaaaaaabbbddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh"
    entities = vegagram.types.List(
        [vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.BOLD, offset=0, length=13),
         vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.ITALIC, offset=7, length=6),
         vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.STRIKETHROUGH, offset=13, length=13),
         vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.SPOILER, offset=21, length=5),
         vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.SPOILER, offset=26, length=10),
         vegagram.types.MessageEntity(type=vegagram.enums.MessageEntityType.CODE, offset=40, length=10)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_no_entities():
    expected = "text"
    text = "text"
    entities = []

    assert Markdown.unparse(text=text, entities=entities) == expected
