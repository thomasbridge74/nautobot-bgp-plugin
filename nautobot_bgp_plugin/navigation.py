from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:nautobot_bgp_plugin:asn_list",
        link_text="AS Numbers",
        permissions=["nautobot_bgp_plugin.view_asn"],
        buttons=(
            PluginMenuButton(
                link="plugins:nautobot_bgp_plugin:asn_add",
                title="AS Numbers",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_bgp_plugin.add_asn"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:nautobot_bgp_plugin:community_list",
        link_text="Communities",
        permissions=["nautobot_bgp_plugin.view_community"],
        buttons=(
            PluginMenuButton(
                link="plugins:nautobot_bgp_plugin:community_add",
                title="Communities",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_bgp_plugin.add_community"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:nautobot_bgp_plugin:session_list",
        link_text="Sessions",
        permissions=["nautobot_bgp_plugin.view_session"],
        buttons=(
            PluginMenuButton(
                link="plugins:nautobot_bgp_plugin:session_add",
                title="Sessions",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_bgp_plugin.add_session"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:nautobot_bgp_plugin:routing_policy_list",
        link_text="Routing Policies",
        permissions=["nautobot_bgp_plugin.view_routing_policy"],
        buttons=(
            PluginMenuButton(
                link="plugins:nautobot_bgp_plugin:routing_policy_add",
                title="Routing Policies",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_bgp_plugin.add_routing_policy"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:nautobot_bgp_plugin:peergroup_list",
        link_text="Peer Groups",
        permissions=["nautobot_bgp_plugin.view_session"],
        buttons=(
            PluginMenuButton(
                link="plugins:nautobot_bgp_plugin:peergroup_add",
                title="Peer Groups",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_bgp_plugin.add_session"],
            ),
        ),
    ),
)
