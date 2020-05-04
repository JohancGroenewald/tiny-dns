dns_classes = {
    # Decimal: ('Name', 'Reference'),
    # 0: ('Reserved', '[RFC6895]'),
    1: ('Internet (IN)', '[RFC1035]'),
    # 2: ('Unassigned', ''),
    3: ('Chaos (CH)', '[D. Moon, "Chaosnet", A.I. Memo 628, Massachusetts Institute ofTechnology Artificial Intelligence Laboratory, June 1981.]'),
    4: ('Hesiod (HS)', '[Dyer, S., and F. Hsu, "Hesiod", Project Athena TechnicalPlan - Name Service, April 1987.]'),
    # 5-253: ('Unassigned', ''),
    254: ('QCLASS NONE', '[RFC2136]'),
    255: ('QCLASS * (ANY)', '[RFC1035]'),
    # 256-65279: ('Unassigned', ''),
    # 65280-65534: ('Reserved for Private Use', '[RFC6895]'),
    # 65535: ('Reserved', '[RFC6895]'),
}

INTERNET_IN = 1
CHAOS_CH = 3
HESIOD_HS = 4
QCLASS_NONE = 254
QCLASS_ANY = 255
