##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class RouteError(Exception):
  def __init__(self, error):
    super(RouteError, self).__init__(error)
