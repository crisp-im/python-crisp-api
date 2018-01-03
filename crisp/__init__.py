##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import json
from urllib import request, parse, error
from base64 import b64encode as b64

from .resources.bucket import BucketResource
from .resources.user import UserResource
from .resources.website import WebsiteResource

class Crisp(object):
  def __init__(self):
    self.__auth = {}

    self.__rest_host = None
    self.__rest_base_path = None
    self.__timeout = None

    self.bucket = BucketResource(self)
    self.user = UserResource(self)
    self.website = WebsiteResource(self)

  def authenticate(self, identifier, key):
    self.__auth["identifier"] = identifier
    self.__auth["key"] = key

  def get_rest_host(self):
    return self.__rest_host or "https://api.crisp.chat"

  def get_rest_base_path(self):
    return self.__rest_base_path or "/v1"

  def get_timeout(self):
    return self.__timeout or 5

  def set_rest_host(self, rest_host):
    self.__rest_host = rest_host

  def set_rest_base_path(self, rest_base_path):
    self.__rest_base_path = rest_base_path

  def set_timeout(self, timeout):
    self.__timeout = timeout

  def get(self, resource, query):
    return self.__do_get(resource, query)

  def __do_get(self, resource, query):
    url = "%s?%s" % (self.__prepare_rest_url(resource), parse.urlencode(query))

    headers = {
      "User-Agent": "python-crisp-api/1.0.0",
      "Authorization": self.__generate_auth()
    }

    req = request.Request(url, None, headers)

    try:
      with request.urlopen(req, None, self.get_timeout()) as response:
        data = response.read()
        raised_error = None
    except error.HTTPError as e:
      raised_error = e

    # Raise intercepted error?
    if raised_error:
      raise raised_error

    return json.loads(data) if data else None

  def __generate_auth(self):
    raw = "%s:%s" % (self.__auth["identifier"], self.__auth["key"])
    key = b64(raw.encode("ascii"))

    return "Basic %s" % key.decode("ascii")

  def __prepare_rest_url(self, resource):
    return self.get_rest_host() + self.get_rest_base_path() + resource
