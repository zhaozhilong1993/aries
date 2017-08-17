#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""quota endpoint for King v1 REST API."""
import json
import six
from webob import exc

from king.common.i18n import _

from king.api.openstack.v1 import util
from king.common import serializers
from king.common import service_utils
from king.common import wsgi

from oslo_log import log as logging


LOG = logging.getLogger(__name__)


class AccountController(object):
    """WSGI controller for account resource in King v1 API.

    Implements the API actions.
    """
    # Define request scope (must match what is in policy.json)
    REQUEST_SCOPE = 'account'

    def __init__(self, options):
        self.options = options

    @util.policy_enforce
    def create(self, req, body):
        pass

    @util.policy_enforce
    def list(self, req, body):
        pass

    @util.policy_enforce
    def update(self, req, body):
        pass


def create_resource(options):
    """account resource factory method."""
    deserializer = wsgi.JSONRequestDeserializer()
    serializer = serializers.JSONResponseSerializer()
    return wsgi.Resource(AccountController(options), deserializer, serializer)
