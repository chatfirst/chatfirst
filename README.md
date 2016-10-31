=======================
Chatfirst Python Client
=======================

Chatfirst Python Client provides simple interface to Chatfirst API (https://api.chatfirst.co). Typical usage
often looks like this::

    #!/usr/bin/env python

    from chatfirst.client import Chatfirst

    client = Chatfirst(your_chatfirst_user_token)
    my_bots = client.bots_list()

See more in documentation
