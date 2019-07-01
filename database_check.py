#done
import re,codecs

def db_check(y):
    with open('my_probe.txt','r') as r:
        con = r.read().splitlines()
        for c in con:
            #print(c)
            req = c.split('|')
            x = codecs.decode(c, 'unicode_escape')
            # print(x)
            if re.search(x, y):
                ans=req[1]
                break
            else:
                ans='?'
                continue
            #print(c)
    return ans

