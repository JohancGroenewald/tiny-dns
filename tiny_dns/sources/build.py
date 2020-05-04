import csv
import os

"""
This file will convert the Domain Name System (DNS) Parameters CSV files to python dictionaries
Source: www.iana.org/assignments/dns-parameters/dns-parameters.xhtml
"""
source_mapping = {
    'classes' : ('dns-parameters-2.csv', 'dns_classes.py' , 'dns_classes' , ''   ),
    'rr_types': ('dns-parameters-4.csv', 'dns_rr_types.py', 'dns_rr_types', 'RR_'),
    'op_codes': ('dns-parameters-5.csv', 'dns_op_codes.py', 'dns_op_codes', 'OP_'),
    'r_codes' : ('dns-parameters-6.csv', 'dns_r_codes.py' , 'dns_r_codes' , 'R_' ),
}


def build_dns_classes(source='classes', out_path=''):
    in_file, out_file, dict_name, prefix = source_mapping[source]
    buffer = []
    dictionary = {}
    with open(in_file) as f:
        csv_reader = csv.reader(f, dialect='excel')
        def append_raw():
            buffer.append(f"{' ' * 4}# {_decimal}: ('{_name}', '{_reference}'),")
        for row in csv_reader:
            _decimal, _hexadecimal, _name, _reference = row
            _reference = _reference.replace('\n', '').replace('\r', '')
            if _name in ['Reserved', 'Unassigned']:
                append_raw()
                continue
            try:
                key = int(_decimal)
                value = f"('{_name}', '{_reference}'),"
                if key in dictionary:
                    append_raw()
                    continue
                dictionary[key] = (_name, _reference)
                buffer.append(f"{' '*4}{key}: {value}")
            except:
                append_raw()
    buffer.insert(0, f'{dict_name} = ''{')
    buffer.append('}')
    buffer.append('')
    replace = [
        (' ', '_'),
        ('(', ''),
        (')', ''),
        ('*_', ''),
    ]
    for key, value in dictionary.items():
        _name, _reference = value
        for _old, _new in replace:
            _name = _name.replace(_old, _new)
        _name = _name.upper()
        buffer.append(f"{prefix}{_name} = {key}")
    buffer.append('')
    with open(os.path.join(out_path, out_file), 'w') as f:
        f.write('\n'.join(buffer))


def build_dns_rr_types(source='rr_types', out_path=''):
    in_file, out_file, dict_name, prefix = source_mapping[source]
    buffer = []
    dictionary = {}
    with open(in_file) as f:
        csv_reader = csv.reader(f, dialect='excel')
        def append_raw():
            buffer.append(f"{' ' * 4}# {_value}: ('{_type}', '{_meaning}'),")
        for row in csv_reader:
            _type, _value, _meaning, _reference, _template, _registration_date = row
            if _type in ['Reserved', 'Unassigned']:
                append_raw()
                continue
            try:
                key = int(_value)
                value = f"('{_type}', '{_meaning}'),"
                if key in dictionary:
                    append_raw()
                    continue
                dictionary[key] = (_type, _meaning)
                buffer.append(f"{' ' * 4}{key}: {value}")
            except:
                append_raw()
    buffer.insert(0, f'{dict_name} = ''{')
    buffer.append('}')
    buffer.append('')
    replace = [
        ('-', '_'),
        ('*', 'ANY'),
    ]
    for key, value in dictionary.items():
        _name, _reference = value
        for _old, _new in replace:
            _name = _name.replace(_old, _new)
        _name = _name.upper()
        buffer.append(f"{prefix}{_name} = {key}")
    buffer.append('')
    with open(os.path.join(out_path, out_file), 'w') as f:
        f.write('\n'.join(buffer))


def build_dns_op_codes(source='op_codes', out_path=''):
    in_file, out_file, dict_name, prefix = source_mapping[source]
    buffer = []
    dictionary = {}
    with open(in_file) as f:
        csv_reader = csv.reader(f, dialect='excel')
        def append_raw():
            buffer.append(f"{' ' * 4}# {_opcode}: ('{_name}', '{_reference}'),")
        for row in csv_reader:
            _opcode, _name, _reference = row
            if _name in ['Reserved', 'Unassigned']:
                append_raw()
                continue
            try:
                key = int(_opcode)
                value = f"('{_name}', '{_reference}'),"
                if key in dictionary:
                    append_raw()
                    continue
                dictionary[key] = (_name, _reference)
                buffer.append(f"{' ' * 4}{key}: {value}")
            except:
                append_raw()
    buffer.insert(0, f'{dict_name} = ''{')
    buffer.append('}')
    buffer.append('')
    replace = [
        ('-', '_'),
        ('  (Inverse Query, OBSOLETE)', ''),
        ('DNS Stateful Operations (DSO)', 'DSO'),
    ]
    for key, value in dictionary.items():
        _name, _reference = value
        for _old, _new in replace:
            _name = _name.replace(_old, _new)
        _name = _name.upper()
        buffer.append(f"{prefix}{_name} = {key}")
    buffer.append('')
    with open(os.path.join(out_path, out_file), 'w') as f:
        f.write('\n'.join(buffer))


def build_dns_r_codes(source='r_codes', out_path=''):
    in_file, out_file, dict_name, prefix = source_mapping[source]
    buffer = []
    dictionary = {}
    with open(in_file) as f:
        csv_reader = csv.reader(f, dialect='excel')
        def append_raw():
            buffer.append(f"{' ' * 4}# {_rcode}: ('{_name}', '{_description}'),")
        for row in csv_reader:
            _rcode, _name, _description, _reference = row
            if _name in ['Reserved', 'Unassigned', 'Reserved, can be allocated by Standards Action']:
                append_raw()
                continue
            try:
                key = int(_rcode)
                value = f"('{_name}', '{_description}'),"
                if key in dictionary:
                    append_raw()
                    continue
                dictionary[key] = (_name, _description)
                buffer.append(f"{' ' * 4}{key}: {value}")
            except:
                append_raw()
    buffer.insert(0, f'{dict_name} = ''{')
    buffer.append('}')
    buffer.append('')
    replace = [
        ('-', '_'),
    ]
    for key, value in dictionary.items():
        _name, _reference = value
        for _old, _new in replace:
            _name = _name.replace(_old, _new)
        _name = _name.upper()
        buffer.append(f"{prefix}{_name} = {key}")
    buffer.append('')
    with open(os.path.join(out_path, out_file), 'w') as f:
        f.write('\n'.join(buffer))


if __name__ == '__main__':
    build_dns_classes(out_path='..')
    build_dns_rr_types(out_path='..')
    build_dns_op_codes(out_path='..')
    build_dns_r_codes(out_path='..')
