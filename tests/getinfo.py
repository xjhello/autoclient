
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)

res = open(os.path.join(BASE_DIR , 'files/board.out'), 'r', encoding='utf-8').read()
print(res)


'''

['SMBIOS 2.7 present.\n\nHandle 0x0001, DMI type 1, 27 bytes\nSystem Information\n\tManufacturer: Parallels Software International Inc.\n\tProduct Name: Parallels Virtual Platform\n\tVersion: None\n\tSerial Number: Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30\n\tUUID: 3BCB1B1A-6664-134B-86B0-86FF7E2B2030\n\tWake-up Type: Power Switch\n\tSKU Number: Undefined\n\tFamily: Parallels VM']
'''

map_key = {
    "Manufacturer" : 'manufacturer',
    "Product Name" : 'pname',
    "Serial Number" : 'sn',
}
response = {}
for v in res.split('\n\t'):
    res = v.split(':')
    if len(res) == 2:
        if res[0] in map_key:
            response[map_key[res[0]]] = res[1].strip() if res[1].strip() else res[1].strip()

print(response)