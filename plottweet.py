import matplotlib.pyplot as plt
import numpy as np
from tweet_Test import gettweet
# used defind module : tweet_Test


'''
dataset = pd.read_csv("scores.csv")
positive=dataset[['positive']].T
negative=dataset[['negative']].T
neutral=dataset[['neutral']].T
print(type(positive))
print(positive)
print(negative)
print(neutral)
'''
res = gettweet()
print(res)

#positive=[20,30,50]
#negative=[40,20,20]
#neutral=[40,50,30]

positive=[]
negative=[]
neutral=[]

for i in range(0,len(res)):
    positive.append(res[i][0])
    negative.append(res[i][1])
    neutral.append(res[i][2])



# data to plot
n_groups = 3

 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, positive, bar_width,
                 alpha=opacity,
                 color='b',
                 label='positive')
 
rects2 = plt.bar(index + bar_width, negative, bar_width,
                 alpha=opacity,
                 color='g',
                 label='negative')

rects3 = plt.bar(index + bar_width+ bar_width, neutral, bar_width,
                 alpha=opacity,
                 color='r',
                 label='neutral')

 
plt.xlabel('Persons')
plt.ylabel('Sentiments')
plt.title('Twitter sentiment analysis')
plt.xticks(index + bar_width, ('Donald Trump', 'Narendra Modi', 'Rahul Gandhi'))
plt.legend()
 
plt.tight_layout()
plt.show()

