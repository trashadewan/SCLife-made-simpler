import requests
import time

headers = {
    'cookie': '_ga=GA1.2.894911153.1537472528; _ga=GA1.3.894911153.1537472528; _gcl_au=1.1.640240292.1538488917; _gid=GA1.2.2006620673.1538772661; _gid=GA1.3.2006620673.1538772661',
    'origin': 'https://libcal.usc.edu',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://libcal.usc.edu/reserve/its',
    'authority': 'libcal.usc.edu',
    'x-requested-with': 'XMLHttpRequest',
}

headers1 = {
    'cookie': '_ga=GA1.2.371424562.1509635181; __unam=79ac26c-165302d8104-76df8e9b-2; _ga=GA1.3.371424562.1509635181; ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; _gid=GA1.2.903064618.1542251894; _gid=GA1.3.903064618.1542251894; _gat=1; _gat_UA-3613630-3=1',
    'origin': 'https://libcal.usc.edu',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://libcal.usc.edu/equipment/confirm/cs_REeBJdsP',
    'authority': 'libcal.usc.edu',
    'x-requested-with': 'XMLHttpRequest',
    'content-length': '0',
}

data1 = {
    'formData[fname]': 'ABC',
    'formData[lname]': 'DEF',
    'formData[email]': '****@usc.edu',
    'forcedEmail': '',
    'bookings[0][id]': '1',
    'bookings[0][eid]': '18394',
    'bookings[0][gid]': '4896',
    'bookings[0][lid]': '2895',
    'bookings[0][start]': '2018-10-16 14:30',
    'bookings[0][end]': '2018-10-16 16:00'
}

data2 = {
    'formData[fname]': 'ABC',
    'formData[lname]': 'DEF',
    'formData[email]': '*****@usc.edu',
    'forcedEmail': '',
    'bookings[0][id]': '1',
    'bookings[0][eid]': '18394',
    'bookings[0][gid]': '4896',
    'bookings[0][lid]': '2895',
    'bookings[0][start]': '2018-10-16 16:00',
    'bookings[0][end]': '2018-10-16 18:00'
}

data = []

# room No: 3W
data1['bookings[0][id]'] = '1'
data1['bookings[0][eid]'] = '18395'
data2['bookings[0][id]'] = '1'
data2['bookings[0][eid]'] = '18395'

# room NO: 3T
data1['bookings[0][id]'] = '6'
data1['bookings[0][eid]'] = '18394'
data2['bookings[0][id]'] = '6'
data2['bookings[0][eid]'] = '18394'

# room No: 3S
data1['bookings[0][id]'] = '1'
data1['bookings[0][eid]'] = '18393'
data2['bookings[0][id]'] = '1'
data2['bookings[0][eid]'] = '18393'

# room No: 3L
data1['bookings[0][id]'] = '1'
data1['bookings[0][eid]'] = '18400'
data2['bookings[0][id]'] = '1'
data2['bookings[0][eid]'] = '18400'

# room No: 3G
data1['bookings[0][id]'] = '1'
data1['bookings[0][eid]'] = '18389'
data2['bookings[0][id]'] = '1'
data2['bookings[0][eid]'] = '18389'

date = '2018-11-20'
data1['bookings[0][start]'] = date + ' 12:00'
data2['bookings[0][start]'] = date + ' 14:00'

data1['bookings[0][end]'] = date + ' 14:00'
data2['bookings[0][end]'] = date + ' 16:00'

data.append(data1)
data.append(data2)

for d in data:
    response = requests.post('https://libcal.usc.edu/ajax/space/book', headers=headers, data=d)
    r = response.json()
    print r
    book_id = r['bookId']
    time.sleep(10)
    req = 'https://libcal.usc.edu/equipment/confirm/' + str(book_id)
    headers1['referer'] = req
    response1 = requests.post(req, headers=headers1)
    print response1.json()
    time.sleep(10)
