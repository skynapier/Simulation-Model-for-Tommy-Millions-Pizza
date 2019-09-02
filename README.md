# [Final Presentation slides here!](Group_1__A_Study_of_Tommy_MIllions_Pizza.pdf)

Most of scripts function same as their names. The special 3 scripts: M1.py, M2.py and M3.py are the three simulation models.

## Introduction
The purpose of the project is to study a system, prepare theoretical and simulation models that could be used to predict what effect changes in the queue setup would have .

## Objective
### The objectives of the project are:
- to practice measuring, analysing, and modeling a real queueing system.
- to analyse observations and extract any useful information. In particular, we are interested in the customer arrival process and the service channel discipline and service times;
- to construct both a queue model and a simulation model of the system for prediction or optimisation;
- to evaluate the performance measures of the system. So your model should be able to predict the customer waiting time or average queue lengths.
- to compare the model's performance measures with those of the real system.

We chose Tommy Millions Pizza because it was a service that we knew had a good rate of arrivals, limited servers, and the service to be a substantial fraction of the interarrival time. Other  services we discarded were: McDonalds Drive Through, Self Services Checkouts at Countdown, Petrol Stations, and Movie Theaters. Most of these ended up being too complicated to collect data for due to: slow arrivals, multiple servers, difficulty keeping track of customers, multiple queues, service time too short, or grouped arrivals. 
Data Processing and Simulations

### Data Criteria (Michael)
Data were initially gathered on 21st, 23rd, 24th, and 27th April 2018 and then one extra day on the 3rd of may 2018. Each data collection session was around 2 hours and approximately from 1200 to 1400. Data was collected by a sole observer at each session. 

We manually used a table to gather the data collection the Date, Arrival Time, Service Start Time, Service Finish Time. We then put the data into an Excel Spreadsheet, downloaded it as a CSV file, then put into a Machine readable format using Atom Text Editor. 

We found that the data collected from the 21st April 2018 skewed the data too much (See below). The factors we believe contributed to this are: 
- School holidays
- Weekend
- People don’t eat out as much on the weekend
- If they do it might later in the day
- Hungover?

So instead we decided to collect data only during work days. 

We chose to target the times of 1200 to 1400 because it was over the lunch period and we thought this would have the best flow of arrival times. Tommy Millions noted that their busy periods were during the day around 1200 to 1400 and also in the late night on the weekend as they are open till 4pm. 

Another thing to note is that the data collection period(Saturday 21st April 2018 to Thursday 3rd May 2018) coincided with the School holidays (Saturday 14th to Sunday 29th April 2018) and the Victoria University holidays (Saturday 21st April to Sunday 29th April 2018). We believe that this could have an affect on the data collected, however we have no proof of that and we believe that the results can still be used to help benefit Tommy Millions Pizza, during busy these times.

### Data Collection (Tian)

The data subsets for each day were presented as side-by-side box-plots for comparison.

The subsets for inter-arrival times are reasonably similar in their distribution [see figure 1].

![](/figures/Figure1.jpg)
#### Figure 1: Boxplots comparing subsets of inter-arrival times.

The comparison of the subsets of service times [see figure 2] showed that the service times for 21st April appear to be markedly longer.  We could not be sure whether this was because the data from that day represented a different distribution, that is because it was a weekend day rather than a weekday, or because the data was collected by a different observer and we had not standardised our data collection methods.

![](/figures/Figure2.jpg)
#### Figure 2: Boxplots comparing subsets of service times.

Having decided to discard the data from 21st April it was decided that a further data collecting session was required.  This was carried out on 3rd May 2018.

The data from the four data subsets were presented as histograms with the same scale on each axis to allow visual comparison [see figures 3,4].  The subsets of inter-arrival times all display the same general distribution of data.  The shape of the histogram for 23rd April shows a less marked peak to the left of the curve compared to the data for the other three days although it is still present.  All four distributions show a relative long tail trailing to the right.  The data subsets for service times all have a similar shape with the data peaking at the second bin from the left and a tail trailing to the right.

![](/figures/Figure3.jpg)
#### Figure 3: Histograms comparing subsets of inter-arrival times

![](/figures/Figure4.jpg)
#### Figure 4: Histograms comparing subsets of service times


Once the data were checked they were collated into one data set as a .csv file.

By the end of this stage the specific outputs produced were the observed distributions of random variables A (inter-arrival time) and S (service time) [see figure 3] and also the estimated first and second moments for both distributions [see table 1].  The histogram shows the distribution of the data (n = 273) in k = 10 bins (k = 1 + log[2]n) and the collected data for both random variables A and S preserves the shape that characterised the data subset..

![](/figures/Figure5.jpg)
#### Figure 5: Histograms of random variables A (inter-arrival time) and S (service time)

 
#### Random variable
 
A
S
First moment
 E(A) = 97
E (S) = 34
Second moment
E (A2) = 18493
E (S2) = 1654
Table 1: Estimated moments for random variables A,S


#### Programs Used
Pen and Paper for Manual collection
Excell to turn into .csv files
Atom text editor to turn into Machine readable code
Facebook for communication and data sharing

Data Processing and Simulations - Just talk about your script here , no discussing results. You should be able to talk about what variables you used and what your script did. Add reference to your script. We will add it to the appendix.

