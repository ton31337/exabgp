#!/usr/bin/env python3
# encoding: utf-8
"""
decode.py

Created by Thomas Mangin on 2009-09-06.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
License: 3-clause BSD. (See the COPYRIGHT file)
"""

# pylint: ignore=E131
# pylama:ignore=E131

import sys

# INET include is required as it perform some AFI/SAFI registration
from exabgp.bgp.message.update.nlri import INET  # noqa

from exabgp.bgp.message.open.routerid import RouterID
from exabgp.protocol.ip import IPv4
from exabgp.bgp.message.open.asn import ASN
from exabgp.bgp.message.open.holdtime import HoldTime

from exabgp.bgp.message import Update
from exabgp.bgp.message import Open
from exabgp.bgp.message.open import Version
from exabgp.bgp.message.open import ASN
from exabgp.bgp.message.open import RouterID
from exabgp.bgp.message.open import HoldTime
from exabgp.bgp.message.open.capability import Capabilities
from exabgp.bgp.message.open.capability import Capability
from exabgp.bgp.message.open.capability import Negotiated
from exabgp.bgp.message.update.nlri import NLRI

from exabgp.bgp.message.direction import Direction

from exabgp.logger import log
from exabgp.environment import getenv

log.init(getenv())


bodies = []

# fmt: off
body = [
    0x0, 0x0,  # len withdrawn routes
    # No routes to remove
    # Attributes
    0x0, 0x30,  # len attributes (48)
        0x40,  # Flag Transitive
        0x1,  # Code : Attribute ID Origin
        0x1,  # len
            0x0,  # Origin : IGP
        0x50,  # Flag Transitive + extended length
        0x2,  # Code : AS Path
        0x0, 0x16,  # len 22
            0x2,  # Type (AS_Sequence)
            0x5,  # length (in ASes as every asn is 0x0 0x0 prefixed ASN4 must have been negotiated)
                0x0, 0x0, 0xfe, 0xb0,  # ASN 65200
                0x0, 0x0, 0x78, 0x14,  # ASN 30740
                0x0, 0x0, 0x19, 0x35,  # ASN 6453
                0x0, 0x0, 0xb, 0x62,  # ASN 2914
                0x0, 0x0, 0x9, 0xd7,  # ASN 2519
        0x40,  # Flag Transitive
        0x3,  # Code: Next HOP
        0x4,  # len
            0x7f, 0x0, 0x0, 0x1,  # 127.0.0.1
        0xc0,  # 0x40 + 0x80 (Transitive Optional)
        0x08,  # Community
        0x8,  # Size 8
            0x78, 0x14, 0x19, 0x35,  # 30740:6453
            0x78, 0x14, 0xfd, 0xeb,  # 30740:65003
    # routes :
        0x18, 0x1, 0x0, 0x19,  # 1.0.25.0/24
        0x10, 0xde, 0xe6,  # 222.330.0.0/16
        0x11, 0xde, 0xe5, 0x80,
        0x12, 0xde, 0xe5, 0x0,
        0x10, 0xde, 0xe4,
        0x11, 0xdc, 0xf7, 0x0,
        0x11, 0xdc, 0x9e, 0x0,
        0x18, 0xdb, 0x79, 0xff,
        0x18, 0xdb, 0x79, 0xf9,
        0x16, 0xd8, 0xb3, 0xcc,
        0x18, 0xd8, 0xb3, 0xb6,
        0x17, 0xd8, 0xb3, 0xb4,
        0x16, 0xd8, 0xb3, 0xb0,
        0x18, 0xd8, 0xb3, 0x99,
        0x12, 0xd2, 0xaa, 0x0,
        0x11, 0xd2, 0x92, 0x80,
        0x11, 0xd2, 0x83, 0x80,
        0x13, 0xcb, 0x8c, 0x20,
        0x18, 0xca, 0xf5, 0xfe,
        0x18, 0xca, 0xf5, 0x8e,
        0x18, 0xca, 0xf3, 0xba,
        0x18, 0xca, 0xf0, 0x8d,
        0x12, 0xca, 0xef, 0xc0,
        0x12, 0xca, 0xe7, 0x40,
        0x10, 0xca, 0xd7,
        0x18, 0xca, 0xd2, 0x8,
        0x13, 0xca, 0xbd, 0xc0,
        0x14, 0xca, 0x58, 0x30,
        0x18, 0xca, 0x22, 0xbf,
        0x17, 0xca, 0x22, 0x96,
        0x18, 0xc0, 0x32, 0x6e,
        0x10, 0xb7, 0xb4,
        0x11, 0xb7, 0xb1, 0x80,
        0x10, 0xa3, 0x8b,
        0x11, 0x9d, 0x78, 0x80,
        0x15, 0x7c, 0xf1, 0x78,
        0x10, 0x7c, 0x6e,
        0x10, 0x7a, 0x67,
        0x10, 0x78, 0x33,
        0x10, 0x74, 0x5b,
        0x15, 0x73, 0xbb, 0x48,
        0x16, 0x73, 0xbb, 0x44,
        0x10, 0x73, 0xb3,
        0x11, 0x72, 0x45, 0x0,
        0x14, 0x71, 0x34, 0xf0,
        0x15, 0x70, 0x6d, 0x18,
        0x18, 0x67, 0xf6, 0xb3,
        0x17, 0x67, 0xb, 0x6,
        0x18, 0x67, 0x5, 0x75,
        0x18, 0x67, 0x5, 0x74,
        0x18, 0x67, 0x3, 0x10,
        0x13, 0x65, 0x37, 0xc0,
        0x11, 0x65, 0x32, 0x80,
        0x18, 0x65, 0x0, 0x1f,
        0x18, 0x65, 0x0, 0x1e,
        0x18, 0x65, 0x0, 0x1d,
        0x18, 0x65, 0x0, 0x1c,
        0xf, 0x24, 0x2,
        0x11, 0x1b, 0x79, 0x80,
        0x13, 0x1b, 0x60, 0x20,
        0x15, 0x1b, 0x60, 0x10,
        0x10, 0x1, 0x15,
        0x16, 0x1, 0x0, 0x1c,
        0x17, 0x1, 0x0, 0x1a
]

