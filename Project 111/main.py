import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import random
df = pd.read_csv('medium_data.csv')
data = df[''].tolist()
population_mean = statistics.mean(df)
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
meanList = []
def Setup():
    meanOfSamples=randomSetOfMean(100)
    meanList.append(meanOfSamples)
stDev = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print("Mean is : ",mean)
print("Standard Deviation = ",stDev)
FirstStDevStart,FirstStDevEnd = mean-stDev,mean+stDev
SecondStDevStart,SecondStDevEnd = mean-2*stDev,mean+2*stDev
ThirdStDevStart , ThirdStDevEnd = mean-3*stDev,mean+3*stDev
print('1st Resulting Standard Deviations(Start,End) = ',FirstStDevStart,FirstStDevEnd)
print('2nd Resulting Standard Deviations(Start,End) = ',SecondStDevStart,SecondStDevEnd)
print('3rd Resulting Standard Deviations(Start,End) = ',ThirdStDevStart,ThirdStDevEnd)
fig = ff.create_distplot([meanList],['Graph'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,0.17],mode='lines'))
fig.add_trace(go.Scatter(x=[FirstStDevEnd,FirstStDevEnd],y=[0,0.17],mode='lines'))
fig.add_trace(go.Scatter(x=[SecondStDevEnd,SecondStDevEnd],y=[0,0.17],mode='lines'))
fig.add_trace(go.Scatter(x=[ThirdStDevEnd,ThirdStDevEnd],y=[0,0.17],mode='lines'))
fig.show()
z_score = (mean-population_mean)/stDev
print(z_score) 
    