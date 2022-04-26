# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
# from rest_framework.test import APIClient, APITestCase
from rest_framework.test import APIClient

from nautobot.users.models import Token

from nautobot.tenancy.models import Tenant
from nautobot.dcim.models import (
    Site,
    DeviceRole,
    DeviceType,
    Manufacturer,
    Device,
    Interface,
)
from nautobot.ipam.models import IPAddress

from nautobot_bgp_plugin.models import ASN, Community, BGPPeerGroup, BGPSession

User = get_user_model()


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")


class ASNTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.base_url_lookup = "plugins-api:nautobot_bgp_plugin-api:asn"
        self.asn1 = ASN.objects.create(number=65000, description="test_asn1")
        self.asn2 = ASN.objects.create(number=65001, description="test_asn2")
        self.tenant = Tenant.objects.create(name="tenant")

    def test_list_asn(self):
        url = reverse(f"{self.base_url_lookup}-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_get_asn(self):
        url = reverse(f"{self.base_url_lookup}-detail", kwargs={"pk": self.asn1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["number"], self.asn1.number)
        self.assertEqual(response.data["description"], self.asn1.description)

    def test_create_asn(self):
        url = reverse(f"{self.base_url_lookup}-list")
        data = {"number": 65002, "description": "test_asn3"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for key, value in data.items():
            self.assertEqual(response.data[key], value)

        asn = ASN.objects.get(pk=response.data["id"])
        self.assertEqual(asn.number, data["number"])
        self.assertEqual(asn.description, data["description"])

    def test_update_asn(self):
        url = reverse(f"{self.base_url_lookup}-detail", kwargs={"pk": self.asn1.pk})

        response = self.client.patch(url, {"number": 65004}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        asn = ASN.objects.get(pk=self.asn1.pk)
        self.assertEqual(asn.number, 65004)

        response = self.client.patch(url, {"number": 65005}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        asn = ASN.objects.get(pk=self.asn1.pk)
        self.assertEqual(asn.number, 65005)

    def test_delete_task(self):
        url = reverse(f"{self.base_url_lookup}-detail", kwargs={"pk": self.asn1.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(ASN.DoesNotExist):
            ASN.objects.get(pk=self.asn1.pk)

    def test_uniqueconstraint_asn(self):
        url = reverse(f"{self.base_url_lookup}-list")
        data = {"number": 65001, "description": "test_asn3"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {"number": 65001, "description": "test_asn3", "tenant": self.tenant.pk}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommunityTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.base_url_lookup = "plugins-api:nautobot_bgp_plugin-api:community"
        self.community1 = Community.objects.create(
            value="65000:65000", description="test_community"
        )

    def test_list_community(self):
        url = reverse(f"{self.base_url_lookup}-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_community(self):
        url = reverse(
            f"{self.base_url_lookup}-detail", kwargs={"pk": self.community1.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["value"], self.community1.value)
        self.assertEqual(response.data["description"], self.community1.description)

    def test_create_community(self):
        url = reverse(f"{self.base_url_lookup}-list")
        data = {"value": "65001:65001", "description": "test_community1"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Community.objects.get(pk=response.data["id"]).value, "65001:65001"
        )
        self.assertEqual(
            Community.objects.get(pk=response.data["id"]).description, "test_community1"
        )

    def test_update_community(self):
        pass

    def test_delete_community(self):
        pass


class PeerGroupTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.base_url_lookup = "plugins-api:nautobot_bgp_plugin-api:peergroup"
        self.peer_group = BGPPeerGroup.objects.create(
            name="peer_group", description="peer_group_description"
        )

    def test_list_peer_group(self):
        url = reverse(f"{self.base_url_lookup}-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_peer_group(self):
        url = reverse(
            f"{self.base_url_lookup}-detail", kwargs={"pk": self.peer_group.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.peer_group.name)
        self.assertEqual(response.data["description"], self.peer_group.description)

    def test_create_peer_group(self):
        url = reverse(f"{self.base_url_lookup}-list")
        data = {"name": "test_peer_group", "description": "peer_group_desc"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            BGPPeerGroup.objects.get(pk=response.data["id"]).name, "test_peer_group"
        )
        self.assertEqual(
            BGPPeerGroup.objects.get(pk=response.data["id"]).description,
            "peer_group_desc",
        )

    def test_update_peer_group(self):
        pass

    def test_delete_peer_group(self):
        pass


class SessionTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.base_url_lookup = "plugins-api:nautobot_bgp_plugin-api:session"
        site = Site.objects.create(name="test", slug="test")
        manufacturer = Manufacturer.objects.create(name="Juniper", slug="juniper")
        device_role = DeviceRole.objects.create(name="Firewall", slug="firewall")
        device_type = DeviceType.objects.create(
            slug="srx3600", model="SRX3600", manufacturer=manufacturer
        )
        self.device = Device.objects.create(
            device_type=device_type,
            name="device1",
            device_role=device_role,
            site=site,
        )
        intf = Interface.objects.create(name="test_intf", device=self.device)
        local_ip = IPAddress.objects.create(address="1.1.1.1/32")
        remote_ip = IPAddress.objects.create(address="2.2.2.2/32")
        self.local_ip = IPAddress.objects.create(address="3.3.3.3/32")
        self.remote_ip = IPAddress.objects.create(address="4.4.4.4/32")
        intf.ip_addresses.add(local_ip)
        self.device.save()
        self.local_as = ASN.objects.create(number=65000, description="local_as")
        self.remote_as = ASN.objects.create(number=65001, description="remote_as")
        local_as = ASN.objects.create(number=65002, description="local_as")
        remote_as = ASN.objects.create(number=65003, description="remote_as")
        self.peer_group = BGPPeerGroup.objects.create(
            name="peer_group", description="peer_group_description"
        )
        self.session = BGPSession.objects.create(
            name="session",
            description="session_descr",
            local_as=local_as,
            remote_as=remote_as,
            local_address=local_ip,
            remote_address=remote_ip,
            status="active",
            peer_group=self.peer_group,
        )

    def test_list_session(self):
        url = reverse(f"{self.base_url_lookup}-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_session(self):
        url = reverse(f"{self.base_url_lookup}-detail", kwargs={"pk": self.session.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.session.name)
        self.assertEqual(response.data["description"], self.session.description)
        self.assertEqual(
            response.data["local_as"]["number"], self.session.local_as.number
        )
        self.assertEqual(
            response.data["remote_as"]["number"], self.session.remote_as.number
        )
        self.assertEqual(
            response.data["local_address"]["address"],
            str(self.session.local_address.address),
        )
        self.assertEqual(
            response.data["remote_address"]["address"],
            str(self.session.remote_address.address),
        )
        self.assertEqual(response.data["status"]["value"], self.session.status)
        self.assertEqual(
            response.data["peer_group"]["name"], self.session.peer_group.name
        )
        self.assertEqual(
            response.data["peer_group"]["description"],
            self.session.peer_group.description,
        )

    def test_create_session(self):
        url = reverse(f"{self.base_url_lookup}-list")
        data = {
            "name": "test_session",
            "description": "session_descr",
            "local_as": self.local_as.pk,
            "remote_as": self.remote_as.pk,
            "local_address": self.local_ip.pk,
            "remote_address": self.remote_ip.pk,
            "status": "active",
            "device": self.device.pk,
            "peer_group": self.peer_group.pk,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            BGPSession.objects.get(pk=response.data["id"]).name, "test_session"
        )
        self.assertEqual(
            BGPSession.objects.get(pk=response.data["id"]).description, "session_descr"
        )
