import requests
from bs4 import BeautifulSoup
limit=6

headers1={'user-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
         'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; SID=egebj00_6FlA0g0iKpTlmTf6kPhfDWjwjHdtjlTkW8nbEtSY5ZwnRahYzFOdsqqgsXeGJA.; HSID=ARiVztK4qffr170QW; SSID=Az7rKw8XIC2IFf0CW; APISID=cezGKzDAHLeFaH-P/Aq0nF09ttlF2GOp6o; SAPISID=4ftU0b6FSNnm9rLV/Aj9zALJWk1l90UGdR; ANID=AHWqTUkf37yjEmJGl-ImRSFFU_3ftc3FpJqpXKAOHD5uUDXSSMw5h9y0vhHIZtzR; 1P_JAR=2019-07-01-14; NID=186=TFvPZgzHv2WGVx9X6wg9B5GglkRAqc7o9R76FWoM-xqFtKmFJVrFSobqz_5itoyU1ttB10A1YugDujmkZi3QyHlnkjoIWdUK4lCPsRMu_JyAoDlk5KIAyREULY3jFjIKfJ6U_A-SzHzfsYBl_DohOqK9OsEZO7dbioO9lzukGKn3KNW7gP66HdYldebhbeggyAUtW1g3CjvCL4RBweaSJFkxzlwNvr9ltZJm1eSgGII4gxXLXnWR8c6DFL8xfUZxhwxtsHDYSsFKFSm1mne0yAU; SIDCC=AN0-TYvrJcs9BuIO6PAYraSFDzRsTyArtGsyDp59CnsygrJ1kxFzG58vrJD4H73r08llp0hl4-c'
         }
def space_to_plus(space_text):
    plus_text=space_text.replace(' ','+')
    return plus_text

def link_scrape(to_be_searched):
    changed_query=space_to_plus(to_be_searched)
    link='https://www.google.com/search?q='+changed_query
    r=requests.get(link,headers=headers1)
    soup=BeautifulSoup(r.text,'lxml')
    #print(soup)
    all_links=soup.find_all(class_='ZINbbc xpd O9g5cc uUPGi')
    index=0
    for l in all_links:
        l_better=l.div.a
        to_split_link=l_better.get('href')
        master_link = to_split_link.split('q=')[1]
        final_link = master_link.split('&sa')[0]
        print(final_link)
        index+=1
        if index==limit:
            break



