from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:nautobot_bgp_plugin:asn_list',
        link_text='AS Numbers',
        permissions=['nautobot_bgp_plugin.view_asn'],
        buttons=(
            PluginMenuButton(
                link='plugins:nautobot_bgp_plugin:asn_add',
                title='AS Numbers',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['nautobot_bgp_plugin.add_asn'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:nautobot_bgp_plugin:community_list',
        link_text='Communities',
        permissions=['nautobot_bgp_plugin.view_community'],
        buttons=(
            PluginMenuButton(
                link='plugins:nautobot_bgp_plugin:community_add',
                title='Communities',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['nautobot_bgp_plugin.add_community'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:nautobot_bgp_plugin:bgpsession_list',
        link_text='Sessions',
        permissions=['nautobot_bgp_plugin.view_bgpsession'],
        buttons=(
            PluginMenuButton(
                link='plugins:nautobot_bgp_plugin:bgpsession_add',
                title='Sessions',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['nautobot_bgp_plugin.add_bgpsession'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:nautobot_bgp_plugin:routingpolicy_list',
        link_text='Routing Policies',
        permissions=['nautobot_bgp_plugin.view_routingpolicy'],
        buttons=(
            PluginMenuButton(
                link='plugins:nautobot_bgp_plugin:routingpolicy_add',
                title='Routing Policies',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['nautobot_bgp_plugin.add_routingpolicy'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:nautobot_bgp_plugin:bgppeergroup_list',
        link_text='Peer Groups',
        permissions=['nautobot_bgp_plugin.view_bgppeergroup'],
        buttons=(
            PluginMenuButton(
                link='plugins:nautobot_bgp_plugin:bgppeergroup_add',
                title='Peer Groups',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['nautobot_bgp_plugin.add_bgppeergroup'],
            ),
        ),
    )
)
