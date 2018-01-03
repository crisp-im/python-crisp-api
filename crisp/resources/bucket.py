##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class BucketResource(object):
  def __init__(self, parent):
    self.parent = parent

  def generate_bucket_url(self, data):
    # TODO