### M/M/1(Tian)
First of all, we must explain what is M/M/1 means, iid exponential interarrival arrival times, iid exponential service times, 1 single server and infinite many arrivals in the system. Moreover, For achieve a M/M/1 simulation model, we must mentioned one package of python which name is SimPy. The SimPy will help us build a simulation model by provide some useful methods of it. 

A simulation model could explain in three aspects, Source, Arrival and Monitor.
During data analysis, we have already find what are the parameters about our collected data of exponential interarrival times and exponential service times. The parameters are fit-lambda = 1.6120 for interval arrival time and fit-lambda=0.5639 for exponential service time. 
- Source, which simulate iid exponential interarrival arrival times. It means that we use the parameters that we got of iid exponential interarrival arrival times to random generate an arrival time for each arrival. The main function of this part is  t = random.expovariate(lambda = 1.6120).
- Arrival, which simulate iid exponential service time, although, the exponential distribution is not the fittest distribution for our service times. Arrival is similar with source aspect. The different between these two aspects is Arrival using the parameters of exponential service time which we got in the data analysis part. The main function of this part is  t = random.expovariate(lambda = 0.5639).
- Monitor, as for its name,  it is using for monitoring Source and Arrival and get three results which are W = the average time in the system, L = the average number of jobs in the system and B = the proportion of busy time (i.e. servers are full) in the system. We simulate 10000 arrivals in 200000 minutes at 50 times then we get 150 results for 50 each of W, L and B. Finally we using these 150 results to find 95% confidence interval of W, L and B, respectively.


### M/G/1(Liam)

#### What is M/G/1:
M/G/1 models are similar to M/M/1 however the service times have a general distribution rather than a Poisson process but they still both have 1 server and a Poisson process for the arrival rate. In this paper we have worked with erlang and gamma distributions which are both general distributions. These distributions have a shape parameter (K) and a scale parameter μ (which is the mean). If these distributions have a k of 1 they become an exponential distribution and when an erlang distribution has a real number as its k it becomes a gamma distribution. I ended up using an erlang distribution in my simulation rather than a gamma distribution because I'm more familiar with it in simpy, but since its k value was always a real number it basically acted as gamma distribution in my simulation. 

My simulation attempts 9 different values of k (1-9) so we can see what different results it gets due to different erlang shapes. The results differ from simulation to simulation due to random variables, so of those 9 different k values it does 50 different simulations, this means we get a more accurate average result and can produce a confidence interval.

The actual simulation itself has its default lambda equal to 1.612 arrivals per minute, 0.563898 servings per minute and 10000 different arrivals. After running my simulation with different values of N I found that the more jobs that go through the system, the higher the waiting time is. I’m not entirely sure why this is but it could be due to the warm up effect. This is when a system takes time after a simulation has started to get to a steady state. 

## Appendix
### Data analysis (Tian)
First of all, for data analysis include two parts. First part is load our data and second part is Chi-Square Goodness of Fit Test.

On one hand, when we get data from real world, the most important things that we need to do is convert these data into machine readable. We input the whole records into “.CVS” formatted file which could be using for many softwares, for example, R, SAS and Python. Consider that we will using Python for the next steps, we write a Python script for load and parser our data. The challenge of data analysis is due to our record of data file is a type of string (e.g. 12:45:06) and we just want a numerical type of time which might be float or integer. Python support one data type which name is “datetime” that we using for this problem and it could compare with two time then return a number as result which could using second, minutes or etc. for time units. 

Furthermore, consider we have many records in an order. The interval arrival time is the arrival time minus the previous arrival time, if we have 10 records then it will be just 9 interval time. For instance, there are 10 records of arrival time (1,2,3,4…,10), the interval time is (2-1), (3-2), …, (10-9). The service time is the end service time minus the start service time, if we have 10 records then it should be 10 service time. We use the script that I mentioned above to parser interarrival time and service time, respectively.

One the second hand, the next step of data analysis is that analyze the fittest distribution of interarrival time and service time. We write a script that using the Chi-Square Goodness of fit test. For approach this, then we need three steps: (1) state the hypothesis, (2) analyse sample data, (3) interpret results:

For (1), We using three distributions (Exponential, Erlang and Gamma) for state null hypotheses. 

For (2), because of interarrival time and service time are independent, both interarrival time and service time are sample data. There are also two significant parameters that we must find it firstly. The number of bins which should be at least 5 and we using method (k = 1 +log2n) to find it where n is the cardinality of sample data. The degree of freedom which in our script is equal to number of estimated parameters, because if the degree of freedom is large then the p-value will too small to show. In part (2), we will get result from test statistic and p-value.

For (3), Our objective is find which distribution hold the biggest p-value, the lowest chi-square test value. The p-value is the probability of observing a sample statistic as extreme as the test statistic and High p-value mean the data are likely with a true null. Moreover, for achieve this goal, we could use our data to find the fitting parameters of different distributions on interarrival time and service time, and then using these parameters to construct a random variable. Firstly, random variable could help us draw a plot of that distribution. Secondly, random variable is the most significant for run the test and calculate p- value. Finally, during our test then we could conclude that exponential distribution with lambda = 1.612 which is the most fitted distribution for interarrival time, for service time which is held by erlang distribution with k = 3 and lambda = 0.1873.

The plot of the Erlang distribution of interarrival time:
![](/results/Erlang_int_arr.png)

The plot of the Exponential distribution of interarrival time:
![](/results/Exponential_int_arr.png)







