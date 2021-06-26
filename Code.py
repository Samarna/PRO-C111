import pandas as pd 
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go 
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

print("Mean of Population : ",statistics.mean(data))
print("SD of Population : ",statistics.stdev(data))

#fig = ff.create_distplot([data],["Math Scores"],show_hist = False)
#fig.show()

def randomSampleMean(num):
    dataset = []
    for i in range(0,num):
        random_index = random.randint(0,len(data)-1)
        dataset.append(data[random_index])
    mean = statistics.mean(dataset)
    return mean 

list_of_means = []
for i in range(0,1000):
    means = randomSampleMean(100)
    list_of_means.append(means)
mean = statistics.mean(list_of_means)
print("Mean of sampling distribution : ",mean)
std = statistics.stdev(list_of_means)
print("SD of sampling distribution : ",std)

std_start_1, std_end_1 = mean - std, mean + std
std_start_2, std_end_2 = mean - 2*std, mean + 2*std
std_start_3, std_end_3 = mean - 3*std, mean + 3*std

fig1 = ff.create_distplot([list_of_means],["Scores"],show_hist = False)
fig1.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = "lines",name = "Mean"))
fig1.add_trace(go.Scatter(x = [std_start_1,std_start_1], y = [0,0.2],mode = "lines",name = "Standard Deviation Start 1"))
fig1.add_trace(go.Scatter(x = [std_end_1,std_end_1], y = [0,0.2],mode = "lines",name = "Standard Deviation End 1"))
fig1.add_trace(go.Scatter(x = [std_start_2,std_start_2], y = [0,0.2],mode = "lines",name = "Standard Deviation Start 2"))
fig1.add_trace(go.Scatter(x = [std_end_2,std_end_2], y = [0,0.2],mode = "lines",name = "Standard Deviation End 2"))
fig1.add_trace(go.Scatter(x = [std_start_3,std_start_3], y = [0,0.2],mode = "lines",name = "Standard Deviation Start 3"))
fig1.add_trace(go.Scatter(x = [std_end_3,std_end_3], y = [0,0.2],mode = "lines",name = "Standard Deviation End 3"))

#fig1.show()

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

mean_sample_1 = statistics.mean(data)
fig1 = ff.create_distplot([list_of_means],["Scores"],show_hist = False)
fig1.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = "lines",name = "Mean"))
fig1.add_trace(go.Scatter(x = [std_end_1,std_end_1], y = [0,0.2],mode = "lines",name = "Standard Deviation End 1"))
fig1.add_trace(go.Scatter(x = [std_end_2,std_end_2], y = [0,0.2],mode = "lines",name = "Standard Deviation End 2"))
fig1.add_trace(go.Scatter(x = [std_end_3,std_end_3], y = [0,0.2],mode = "lines",name = "Standard Deviation End 3"))
fig1.add_trace(go.Scatter(x = [mean_sample_1,mean_sample_1], y = [0,0.2],mode = "lines",name = "Mean of sample 1"))

#fig1.show()

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()

mean_sample_2 = statistics.mean(data)
fig1 = ff.create_distplot([list_of_means],["Scores"],show_hist = False)
fig1.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = "lines",name = "Mean"))
fig1.add_trace(go.Scatter(x = [std_end_1,std_end_1], y = [0,0.2],mode = "lines",name = "Standard Deviation End 1"))
fig1.add_trace(go.Scatter(x = [std_end_2,std_end_2], y = [0,0.2],mode = "lines",name = "Standard Deviation End 2"))
fig1.add_trace(go.Scatter(x = [std_end_3,std_end_3], y = [0,0.2],mode = "lines",name = "Standard Deviation End 3"))
fig1.add_trace(go.Scatter(x = [mean_sample_2,mean_sample_2], y = [0,0.2],mode = "lines",name = "Mean of sample 2"))

#fig1.show()

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean_sample_3 = statistics.mean(data)
fig1 = ff.create_distplot([list_of_means],["Scores"],show_hist = False)
fig1.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = "lines",name = "Mean"))
fig1.add_trace(go.Scatter(x = [std_end_1,std_end_1], y = [0,0.2],mode = "lines",name = "Standard Deviation End 1"))
fig1.add_trace(go.Scatter(x = [std_end_2,std_end_2], y = [0,0.2],mode = "lines",name = "Standard Deviation End 2"))
fig1.add_trace(go.Scatter(x = [std_end_3,std_end_3], y = [0,0.2],mode = "lines",name = "Standard Deviation End 3"))
fig1.add_trace(go.Scatter(x = [mean_sample_3,mean_sample_3], y = [0,0.2],mode = "lines",name = "Mean of sample 3"))

#fig1.show()

z_score = (mean_sample_1 - mean)/std 
print("Z score for sample 1 : ",z_score)
z_score = (mean_sample_2 - mean)/std 
print("Z score for sample 2 : ",z_score)
z_score = (mean_sample_3 - mean)/std 
print("Z score for sample 3 : ",z_score)
