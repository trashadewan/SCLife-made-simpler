import requests
import unicodecsv as csv

def get_data_from_k(k):
    data = ""
    for some_data in k:
        data = data + some_data["_label"] + " | "
    data = data.rstrip(" | ")
    return data

output_f = open("output.txt", "w")
fieldnames = ['majors', 'name', 'industry', 'degree_level', 'days', 'position_types', 'position_titles', 'work_authorization',
                'contact', 'employer']
writer = csv.DictWriter(output_f, fieldnames=fieldnames, encoding='utf-8')
writer.writeheader()
writer.close()

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://usc-csm.symplicity.com/students/event/careerfairs/291138f0c7f02f1a61b7e4fe92af1798/overview?gotodiv=&student=af9806c34f676344314657e86d790de6',
    'authority': 'usc-csm.symplicity.com',
    'cookie': 'ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; __stripe_mid=7c8b5a2a-5659-45a8-92b0-78cb2bdf3cf9; _ga=GA1.2.98315038.1533586190; shib_givenName=Trasha; shib_sn=Dewan; shib_uscid=6527804874; shib_email=tdewan%40usc.edu; shib_schoolCode=ENGR; shib_ownerPVID=scbs7tz3; PHPSESSID=e414d0a5e807ac4bbc4b1da81817e126; sympcsm_cookie_check=1; __utmc=155774015; edd3f4b6736ed25181d5405c66c0a5cc=M04yMEpOTU4xMUpNNEq2NEpLNk8zMU0zSE4yMrQ0SLO0CnP0sTIEAA%3D%3D; shib_user=6527804874; __utma=155774015.98315038.1533586190.1536125913.1536525059.28; __utmz=155774015.1536525059.28.22.utmcsr=shibboleth.usc.edu|utmccn=(referral)|utmcmd=referral|utmcct=/idp/profile/SAML2/Redirect/SSO; __utmt=1; __utmt_b=1; __stripe_sid=18deda22-7dcf-4a44-8731-6d658a144797; __utmb=155774015.8.10.1536525059; AWSALB=f+hb8ICaqprNLg2XpsalVz5eu2sVl+qze5uoTRJJIREN9IXitB0kaIf5I9XNaX8OZ6G/UqMtu469GdkfJVpg7TYIzuygFkIQ0dHYdcSsoJv+exQjh+pB/Izxgo7i',
}

for i in xrange(1,11):
    params = (
        ('event', '291138f0c7f02f1a61b7e4fe92af1798'),
        ('remove_hidden_days', 'true'),
        ('page', i)
        )
    response = requests.get('https://usc-csm.symplicity.com/api/v2/eventRegistration', headers=headers, params=params)
    data =  response.json()

    models = data["models"]

    for model in models:
        company_data = {}
        company_data["name"] = model["name"]
        company_req_major = ""
        company_data["days"] = get_data_from_k(model["days"])
        company_data["majors"] = get_data_from_k(model["majors"])
        company_data["position_types"] = get_data_from_k(model["position_types"])
        company_data["position_titles"] = model["sal_position_titles_b30a45a34bc277f5bc6d9a8a6832d559"]
        company_data["work_authorization"] = get_data_from_k(model["work_authorization"])
        company_data["industry"] = get_data_from_k(model["industry"])
        company_data["degree_level"] = get_data_from_k(model["degree_level"])
        try:
            company_data["contact"] = get_data_from_k(model["contact"])
        except Exception:
            pass
        try:
            company_data["employer"] = get_data_from_k(model["employer"])
        except Exception:
            pass
        writer.writerow(company_data)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://usc-csm.symplicity.com/api/v2/eventRegistration?event=291138f0c7f02f1a61b7e4fe92af1798&remove_hidden_days=true', headers=headers)
