import plotly.figure_factory as pf
import pandas as p
import statistics as s
import random as r
import plotly.graph_objects as go

df = p.read_csv("project.csv")
data = df["reading_time"].tolist()
populationmean = s.mean(data)
std = s.stdev(data)
print(populationmean,std)

def randomsetofmean(number):
    dataset = []
    for i in range(0,number):
        index = r.randint(0,len(data)-1)
        value=  data[index]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

def show(list):
    mean = s.mean(list)
    fig = pf.create_distplot([list],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.5],mode="lines",name="mean"))
    fig.show()

def setup():
    meanlist = []
    for j in range(0,100):
        means = randomsetofmean(30)
        meanlist.append(means)
    show(meanlist)
    mean = s.mean(meanlist)
    std = s.stdev(meanlist)
    print(mean,std)

setup()

df1 = p.read_csv("pro.csv")
data1 = df1["reading_time"].tolist()
mean1 = s.mean(data1)
zscore = (mean1-populationmean)/std
print(zscore)