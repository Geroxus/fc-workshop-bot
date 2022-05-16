import requests

start = 'https://ffxiv.consolegameswiki.com/wiki/'


def get_tables_entries(text, position):
    value = []
    for row in text.split('tbody')[position].split('tr')[2:]:
        if len(row) > 5:
            # print(row.split('td')[7].split('</')[0][1:])
            # print(row.split('td')[9].split('title=\"')[1].split('\">')[0])
            value.append(
                row.split('td')[9].split('title=\"')[1].split('\">')[0] + ': ' + row.split('td')[7].split('</')[0][1:])
    return value


def mat_list(vehicle_type, part):
    value = []
    r = requests.get(start + vehicle_type + '-type_' + part)
    # with open('output.txt', 'wt', encoding='utf-8') as f:
    #     f.write(r.text)
    print('start')
    # print(r.text.split('tbody')[3], r.text.split('tbody')[5])
    # value[0] = \
    # print(get_tables_entries(r.text, 1))
    # value[1] = get_tables_entries(r.text, 3)
    # value[2] = get_tables_entries(r.text, 5)
    for i in [1, 3, 5]:
        value.append(get_tables_entries(r.text, i))
    return value


# print(mat_list('Bronco', 'Sail'))

# https://ffxiv.consolegameswiki.com/wiki/Bronco-type_Hull
# https://ffxiv.consolegameswiki.com/wiki/Bronco-type_Sail
# https://ffxiv.consolegameswiki.com/wiki/Bronco-type_Forecastle
# https://ffxiv.consolegameswiki.com/wiki/Bronco-type_Aftcastle
#
# https://ffxiv.consolegameswiki.com/wiki/Invincible-type_Hull
# https://ffxiv.consolegameswiki.com/wiki/Invincible-type_Propellers
# https://ffxiv.consolegameswiki.com/wiki/Invincible-type_Forecastle
# https://ffxiv.consolegameswiki.com/wiki/Invincible-type_Aftcastle
#
# https://ffxiv.consolegameswiki.com/wiki/Enterprise-type_Hull
# https://ffxiv.consolegameswiki.com/wiki/Enterprise-type_Bladder
# https://ffxiv.consolegameswiki.com/wiki/Enterprise-type_Forecastle
# https://ffxiv.consolegameswiki.com/wiki/Enterprise-type_Aftcastle