# asn4, data
bodies.append((True,body))

body = [
    0x0, 0x0,
    0x0, 0x38,
    0x40,
        0x1,
        0x1,
            0x0,
    0x50,
        0x2,
        0x0, 0x12,
            0x2,
            0x4,
                0x0, 0x0, 0xc7, 0x9d,
                0x0, 0x0, 0x9b, 0xbd,
                0x0, 0x0, 0xb, 0x62,
                0x0, 0x0, 0x9, 0xd7,
    0x40,
        0x3,
        0x4,
            0xb2, 0xd9, 0x76, 0x1,
    0xc0,
        0x8,
        0x14,
            0xb, 0x62, 0x1, 0x9a,
            0xb, 0x62, 0x5, 0x7b,
            0xb, 0x62, 0x9, 0x61,
            0xb, 0x62, 0xd, 0x48,
            0x9b, 0xbd, 0x1d, 0x1a,
    0x18, 0x1, 0x0, 0x19,
    0x10, 0xde, 0xe6,
    0x11, 0xde, 0xe5, 0x80,
    0x12, 0xde, 0xe5, 0x0,
    0x18, 0xdb, 0x79, 0xff,
    0x18, 0xdb, 0x79, 0xf9,
    0x16, 0xd8, 0xb3, 0xcc,
    0x18, 0xd8, 0xb3, 0xb6,
    0x17, 0xd8, 0xb3, 0xb4,
    0x16, 0xd8, 0xb3, 0xb0,
    0x18, 0xd8, 0xb3, 0x99,
    0x12, 0xd2, 0xaa, 0x0,
    0x11, 0xd2, 0x92, 0x80,
    0x11, 0xd2, 0x83, 0x80,
    0x13, 0xcb, 0x8c, 0x20,
    0x18, 0xca, 0xf5, 0xfe,
    0x18, 0xca, 0xf5, 0x8e,
    0x18, 0xca, 0xf3, 0xba,
    0x18, 0xca, 0xf0, 0x8d,
    0x12, 0xca, 0xef, 0xc0,
    0x12, 0xca, 0xe7, 0x40,
    0x18, 0xca, 0xd2, 0x8,
    0x13, 0xca, 0xbd, 0xc0,
    0x14, 0xca, 0x58, 0x30,
    0x18, 0xca, 0x22, 0xbf,
    0x17, 0xca, 0x22, 0x96,
    0x18, 0xc0, 0x32, 0x6e,
    0x10, 0xb7, 0xb4,
    0x11, 0x9d, 0x78, 0x80,
    0x15, 0x7c, 0xf1, 0x78,
    0x10, 0x7a, 0x67,
    0x15, 0x73, 0xbb, 0x48,
    0x16, 0x73, 0xbb, 0x44,
    0x11, 0x72, 0x45, 0x0,
    0x14, 0x71, 0x34, 0xf0,
    0x15, 0x70, 0x6d, 0x18,
    0x18, 0x67, 0xf6, 0xb3,
    0x17, 0x67, 0xb, 0x6,
    0x18, 0x67, 0x5, 0x75,
    0x18, 0x67, 0x5, 0x74,
    0x18, 0x67, 0x3, 0x10,
    0x13, 0x65, 0x37, 0xc0,
    0x11, 0x65, 0x32, 0x80,
    0x18, 0x65, 0x0, 0x1f,
    0x18, 0x65, 0x0, 0x1e,
    0x18, 0x65, 0x0, 0x1d,
    0x18, 0x65, 0x0, 0x1c,
    0xf, 0x24, 0x2,
    0x11, 0x1b, 0x79, 0x80,
    0x13, 0x1b, 0x60, 0x20,
    0x15, 0x1b, 0x60, 0x10,
    0x10, 0x1, 0x15,
    0x16, 0x1, 0x0, 0x1c,
    0x17, 0x1, 0x0, 0x1a
]
# asn4, data
bodies.append((True,body))

