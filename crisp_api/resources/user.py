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

  def get_user_availability(self):
    return self.parent.get(self.__url_user("/availability"))

  def update_user_availability(self, data):
    return self.parent.patch(self.__url_user("/availability"), data)

  def get_user_availability_status(self):
    return self.parent.get(self.__url_user("/availability/status"))

  def get_user_account(self):
    return self.parent.get(self.__url_user("/account"))

  def create_user_account(self, data):
    return self.parent.post(self.__url_user("/account"), data)

  def list_websites(self):
    return self.parent.get(self.__url_user("/account/websites"))

  def get_profile(self):
    return self.parent.get(self.__url_user("/account/profile"))

  def update_profile(self, data):
    return self.parent.patch(self.__url_user("/account/profile"), data)

  def check_session_validity(self):
    return self.parent.head(self.__url_user("/session"))

  def create_new_session(self, data):
    return self.parent.post(self.__url_user("/session/login"), data)

  def destroy_session(self):
    return self.parent.post(self.__url_user("/session/logout"))

  def count_total_unread_messages(self):
    return self.parent.get(self.__url_user("/stats/unread"))
