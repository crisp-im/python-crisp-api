##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import json
from requests import request
from requests.auth import HTTPBasicAuth

from .errors.route import RouteError
from .resources.bucket import BucketResource
from .resources.user import UserResource
from .resources.website import WebsiteResource

class Crisp(object):
  REQUEST_HEADERS = {
    "User-Agent": "python-crisp-api/1.0.2",
    "Content-Type": "application/json"
  }

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

  def get(self, resource, query={}):
    return self.__do_request("GET", resource, query=query)

  def head(self, resource):
    return self.__do_request("HEAD", resource)

  def remove(self, resource):
    return self.__do_request("DELETE", resource)

  def post(self, resource, data={}):
    return self.__do_request("POST", resource, data=data)

  def patch(self, resource, data={}):
    return self.__do_request("PATCH", resource, data=data)

  def put(self, resource, data={}):
    return self.__do_request("PUT", resource, data=data)

  def __do_request(self, method, resource, query=None, data=None):
    auth = None

    if "identifier" in self.__auth and "key" in self.__auth:
      auth = HTTPBasicAuth(self.__auth["identifier"], self.__auth["key"])

    req = request(
      method,
      self.__prepare_rest_url(resource),
      timeout=self.get_timeout(),
      verify=True,
      headers=self.REQUEST_HEADERS,
      auth=auth,
      params=query,
      data=(json.dumps(data) if data != None else None)
    )

    result = req.json()

    if "error" in result and result["error"] is True:
      raise RouteError(result["reason"] if ("reason" in result) else "error")

    return result["data"] if "data" in result else {}

  def __prepare_rest_url(self, resource):
    return self.get_rest_host() + self.get_rest_base_path() + resource
