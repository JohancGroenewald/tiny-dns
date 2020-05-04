dns_r_codes = {
    # RCODE: ('Name', 'Description'),
    0: ('NoError', 'No Error'),
    1: ('FormErr', 'Format Error'),
    2: ('ServFail', 'Server Failure'),
    3: ('NXDomain', 'Non-Existent Domain'),
    4: ('NotImp', 'Not Implemented'),
    5: ('Refused', 'Query Refused'),
    6: ('YXDomain', 'Name Exists when it should not'),
    7: ('YXRRSet', 'RR Set Exists when it should not'),
    8: ('NXRRSet', 'RR Set that should exist does not'),
    9: ('NotAuth', 'Server Not Authoritative for zone'),
    # 9: ('NotAuth', 'Not Authorized'),
    10: ('NotZone', 'Name not contained in zone'),
    11: ('DSOTYPENI', 'DSO-TYPE Not Implemented'),
    # 12-15: ('Unassigned', ''),
    16: ('BADVERS', 'Bad OPT Version'),
    # 16: ('BADSIG', 'TSIG Signature Failure'),
    17: ('BADKEY', 'Key not recognized'),
    18: ('BADTIME', 'Signature out of time window'),
    19: ('BADMODE', 'Bad TKEY Mode'),
    20: ('BADNAME', 'Duplicate key name'),
    21: ('BADALG', 'Algorithm not supported'),
    22: ('BADTRUNC', 'Bad Truncation'),
    23: ('BADCOOKIE', 'Bad/missing Server Cookie'),
    # 24-3840: ('Unassigned', ''),
    # 3841-4095: ('Reserved for Private Use', ''),
    # 4096-65534: ('Unassigned', ''),
    # 65535: ('Reserved, can be allocated by Standards Action', ''),
}

R_NOERROR = 0
R_FORMERR = 1
R_SERVFAIL = 2
R_NXDOMAIN = 3
R_NOTIMP = 4
R_REFUSED = 5
R_YXDOMAIN = 6
R_YXRRSET = 7
R_NXRRSET = 8
R_NOTAUTH = 9
R_NOTZONE = 10
R_DSOTYPENI = 11
R_BADVERS = 16
R_BADKEY = 17
R_BADTIME = 18
R_BADMODE = 19
R_BADNAME = 20
R_BADALG = 21
R_BADTRUNC = 22
R_BADCOOKIE = 23
