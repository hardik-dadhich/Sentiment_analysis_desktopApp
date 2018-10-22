import json
from watson_developer_cloud import ToneAnalyzerV3
from sentimental import *
import ast
import pandas as pd
from ss import *


# ton analyser class that takes comments and return mood status according to it.
class TonAna:
    def statusfun(self):
        tone_analyzer = ToneAnalyzerV3(version='2018-08-01', username='5aab6b7d-c06c-4105-aa4e-9fd81030451c',
                                       password='lPH5HXLmrDdN',
                                       url='https://gateway.watsonplatform.net/tone-analyzer/api')
        # temp = Senti()
        # res = temp.sentiments()
        # text = res

        temp = TwitterClient()
        res = temp.tweetsanalyse()
        text = res
        print("this is about tweeter!")

        tone_analysis = tone_analyzer.tone({'text': text}, 'application/json').get_result()
        output = json.dumps(tone_analysis, indent=2)
        x = ast.literal_eval(output)
        fin = x['document_tone']['tones']
        df = pd.DataFrame(fin)
        mood = df.loc[0]['tone_name']
        print(mood)
        return mood


if __name__ == '__main__':
    obj = TonAna()
    obj.statusfun()
