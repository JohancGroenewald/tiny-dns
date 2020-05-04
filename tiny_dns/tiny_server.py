import socket

from tiny_dns.dindings import ORGANISATION, BINDINGS
import tiny_dns.dns_classes as dns_classes
import tiny_dns.dns_op_codes as dns_op_codes
import tiny_dns.dns_r_codes as dns_r_codes
import tiny_dns.dns_rr_types as dns_rr_types

UDP_IP = "0.0.0.0"
UDP_SOCKET = 53
MAX_BUFFER_SIZE = 512

GATEWAY_DNS_SERVER = '192.168.0.1'
OPEN_DNS_SERVER = '208.67.222.222'
GOOGLE_DNS_SERVER = '8.8.8.8'

PASS_THROUGH_DNS_SERVER_IP = GATEWAY_DNS_SERVER

DEFAULT_TTL = 60

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connection.bind((UDP_IP, UDP_SOCKET))


class Message():

    def __init__(self):
        self.index = 0

    def start(self, offset=0, increment=0):
        self.index += increment
        return self.index + offset

    def stop(self, offset=0, increment=0):
        self.index += increment
        return self.index + offset

    def inc(self, value):
        self.index += value

    @staticmethod
    def dump(index, data):
        print(''.join([f'[{b:02X}' if i == index else f' {b:02X}' for i, b in enumerate(data)]))


