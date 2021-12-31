import requests
def email_check(email):
    url = "https://api.eva.pingutil.com/email?email="+email
    response = requests.get(url)
    data = response.json()
    valid = data['data']
    if (valid['valid_syntax'] == True and valid['webmail'] == True and valid['deliverable'] == True and valid['gibberish'] == False and valid['spam'] == False and valid['disposable'] == False):
        return [True,valid]
    else:
        return [False, valid]

# def phone_check(number):
#     url = "https://veriphone.p.rapidapi.com/verify"
#
#     querystring = {"phone": number}
#
#     headers = {
#         'x-rapidapi-host': "veriphone.p.rapidapi.com",
#         'x-rapidapi-key': "34262c539amsh117b337c7ab904fp198546jsn3cb7619c8fb4"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     values = response.json()
#     if(values['status'] == "success" and values['phone_valid']==True and values['phone_type'] != "unknown" and values['carrier'] != ""):
#         return [True,values]
#
#     else:
#         return [False,values]


print(email_check('nkush9598@gmail.com'))


# "status":"success"
# "phone":"895767133"
# "phone_valid":false
# "phone_type":"unknown"
# "phone_region":""
# "country":"India"
# "country_code":"IN"
# "country_prefix":"91"
# "international_number":"+91 895767133"
# "local_number":"895767133"
# "e164":"+91895767133"
# "carrier":""

# "status":"success"
# "phone":"+918957671332"
# "phone_valid":true
# "phone_type":"mobile"
# "phone_region":"India"
# "country":"India"
# "country_code":"IN"
# "country_prefix":"91"
# "international_number":"+91 89576 71332"
# "local_number":"089576 71332"
# "e164":"+918957671332"
# "carrier":"Reliance Jio"

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline