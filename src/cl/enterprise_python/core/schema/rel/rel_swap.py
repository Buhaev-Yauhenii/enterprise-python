# Copyright (C) 2021-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mongoengine as me
from cl.enterprise_python.core.schema.rel.rel_leg import RelLeg
from cl.enterprise_python.core.schema.rel.rel_trade import RelTrade


class RelSwap(RelTrade):  # Inherits from RelTrade that has attributes common to all trades
    """Remaining attributes of swap record."""

    legs = me.ListField(me.EmbeddedDocumentField(RelLeg))
    """List of swap legs."""