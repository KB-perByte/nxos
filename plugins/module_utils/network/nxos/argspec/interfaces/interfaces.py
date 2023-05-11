#
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""The arg spec for the nxos_interfaces module."""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class InterfacesArgs:  # pylint: disable=R0903
    """The arg spec for the nxos_interfaces module."""

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "elements": "dict",
            "options": {
                "description": {"type": "str"},
                "duplex": {"choices": ["full", "half", "auto"], "type": "str"},
                "enabled": {"type": "bool"},
                "fabric_forwarding_anycast_gateway": {"type": "bool"},
                "ip_forward": {"type": "bool"},
                "mode": {"choices": ["layer2", "layer3"], "type": "str"},
                "mtu": {"type": "str"},
                "name": {"required": True, "type": "str"},
                "speed": {"type": "str"},
            },
            "type": "list",
        },
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
                "purged",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
