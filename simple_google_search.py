import time
import random

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")





# to search
search_list = [



]
for searchterm in search_list:
    query = searchterm


    try:
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print(searchterm + "- ",j)

        time.sleep(300)

    except Exception:
        time.sleep(3600)
        try:

            for x in search(query, tld="co.in", num=1, stop=1, pause=2):
                print(searchterm + "- ",x)

        except Exception:
            time.sleep(3600)
            for y in search(query, tld="co.in", num=1, stop=1, pause=2):
                print(searchterm + "- ",y)