# BGP-LS with draft-gredler-idr-bgp-ls-segment-routing-ext
body = [0x00, 0x00, # withdrawn routes length 0
        0x00, 0xdc,    # Path Attribute Length 220
        0x90, 0x0e,
        0x00, 0x62,
        0x40, 0x04, 0x47, 0x04,
        0xac, 0x18, 0xf8, 0x4f,
        0x00, 0x00, 0x02, 0x00,
        0x55, 0x02, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x01, 0x00,
        0x00, 0x1a, 0x02, 0x00,
        0x00, 0x04, 0x00, 0x00,
        0xfd, 0xe8, 0x02, 0x01,
        0x00, 0x04, 0xac, 0x10,
        0x00, 0x58, 0x02, 0x03,
        0x00, 0x06, 0x17, 0x20,
        0x00, 0x16, 0x00, 0x02,
        0x01, 0x01, 0x00, 0x1a,
        0x02, 0x00, 0x00, 0x04,
        0x00, 0x00, 0xfd, 0xe8,
        0x02, 0x01, 0x00, 0x04,
        0xac, 0x10, 0x00, 0x58,
        0x02, 0x03, 0x00, 0x06,
        0x17, 0x20, 0x00, 0x16,
        0x00, 0x01, 0x01, 0x03,
        0x00, 0x04, 0x0a, 0x00,
        0x00, 0x07, 0x01, 0x04,
        0x00, 0x04, 0x0a, 0x00,
        0x00, 0x06, 0x40, 0x01,
        0x01, 0x00, 0x40, 0x02,
        0x06, 0x02, 0x01, 0x00,
        0x00, 0xfd, 0xe8,
        0x80, 0x1d,             # Link State Attribute Code 29
        0x66,                      # Length
        0x04, 0x04, 0x00, 0x04, # Type 1028, Length 4
        0xac, 0x10, 0x00, 0x02, # IPv4 Router-ID 172.16.0.2
        0x04, 0x06,               # Type 1030
        0x00, 0x04,
        0xac, 0x10, 0x00, 0x01, # IPv4 Router ID 172.16.0.1
        0x04, 0x40,                # Type 1088
        0x00, 0x04,
        0x00, 0x00, 0x00, 0x00, # SRLG = 0
        0x04, 0x41,                # Type 1089
        0x00, 0x04,
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Maximum Link bandwidth
        0x04, 0x42,                # Type 1090
        0x00, 0x04,
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Maximum reservable link bandwidth
        0x04, 0x43,                # Type 1091
        0x00, 0x20,
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P0
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P1
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P2
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P3
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P4
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P5
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P6
        0x4c, 0xee, 0x6b, 0x28, # 1000.00 Mbps Unreserved Bandwidth P7
        0x04, 0x44,                # Type 1092
        0x00, 0x04,                # Length 4
        0x00, 0x00, 0x00, 0x0a, # 10
        0x04, 0x47,                # Type 1095 Metric TLV
        0x00, 0x03,                # Length 3
        0x00, 0x00, 0x0a,        # 10
        0x04, 0x4b,                # Type 1099 Adjacency Segment TLV
        0x00, 0x07,                # Length 7
        0x30,                    # Flags  0011 0000
        0x00,                    # Weigth 0
        0x00, 0x00,                # Reserved 0x0
        0x04, 0x93, 0x1e]        # SID/Label 299806
