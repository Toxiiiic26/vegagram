Available Methods
=================

This page is about vegagram methods. All the methods listed here are bound to a :class:`~vegagram.Client` instance,
except for :meth:`~vegagram.idle()` and :meth:`~vegagram.compose()`, which are special functions that can be found in
the main package directly.

.. code-block:: python

    from vegagram import Client

    app = Client("my_account")

    with app:
        app.send_message("me", "hi")

-----

.. currentmodule:: vegagram.Client

Utilities
---------

.. autosummary::
    :nosignatures:

    {utilities}

.. toctree::
    :hidden:

    {utilities}

.. currentmodule:: vegagram

.. autosummary::
    :nosignatures:

    idle
    compose

.. toctree::
    :hidden:

    idle
    compose

.. currentmodule:: vegagram.Client

Messages
--------

.. autosummary::
    :nosignatures:

    {messages}

.. toctree::
    :hidden:

    {messages}

Chats
-----

.. autosummary::
    :nosignatures:

    {chats}

.. toctree::
    :hidden:

    {chats}

Users
-----

.. autosummary::
    :nosignatures:

    {users}

.. toctree::
    :hidden:

    {users}

Invite Links
------------

.. autosummary::
    :nosignatures:

    {invite_links}

.. toctree::
    :hidden:

    {invite_links}

Contacts
--------

.. autosummary::
    :nosignatures:

    {contacts}

.. toctree::
    :hidden:

    {contacts}

Password
--------

.. autosummary::
    :nosignatures:

    {password}

.. toctree::
    :hidden:

    {password}

Bots
----

.. autosummary::
    :nosignatures:

    {bots}

.. toctree::
    :hidden:

    {bots}

Authorization
-------------

.. autosummary::
    :nosignatures:

    {authorization}

.. toctree::
    :hidden:

    {authorization}

Stories
-------

.. autosummary::
    :nosignatures:

    {stories}

.. toctree::
    :hidden:

    {stories}

Premium
-------

.. autosummary::
    :nosignatures:

    {premium}

.. toctree::
    :hidden:

    {premium}

Phone
-----

.. autosummary::
    :nosignatures:

    {phone}

.. toctree::
    :hidden:

    {phone}

Business
--------

.. autosummary::
    :nosignatures:

    {business}

.. toctree::
    :hidden:

    {business}

Payments
--------

.. autosummary::
    :nosignatures:

    {payments}

.. toctree::
    :hidden:

    {payments}

Account
-------

.. autosummary::
    :nosignatures:

    {account}

.. toctree::
    :hidden:

    {account}

Advanced
--------

Methods used only when dealing with the raw Telegram API.
Learn more about how to use the raw API at :doc:`Advanced Usage <../../topics/advanced-usage>`.

.. autosummary::
    :nosignatures:

    {advanced}

.. toctree::
    :hidden:

    {advanced}
