##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

from crisp_api import Crisp

client = Crisp()

client.authenticate(
  "13937834-f6ce-4556-ae4f-9e0c54faf038",
  "eb6c3623245521d7a6c35f5b29f3fa756e893f034ed551d84518961c5ff16dec"
)

data = client.user.get_profile()

print(data)
