dns_op_codes = {
    # OpCode: ('Name', 'Reference'),
    0: ('Query', '[RFC1035]'),
    1: ('IQuery  (Inverse Query, OBSOLETE)', '[RFC3425]'),
    2: ('Status', '[RFC1035]'),
    # 3: ('Unassigned', ''),
    4: ('Notify', '[RFC1996]'),
    5: ('Update', '[RFC2136]'),
    6: ('DNS Stateful Operations (DSO)', '[RFC8490]'),
    # 7-15: ('Unassigned', ''),
}

OP_QUERY = 0
OP_IQUERY = 1
OP_STATUS = 2
OP_NOTIFY = 4
OP_UPDATE = 5
OP_DSO = 6
