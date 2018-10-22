import json
import requests
import pprint as p
import random

class Senti:

    def sentiments(self):
        headers = {
            "Authorization": "Bearer EAAQuXVhWilUBAKnKQGauZAdLdm8kB9mCj5v0JRtOZBfZAeaDOKLBRBHJxLmAhmDQe1oNedXmfqvu6I0fZB8hRd4EDWtU83ztgjL9GiqoD0wJpJUgFWHzcdhdIZArMoez5jG6PCLqf7lt73aVxVLBMMYPbMIZCu4ATE94prW0xRNQ6XB9ZA35SvlWvmN9rTKUgaE9ovdy8uEMAZDZD"}
        r = requests.get('https://graph.facebook.com/me?fields=posts.limit(10)', headers=headers)
        res = r.json()
       # a = res['posts']['data']
        ll = []
        pp = []
        d = {}
        #for i in a:
         #   if 'message' in i.keys():
          #      ll.append(list(i.values()))
        #for j in ll:
         #   pp.append(j[0])

        #d['post'] = pp
        comments = ['Haesh! I am sad today','Holy shit I am so sad and crying','hey I am happy today.', 'very fine day.', 'So Enjoying today!', 'I am scared!', 'nice place to visit', 'feeling sick', 'feeling quality time with him.', 'So scared today!']
        pp = random.randrange(len(comments))
        tweeter_comments = ''
        return comments[pp]


if __name__ == '__main__':
    obj = Senti()
    z = obj.sentiments()
