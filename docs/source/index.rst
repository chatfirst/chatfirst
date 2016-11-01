Welcome to Chatfirst Python Client's documentation!
===================================================

Chatfirst Python Client provides simple interface to `Chatfirst API <https://api.chatfirst.co/swagger>`_. Typical usage::

    #!/usr/bin/env python

    from chatfirst.client import Chatfirst

    client = Chatfirst(your_chatfirst_user_token)
    my_bots = client.bots_list()


Get the code
-------------

The `source <https://github.com/chatfirst/chatfirst>`_ is available on Github.

Contents:
---------

.. toctree::
   :maxdepth: 2

   client
   models

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

