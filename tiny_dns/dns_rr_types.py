dns_rr_types = {
    # Value: ('TYPE', 'Meaning'),
    1: ('A', 'a host address'),
    2: ('NS', 'an authoritative name server'),
    3: ('MD', 'a mail destination (OBSOLETE - use MX)'),
    4: ('MF', 'a mail forwarder (OBSOLETE - use MX)'),
    5: ('CNAME', 'the canonical name for an alias'),
    6: ('SOA', 'marks the start of a zone of authority'),
    7: ('MB', 'a mailbox domain name (EXPERIMENTAL)'),
    8: ('MG', 'a mail group member (EXPERIMENTAL)'),
    9: ('MR', 'a mail rename domain name (EXPERIMENTAL)'),
    10: ('NULL', 'a null RR (EXPERIMENTAL)'),
    11: ('WKS', 'a well known service description'),
    12: ('PTR', 'a domain name pointer'),
    13: ('HINFO', 'host information'),
    14: ('MINFO', 'mailbox or mail list information'),
    15: ('MX', 'mail exchange'),
    16: ('TXT', 'text strings'),
    17: ('RP', 'for Responsible Person'),
    18: ('AFSDB', 'for AFS Data Base location'),
    19: ('X25', 'for X.25 PSDN address'),
    20: ('ISDN', 'for ISDN address'),
    21: ('RT', 'for Route Through'),
    22: ('NSAP', 'for NSAP address, NSAP style A record'),
    23: ('NSAP-PTR', 'for domain name pointer, NSAP style'),
    24: ('SIG', 'for security signature'),
    25: ('KEY', 'for security key'),
    26: ('PX', 'X.400 mail mapping information'),
    27: ('GPOS', 'Geographical Position'),
    28: ('AAAA', 'IP6 Address'),
    29: ('LOC', 'Location Information'),
    30: ('NXT', 'Next Domain (OBSOLETE)'),
    31: ('EID', 'Endpoint Identifier'),
    32: ('NIMLOC', 'Nimrod Locator'),
    33: ('SRV', 'Server Selection'),
    34: ('ATMA', 'ATM Address'),
    35: ('NAPTR', 'Naming Authority Pointer'),
    36: ('KX', 'Key Exchanger'),
    37: ('CERT', 'CERT'),
    38: ('A6', 'A6 (OBSOLETE - use AAAA)'),
    39: ('DNAME', 'DNAME'),
    40: ('SINK', 'SINK'),
    41: ('OPT', 'OPT'),
    42: ('APL', 'APL'),
    43: ('DS', 'Delegation Signer'),
    44: ('SSHFP', 'SSH Key Fingerprint'),
    45: ('IPSECKEY', 'IPSECKEY'),
    46: ('RRSIG', 'RRSIG'),
    47: ('NSEC', 'NSEC'),
    48: ('DNSKEY', 'DNSKEY'),
    49: ('DHCID', 'DHCID'),
    50: ('NSEC3', 'NSEC3'),
    51: ('NSEC3PARAM', 'NSEC3PARAM'),
    52: ('TLSA', 'TLSA'),
    53: ('SMIMEA', 'S/MIME cert association'),
    # 54: ('Unassigned', ''),
    55: ('HIP', 'Host Identity Protocol'),
    56: ('NINFO', 'NINFO'),
    57: ('RKEY', 'RKEY'),
    58: ('TALINK', 'Trust Anchor LINK'),
    59: ('CDS', 'Child DS'),
    60: ('CDNSKEY', 'DNSKEY(s) the Child wants reflected in DS'),
    61: ('OPENPGPKEY', 'OpenPGP Key'),
    62: ('CSYNC', 'Child-To-Parent Synchronization'),
    63: ('ZONEMD', 'message digest for DNS zone'),
    # 64-98: ('Unassigned', ''),
    99: ('SPF', ''),
    100: ('UINFO', ''),
    101: ('UID', ''),
    102: ('GID', ''),
    103: ('UNSPEC', ''),
    104: ('NID', ''),
    105: ('L32', ''),
    106: ('L64', ''),
    107: ('LP', ''),
    108: ('EUI48', 'an EUI-48 address'),
    109: ('EUI64', 'an EUI-64 address'),
    # 110-248: ('Unassigned', ''),
    249: ('TKEY', 'Transaction Key'),
    250: ('TSIG', 'Transaction Signature'),
    251: ('IXFR', 'incremental transfer'),
    252: ('AXFR', 'transfer of an entire zone'),
    253: ('MAILB', 'mailbox-related RRs (MB, MG or MR)'),
    254: ('MAILA', 'mail agent RRs (OBSOLETE - see MX)'),
    255: ('*', 'A request for some or all records the server has available'),
    256: ('URI', 'URI'),
    257: ('CAA', 'Certification Authority Restriction'),
    258: ('AVC', 'Application Visibility and Control'),
    259: ('DOA', 'Digital Object Architecture'),
    260: ('AMTRELAY', 'Automatic Multicast Tunneling Relay'),
    # 261-32767: ('Unassigned', ''),
    32768: ('TA', 'DNSSEC Trust Authorities'),
    32769: ('DLV', 'DNSSEC Lookaside Validation (OBSOLETE)'),
    # 32770-65279: ('Unassigned', ''),
    # 65280-65534: ('Private use', ''),
    # 65535: ('Reserved', ''),
}

RR_A = 1
RR_NS = 2
RR_MD = 3
RR_MF = 4
RR_CNAME = 5
RR_SOA = 6
RR_MB = 7
RR_MG = 8
RR_MR = 9
RR_NULL = 10
RR_WKS = 11
RR_PTR = 12
RR_HINFO = 13
RR_MINFO = 14
RR_MX = 15
RR_TXT = 16
RR_RP = 17
RR_AFSDB = 18
RR_X25 = 19
RR_ISDN = 20
RR_RT = 21
RR_NSAP = 22
RR_NSAP_PTR = 23
RR_SIG = 24
RR_KEY = 25
RR_PX = 26
RR_GPOS = 27
RR_AAAA = 28
RR_LOC = 29
RR_NXT = 30
RR_EID = 31
RR_NIMLOC = 32
RR_SRV = 33
RR_ATMA = 34
RR_NAPTR = 35
RR_KX = 36
RR_CERT = 37
RR_A6 = 38
RR_DNAME = 39
RR_SINK = 40
RR_OPT = 41
RR_APL = 42
RR_DS = 43
RR_SSHFP = 44
RR_IPSECKEY = 45
RR_RRSIG = 46
RR_NSEC = 47
RR_DNSKEY = 48
RR_DHCID = 49
RR_NSEC3 = 50
RR_NSEC3PARAM = 51
RR_TLSA = 52
RR_SMIMEA = 53
RR_HIP = 55
RR_NINFO = 56
RR_RKEY = 57
RR_TALINK = 58
RR_CDS = 59
RR_CDNSKEY = 60
RR_OPENPGPKEY = 61
RR_CSYNC = 62
RR_ZONEMD = 63
RR_SPF = 99
RR_UINFO = 100
RR_UID = 101
RR_GID = 102
RR_UNSPEC = 103
RR_NID = 104
RR_L32 = 105
RR_L64 = 106
RR_LP = 107
RR_EUI48 = 108
RR_EUI64 = 109
RR_TKEY = 249
RR_TSIG = 250
RR_IXFR = 251
RR_AXFR = 252
RR_MAILB = 253
RR_MAILA = 254
RR_ANY = 255
RR_URI = 256
RR_CAA = 257
RR_AVC = 258
RR_DOA = 259
RR_AMTRELAY = 260
RR_TA = 32768
RR_DLV = 32769
