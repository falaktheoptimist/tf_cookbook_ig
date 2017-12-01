from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
def get_details(url):
    r = requests.get(url)
    json_dict = r.json()
    watchers = json_dict['subscribers_count']
    forks = json_dict['forks']
    open_issues = json_dict['open_issues']
    stars = json_dict['stargazers_count']
    return [stars, watchers, forks, open_issues]

base_url ='https://api.github.com/repos/'
urls = ['tensorflow/tensorflow', 'fchollet/keras', 'BVLC/caffe','Microsoft/CNTK',
'apache/incubator-mxnet','pytorch/pytorch','deeplearning4j/deeplearning4j','Theano/Theano']



listup = []
for url in urls:
    lo = get_details(base_url + url)
    listup = listup + [[url[url.index('/')+1:]]  + lo]

df = pd.DataFrame(columns = ['Library Name', 'Stars','Watchers', 'Forks', 'Open Issues'], data = listup)
print df

plt.figure(figsize=(15.0, 8.0))
plt.subplot(2,2,1)
sns.barplot( df['Library Name'], df['Stars'])
plt.ylabel('Stars')
plt.subplot(2,2,2)
sns.barplot( df['Library Name'], df['Forks'])
plt.ylabel('Forks')
plt.subplot(2,2,3)
sns.barplot( df['Library Name'], df['Watchers'])
plt.ylabel('Watchers')
plt.subplot(2,2,4)
sns.barplot( df['Library Name'], df['Open Issues'])
plt.ylabel('Open Issues')
plt.tight_layout()
plt.savefig('Current_stats.png')
plt.show()

