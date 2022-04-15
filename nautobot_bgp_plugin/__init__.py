from nautobot.extras.plugins import PluginConfig
from .version import __version__


class BGPConfig(PluginConfig):
    name = "nautobot_bgp_plugin"
    verbose_name = "BGP"
    description = "Subsystem for tracking bgp related objects (forked from Netbox Plugin)"
    version = __version__
    author = "Thomas Bridge (forked from Nikolay Yuzefovich)"
    author_email = "thomas.bridge@icloud.com"
    base_url = "bgp"
    required_settings = []
    # min_version = "2.10.1"
    # max_version = "2.11.12"
    default_settings = {"device_ext_page": "right"}


config = BGPConfig  # noqa
