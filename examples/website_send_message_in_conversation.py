##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import sys
sys.path.append('..')
from crisp import Crisp

client = Crisp()

client.authenticate(
  "13937834-f6ce-4556-ae4f-9e0c54faf038",
  "eb6c3623245521d7a6c35f5b29f3fa756e893f034ed551d84518961c5ff16dec"
)

# Message routing details
website_id = "88972681-a00c-4b3b-a383-cab281636484"
session_id = "session_9df2a21e-f113-41d4-8ed2-bad8b49cafd1"

data = client.website.send_message_in_conversation(
  website_id, session_id,

  {
    "type": "text",
    "content": "This message was sent from python-crisp-api! :)",
    "from": "operator",
    "origin": "chat"
  }
)

print(data)