class Header():
    """
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    """

    QUERY = 0
    RESPONSE = 1
    NON_AUTHORITATIVE = 0
    AUTHORITATIVE = 1
    RESERVED = 0

    def __init__(self):

        self.ID = None
        self.QR = None
        self.Opcode = None
        self.AA = None
        self.TC = None
        self.RD = None
        self.RA = None
        self.Z = None
        self.RCODE = None
        self.QDCOUNT = None
        self.ANCOUNT = None
        self.NSCOUNT = None
        self.ARCOUNT = None
        self.start = None
        self.stop = None

    def loads(self, message, data):
        self.start = message.start()

        """
        ID              A 16 bit identifier assigned by the program that
                        generates any kind of query.  This identifier is copied
                        the corresponding reply and can be used by the requester
                        to match up replies to outstanding queries.
        """
        # Message.dump(message.start(), data)
        self.ID = data[message.start():message.stop(increment=2)]
        """
        QR              A one bit field that specifies whether this message is a
                        query (0), or a response (1).
        """
        self.QR = (data[message.start()] & 0b10000000) == 0b10000000
        # Message.dump(message.start(), data)
        """
        OPCODE          A four bit field that specifies kind of query in this
                        message.  This value is set by the originator of a query
                        and copied into the response.  The values are:
        
                        0               a standard query (QUERY)
        
                        1               an inverse query (IQUERY)
        
                        2               a server status request (STATUS)
        
                        3-15            reserved for future use
        """
        self.OPCODE = (data[message.start()] & 0b01111000) >> 3
        # Message.dump(message.start(), data)
        """
        AA              Authoritative Answer - this bit is valid in responses,
                        and specifies that the responding name server is an
                        authority for the domain name in question section.
                        
                        Note that the contents of the answer section may have
                        multiple owner names because of aliases.  The AA bit
                        corresponds to the name which matches the query name, or
                        the first owner name in the answer section.
        """
        # Message.dump(message.start(), data)
        self.AA = (data[message.start()] & 0b00000100) == 0b00000100
        """
        TC              TrunCation - specifies that this message was truncated
                        due to length greater than that permitted on the
                        transmission channel.
        """
        # Message.dump(message.start(), data)
        self.TC = (data[message.start()] & 0b00000010) == 0b00000010
        """
        RD              Recursion Desired - this bit may be set in a query and
                        is copied into the response.  If RD is set, it directs
                        the name server to pursue the query recursively.
                        Recursive query support is optional.
        """
        # Message.dump(message.start(), data)
        self.RD = (data[message.start()] & 0b00000001) == 0b00000001
        """
        RA              Recursion Available - this be is set or cleared in a
                        response, and denotes whether recursive query support is
                        available in the name server.
        """
        # Message.dump(message.start(), data)
        self.RA = (data[message.start(increment=1)] & 0b10000000) == 0b10000000
        """
        Z               Reserved for future use.  Must be zero in all queries
                        and responses.
        """
        # Message.dump(message.start(), data)
        self.Z = (data[message.start()] & 0b01110000) >> 4
        """
        RCODE           Response code - this 4 bit field is set as part of
                        responses.  The values have the following
                        interpretation:

                        0               No error condition
        
                        1               Format error - The name server was
                                        unable to interpret the query.
        
                        2               Server failure - The name server was
                                        unable to process this query due to a
                                        problem with the name server.
        
                        3               Name Error - Meaningful only for
                                        responses from an authoritative name
                                        server, this code signifies that the
                                        domain name referenced in the query does
                                        not exist.
        
                        4               Not Implemented - The name server does
                                        not support the requested kind of query.
        
                        5               Refused - The name server refuses to
                                        perform the specified operation for
                                        policy reasons.  For example, a name
                                        server may not wish to provide the
                                        information to the particular requester,
                                        or a name server may not wish to perform
                                        a particular operation (e.g., zone
                                        transfer) for particular data.
                        
                        6-15            Reserved for future use.
        """
        # Message.dump(message.start(), data)
        self.RCODE = data[message.start()] & 0b00001111
        """
        QDCOUNT         an unsigned 16 bit integer specifying the number of
                        entries in the question section.
        """
        self.QDCOUNT = int.from_bytes(
            data[message.start(increment=1):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        """
        ANCOUNT         an unsigned 16 bit integer specifying the number of
                        resource records in the answer section.
        """
        self.ANCOUNT = int.from_bytes(
            data[message.start(increment=2):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        """
        NSCOUNT         an unsigned 16 bit integer specifying the number of name
                        server resource records in the authority records
                        section.
        """
        self.NSCOUNT = int.from_bytes(
            data[message.start(increment=2):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        """
        ARCOUNT         an unsigned 16 bit integer specifying the number of
                        resource records in the additional records section.
        """
        self.ARCOUNT = int.from_bytes(
            data[message.start(increment=2):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)

        # Move the index past the end of the header data block
        message.inc(2)

        self.stop = message.start()
        return self

    def load(self, ID, QR, Opcode, AA, TC, RD, RA, Z, RCODE, QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT):
        self.ID = ID
        self.QR = QR
        self.Opcode = Opcode
        self.AA = AA
        self.TC = TC
        self.RD = RD
        self.RA = RA
        self.Z = Z
        self.RCODE = RCODE
        self.QDCOUNT = QDCOUNT
        self.ANCOUNT = ANCOUNT
        self.NSCOUNT = NSCOUNT
        self.ARCOUNT = ARCOUNT
        return self

    def dumps(self, buffer):
        buffer.extend(self.ID)
        buffer.append(0b00000000)
        if self.QR:
            buffer[-1] |= 0b10000000
        if self.OPCODE:
            value = self.OPCODE << 3
            buffer[-1] |= value
        if self.AA:
            buffer[-1] |= 0b00000100
        if self.TC:
            buffer[-1] |= 0b00000010
        if self.RD:
            buffer[-1] |= 0b00000001
        buffer.append(0b00000000)
        if self.RA:
            buffer[-1] |= 0b10000000
        if self.Z:
            value = self.Z << 4
            buffer[-1] |= value
        if self.RCODE:
            value = self.RCODE & 0b00001111
            buffer[-1] |= value
        buffer.extend(self.QDCOUNT.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.ANCOUNT.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.NSCOUNT.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.ARCOUNT.to_bytes(2, byteorder='big', signed=False))
        return buffer

    def slice(self, data):
        return data[self.start:self.stop]

    def __eq__(self, other):
        return (
            self.ID      == other.ID      and
            self.QR      == other.QR      and
            self.Opcode  == other.Opcode  and
            self.AA      == other.AA      and
            self.TC      == other.TC      and
            self.RD      == other.RD      and
            self.RA      == other.RA      and
            self.Z       == other.Z       and
            self.RCODE   == other.RCODE   and
            self.QDCOUNT == other.QDCOUNT and
            self.ANCOUNT == other.ANCOUNT and
            self.NSCOUNT == other.NSCOUNT and
            self.ARCOUNT == other.ARCOUNT
        )

    def __repr__(self):
        buffer = [
            f"ID={''.join([format(_byte, '02X') for _byte in self.ID])}",
            f'QR={self.QR}',
            f"OPCODE={dns_op_codes.dns_op_codes.get(self.OPCODE, 'Unassigned')}",
            f'AA={self.AA}',
            f'TC={self.TC}',
            f'RD={self.RD}',
            f'RA={self.RA}',
            f'Z={self.Z}',
            f"RCODE={dns_r_codes.dns_r_codes.get(self.RCODE, 'Unassigned')}",
            f'QDCOUNT={self.QDCOUNT}',
            f'ANCOUNT={self.ANCOUNT}',
            f'NSCOUNT={self.NSCOUNT}',
            f'ARCOUNT={self.ARCOUNT}',
        ]
        return f'Header({",".join(buffer)})'


class Question():
    """
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                     QNAME                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     QTYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     QCLASS                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    """

    def __init__(self):
        self.QNAME = None   # An array of URL components
        self.QTYPE = None
        self.QCLASS = None
        self.start = None
        self.stop = None

    def loads(self, message, data):
        self.start = message.start()

        """
        QNAME           a domain name represented as a sequence of labels, where
                        each label consists of a length octet followed by that
                        number of octets.  The domain name terminates with the
                        zero length octet for the null label of the root.  Note
                        that this field may be an odd number of octets; no
                        padding is used.
        """
        self.QNAME = []
        while True:
            length = data[message.start()]
            if 1 <= length <= 255:
                qname = data[message.start(increment=1):message.stop(offset=length)].decode('ascii')
                self.QNAME.append(qname.lower())
                message.inc(length)
            else:
                break
        """
        QTYPE           a two octet code which specifies the type of the query.
                        The values for this field include all codes valid for a
                        TYPE field, together with some more general codes which
                        can match more than one type of RR.
        """
        self.QTYPE = int.from_bytes(
            data[message.start(increment=1):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        """
        QCLASS          a two octet code that specifies the class of the query.
                        For example, the QCLASS field is IN for the Internet.
        """
        self.QCLASS = int.from_bytes(
            data[message.start(increment=2):message.start(offset=2)],
            byteorder='big',
            signed=False
        )

        # Move the index past the end of the question data block
        message.inc(2)

        self.stop = message.start()
        return self

    def load(self, QNAME, QTYPE, QCLASS):
        self.QNAME = QNAME
        self.QTYPE = QTYPE
        self.QCLASS = QCLASS
        return self

    def dumps(self, buffer):
        for name in self.QNAME:
            buffer.append(len(name))
            buffer.extend(bytes(name, 'ascii'))
        buffer.append(0b00000000)
        buffer.extend(self.QTYPE.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.QCLASS.to_bytes(2, byteorder='big', signed=False))
        return buffer

    def slice(self, data):
        return data[self.start:self.stop]

    def __eq__(self, other):
        return (
            self.QNAME  == other.QNAME  and
            self.QTYPE  == other.QTYPE  and
            self.QCLASS == other.QCLASS
        )

    def __repr__(self):
        buffer = [
            f'QNAME={self.QNAME}',
            f"QTYPE={dns_rr_types.dns_rr_types.get(self.QTYPE, 'Unassigned')}",
            f"QCLASS={dns_classes.dns_classes.get(self.QCLASS, 'Unassigned')}"
        ]
        return f'Question({",".join(buffer)})'


class ResourceRecord():
    """
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                                               /
    /                      NAME                     /
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     CLASS                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TTL                      |
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                   RDLENGTH                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--|
    /                     RDATA                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    """
    def __init__(self):
        self.NAME = None
        self.TYPE = None
        self.CLASS = None
        self.TTL = None
        self.RDLENGTH = None
        self.RDATA = None
        self.start = None
        self.stop = None

    def loads(self, message, data):
        self.start = message.start()

        """
        NAME            a domain name to which this resource record pertains.
        """
        def load_name(index, name):
            print(f'index: {index}')
            if (data[index] & 0b11000000) == 0b11000000:
                value = int.from_bytes(data[index:index+2], byteorder='big', signed=False)
                pointer = value & 0x3FFF
                index += 2
                index += load_name(pointer, name)
            elif data[index] == 0:
                index += 1
            else:
                length = data[index]
                index += 1
                if 1 <= length <= 255:
                    string = data[index:index+length].decode('ascii')
                    name.append(string.lower())
                index += length
                index += load_name(index, name)
            return index

                # while True:
                #     found_pointer = (data[message.start()] & 0b11000000) == 0b11000000
                #     if found_pointer:
                #         value = int.from_bytes(data[message.start():message.start(offset=2)], byteorder='big',
                #                                signed=False)
                #         pointer = value & 0x3FFF
                #         message.inc(2)
                #         while True:
                #             length = data[pointer]
                #             pointer += 1
                #             if 1 <= length <= 255:
                #                 qname = data[pointer:pointer + length].decode('ascii')
                #                 self.NAME.append(qname.lower())
                #                 pointer += length
                #             else:
                #                 break
                #         break
                #     else:
                #         length = data[message.start()]
                #         message.inc(1)
                #         if 1 <= length <= 255:
                #             qname = data[message.start():message.stop(offset=length)].decode('ascii')
                #             self.NAME.append(qname.lower())
                #             message.inc(length)
                #         else:
                #             break


        self.NAME = []
        Message.dump(message.start(), data)
        print(f'start: {message.start()}')
        message.inc(load_name(message.start(), self.NAME))

        """
        TYPE            two octets containing one of the RR type codes.  This
                        field specifies the meaning of the data in the RDATA
                        field.
        """
        self.TYPE = int.from_bytes(
            data[message.start(increment=0):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        """
        CLASS           two octets which specify the class of the data in the
                        RDATA field.
        """
        self.CLASS = int.from_bytes(
            data[message.start(increment=2):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        """
        TTL             a 32 bit unsigned integer that specifies the time
                        interval (in seconds) that the resource record may be
                        cached before it should be discarded.  Zero values are
                        interpreted to mean that the RR can only be used for the
                        transaction in progress, and should not be cached.
        """
        self.TTL = int.from_bytes(
            data[message.start(increment=2):message.start(offset=4)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        """
        RDLENGTH        an unsigned 16 bit integer that specifies the length in
                        octets of the RDATA field.
        """
        self.RDLENGTH = int.from_bytes(
            data[message.start(increment=4):message.start(offset=2)],
            byteorder='big',
            signed=False
        )
        # Message.dump(message.start(), data)
        message.inc(2)
        """
        RDATA           a variable length string of octets that describes the
                        resource.  The format of this information varies
                        according to the TYPE and CLASS of the resource record.
                        For example, the if the TYPE is A and the CLASS is IN,
                        the RDATA field is a 4 octet ARPA Internet address.
        """
        # Message.dump(message.start(), data)
        self.RDATA = data[message.start(increment=0):message.stop(offset=self.RDLENGTH)]

        # Move the index past the end of the question data block
        message.inc(self.RDLENGTH)

        Message.dump(message.start(), data)
        self.stop = message.start()
        return self

    def load(self, NAME, TYPE, CLASS, TTL, RDLENGTH, RDATA):
        self.NAME = NAME
        self.TYPE = TYPE
        self.CLASS = CLASS
        self.TTL = TTL
        self.RDLENGTH = RDLENGTH
        self.RDATA = RDATA
        return self

    def dumps(self, buffer):
        for name in self.NAME:
            buffer.append(len(name))
            buffer.extend(bytes(name, 'ascii'))
        buffer.append(0b00000000)
        buffer.extend(self.TYPE.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.CLASS.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.TTL.to_bytes(4, byteorder='big', signed=False))
        buffer.extend(self.RDLENGTH.to_bytes(2, byteorder='big', signed=False))
        buffer.extend(self.RDATA)
        return buffer

    def __eq__(self, other):
        return (
            self.NAME     == other.NAME     and
            self.TYPE     == other.TYPE     and
            self.CLASS    == other.CLASS    and
            self.TTL      == other.TTL      and
            self.RDLENGTH == other.RDLENGTH and
            self.RDATA    == other.RDATA
        )

    def __repr__(self):
        buffer = [
            f'NAME={self.NAME}',
            f"TYPE={dns_rr_types.dns_rr_types.get(self.TYPE, 'Unassigned')}",
            f"CLASS={dns_classes.dns_classes.get(self.CLASS, 'Unassigned')}",
            f'TTL={self.TTL}',
            f'RDLENGTH={self.RDLENGTH}',
            f'RDATA="{self.RDATA}"',
        ]
        return f'Resource({",".join(buffer)})'


def resolver(question, disabled=False):
    answer = None
    rcode = None
    resolve = not disabled and question and len(question.QNAME) > 0 and question.QNAME[-1] == ORGANISATION
    if resolve:
        top_level_domain_only = len(question.QNAME) == 1
        if top_level_domain_only:
            resource = 'router1'
        else:
            resource = question.QNAME[-2]
        ip = BINDINGS.get(resource, None)
        if ip is None:
            rcode = dns_r_codes.R_NOTZONE
        else:
            ip = ip.split('.')
            rcode = dns_r_codes.R_NOERROR
            answer = ResourceRecord().load(
                NAME=question.QNAME,
                TYPE=dns_rr_types.RR_A,
                CLASS=dns_classes.INTERNET_IN,
                TTL=DEFAULT_TTL,
                RDLENGTH=4,
                RDATA=bytearray([int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])])
            )
    return resolve, rcode, answer


def validation_testing():
    buffer = bytearray()
    header.dumps(buffer)
    _message = Message()
    dummy_header = Header().loads(_message, buffer)
    print(f'd header:{dummy_header}')
    print(f'equal: {header == dummy_header}')

    buffer = bytearray()
    question.dumps(buffer)
    _message = Message()
    dummy_question = Question().loads(_message, buffer)
    print(f'd question:{dummy_question}')
    print(f'equal: {question == dummy_question}')


while True:
    verbose = 2
    data, address = connection.recvfrom(MAX_BUFFER_SIZE + 1)
    truncation = len(data) > MAX_BUFFER_SIZE
    message = Message()
    header = Header().loads(message, data)
    if header.QDCOUNT == 1:
        question = Question().loads(message, data)
    else:
        question = None

    query_address, query_port = address
    print(f'-> DNS query from {query_address}:{query_port}')
    if verbose > 0:
        print(
            f"** Received a message with id 0x{header.ID[0]:02X}{header.ID[1]:02X} "
            f"containing {len(data)} bytes of data and was {'' if truncation else 'not '}truncated"
        )
        print(f'*> {header}')
        print(f'*> {question}')

    if query_address == PASS_THROUGH_DNS_SERVER_IP:
        header.QR = Header.RESPONSE
        header.AA = Header.NON_AUTHORITATIVE
        header.TC = truncation
        header.RA = False
        header.RCODE = dns_r_codes.R_REFUSED
        buffer = bytearray()
        header.dumps(buffer)
        connection.sendto(buffer, address)
        print(f'<- Refusing to answer question from {query_address}:{query_port}')
        if verbose > 0:
            print(f'<* {header}')
        print(';;')
        continue

    resolved, rcode, answer = resolver(question, disabled=False)
    if resolved:
        if rcode == dns_r_codes.R_NOERROR:
            header.ANCOUNT = 1
            header.NSCOUNT = 0
            header.ARCOUNT = 0
        else:
            header.ANCOUNT = 0
            header.NSCOUNT = 0
            header.ARCOUNT = 0
        header.QR = Header.RESPONSE
        header.AA = Header.AUTHORITATIVE
        header.TC = truncation
        header.RA = False
        header.RCODE = rcode
        if verbose > 0:
            print(f'<* {header}')
        buffer = bytearray()
        header.dumps(buffer)
        question.dumps(buffer)
        if header.ANCOUNT == 1:
            answer.dumps(buffer)
            if verbose > 0:
                print(f'<* {answer}')
        connection.sendto(buffer, address)
        print(f'<- Returning authoritative answer to {query_address}:{query_port}')
    else:
        print(f'-> Forwarding DNS query to {PASS_THROUGH_DNS_SERVER_IP}:{UDP_SOCKET}')
        connection.sendto(data, (PASS_THROUGH_DNS_SERVER_IP, UDP_SOCKET))
        data, _ = connection.recvfrom(MAX_BUFFER_SIZE)
        print(f'<- Returning the answer to {query_address}:{query_port}')
        connection.sendto(data, address)

        if verbose > 1:
            message = Message()
            header = Header().loads(message, data)
            print(f'<* {header}')
            if header.QDCOUNT:
                for _ in range(header.QDCOUNT):
                    question = Question().loads(message, data)
                    print(f'<* {question}')
            if header.ANCOUNT:
                for _ in range(header.ANCOUNT):
                    answer = ResourceRecord().loads(message, data)
                    print(f'<* {answer}')
            if header.NSCOUNT:
                for _ in range(header.NSCOUNT):
                    authority = ResourceRecord().loads(message, data)
                    print(f'<* {authority}')
            if header.ARCOUNT:
                for _ in range(header.ARCOUNT):
                    additional = ResourceRecord().loads(message, data)
                    print(f'<* {additional}')

    print(';;')