# fmt: on

# asn4, data
bodies.append((True, body))


class FakeNeighbor(dict):
    def __init__(self):
        self.update({
            'description': 'a test neighbor',
            'router-id': RouterID('127.0.0.1'),
            'local-address': IPv4('127.0.0.1'),
            'peer-address': IPv4('127.0.0.1'),
            'host-name': 'localhost',
            'domain-name': 'localdomain',
            'peer-as': ASN('65500'),
            'local-as': ASN('65500'),
            'hold-time': HoldTime(180),
            'capability': {
                'asn4': False,
                'add-path': 0,
                'extended_message': False,
                'nexthop': None,
                'route-refresh': False,
                'graceful-restart': False,
                'multi-session': None,
                'add-path': None,
                'aigp': None,
                'operational': None,
                'extended-message': True,
                'software-version': False,
             },
        })

    @staticmethod
    def families():
        return NLRI.known_families()

import unittest

# from contextlib import contextmanager
# @contextmanager
# def change_cwd (directory):
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     new_dir = os.path.join(current_dir, directory)
#     old_cwd = os.getcwd()
#     os.chdir(new_dir)
#     try:
#         yield
#     finally:
#         os.chdir(old_cwd)


class TestUpdateDecoding(unittest.TestCase):
    def setUp(self):
        self.negotiated = {}

        for asn4 in (True, False):
            neighbor = FakeNeighbor()
            neighbor.asn4 = asn4

            capa = Capabilities().new(neighbor, False)
            capa[Capability.CODE.MULTIPROTOCOL] = neighbor.families()

            # path = {}
            # for f in NLRI.known_families():
            #     if neighbor.add_path:
            #         path[f] = neighbor.add_path
            # capa[Capability.CODE.ADD_PATH] = path

            routerid_1 = str(neighbor['router-id'])
            routerid_2 = '.'.join(str((int(_) + 1) % 250) for _ in str(neighbor['router-id']).split('.', -1))

            o1 = Open(Version(4), ASN(neighbor['local-as']), HoldTime(180), RouterID(routerid_1), capa)
            o2 = Open(Version(4), ASN(neighbor['peer-as']), HoldTime(180), RouterID(routerid_2), capa)

            negotiated = Negotiated(neighbor)
            negotiated.sent(o1)
            negotiated.received(o2)

            self.negotiated[asn4] = negotiated

    # size = len(body)+19
    # header = [0xFF,]*16 + [size >> 8] + [size & 0xFF] + [0x02]
    # print ''.join('%02X' % _ for _ in header+body

    def test_decoding_udpate_asn(self):
        for asn4, body in bodies:
            if asn4:
                continue
            Update.unpack_message(bytes(body), Direction.IN, self.negotiated[asn4])

    def test_decoding_udpate_asn4(self):
        for asn4, body in bodies:
            if not asn4:
                continue
            Update.unpack_message(bytes(body), Direction.IN, self.negotiated[asn4])


if __name__ == '__main__':
    unittest.main()
