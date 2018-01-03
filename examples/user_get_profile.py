##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

from crisp_api import Crisp

client = Crisp()

client.authenticate(
  "7c3ef21c-1e04-41ce-8c06-5605c346f73e",
  "cc29e1a5086e428fcc6a697d5837a66d82808e65c5cce006fbf2191ceea80a0a"
)

data = client.user.get_profile()

print(data)
