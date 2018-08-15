##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class UserResource(object):
  def __init__(self, parent):
    self.parent = parent

  def __url_user(self, resource):
    return "/user%s" % resource

  def check_session_validity(self):
    return self.parent.head(self.__url_user("/session"))

  def create_new_session(self, data):
    return self.parent.post(self.__url_user("/session/login"), data)

  def destroy_session(self):
    return self.parent.post(self.__url_user("/session/logout"))
