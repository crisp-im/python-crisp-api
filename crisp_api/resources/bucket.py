##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class BucketResource(object):
  def __init__(self, parent):
    self.parent = parent

  @staticmethod
  def __url_bucket(resource):
    return f"/bucket{resource}"

  def generate_bucket_url(self, data):
    return self.parent.post(self.__url_bucket("/url/generate"), data)
