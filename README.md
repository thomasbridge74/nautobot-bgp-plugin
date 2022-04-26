# Nautobot BGP Plugin
[Nautobot](https://github.com/nautobot/nautobot) plugin for BGP related objects documentation.

This is a fork of the original [Netbox Plugin](https://github.com/k01ek/netbox-bgp) at v0.3.9 - this was
the last version before the Nautobot fork from Netbox v2.10.4.     Later versions of the plugin are using
some of the newer Netbox features.

## Compatibility

I worked with Nautobot v1.2.11 - your mileage may vary!

## Installation

Install direct from the repo.    Not currently available through pypi.
```shell
pip install git+https://github.com/thomasbridge74/nautobot-bgp-plugin.git
```

## Docker image
I have forked [Nautobot Lab](https://github.com/thomasbridge74/nautobot-lab) and installed the
BGP Plugin into my fork.   I have also pushed it to Docker Hub.

This can be run as:
```shell
docker run -itd --name nautobot_bgp -p 8000:8000 thomasbridge/nautobot-bgp-lab
```

This is all added on an adhoc basis and in the hope it will be useful to some.

## Configuration

The following options are available:
* `device_ext_page`: String (default right) Device related BGP sessions table position. The following values are available:  
left, right, full_width. Set empty value for disable.

## Screenshots
