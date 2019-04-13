# Communicating-data-findings
This repository has two parts that demonstrate the importance and value of data visualization techniques in the data analysis process. In the first part,  Python visualization libraries are used to systematically explore a selected dataset, starting from plots of single variables and building up to plots of multiple variables. In the second part,a short presentation that illustrates interesting properties, trends, and relationships that is discovered in selected dataset. The primary method of conveying findings will be through transforming exploratory visualizations from the first part into polished, explanatory visualizations.

Project overview
Data Overview
The dataset has been chosen from the options provided by Udacity.The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics (BTS) tracks the on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled and diverted flights appears in DOT's monthly Air Travel Consumer Report, published about 30 days after the month's end, as well as in summary tables posted on this website. BTS began collecting details on the causes of flight delays in June 2003. Summary statistics and raw data are made available to the public at the time the Air Travel Consumer Report is released.

The datset used here reports flights in the United States, including carriers, arrival and departure delays,in 1987.

Key points from exploratory analysis
The histogram depicting distribution of total delays shows that majority of the delays are within 25 minutes,and the number decreases significantly as the duration increases.This shows that major delays are few and if we reduce the minor delays air transport will be optimised and those delays with high negative values are actually outliers.

A barplot is plotted between total delay and unique carrier.Here quantitative variable has been plotted against qualitative variable.In the explanatory analysis the plot has been polished with proper labels and title.

For a clear analysis of delays with carrier month wise analysis has also been plotted with proper labels so as to see how the total delay is distributed for each month.

A pie chart depicting which carrier constitutes major proportion in the dataset has been plotted in the exploratory but it could be related to total delays.

The scatterplot does not depict any clear relation between distance and total delay as the data points are present as clusters.The same plot has been properly labelled in explanatory analysis with appropriate conclusions.

The scatterplot for distance vs actual elapsed time does depict some sort of linear relation.The correlation coefficient calculated also has a high value of 0.97 which shows that there's strong positive correlation between distance and actual elapsed time.Regression analysis has been performed in the exploratory analysis to give a clear insight.

For each of the scatter plot in the multivariate visualisation for distance vs total delay on month basis correlation coefficient has been calculated.The correlation coefficient for each of them is quite close to zero which depicts that there is no relation between diatance and total delay. Also the scatter plot is similar to that of distance vs total delay as a whole depicting that the two features are independent.

At last cluster analysis has been performed for total delay vs distance with initially two clusters.By using elbow method it has been found that seven is optimal number of clusters for the given scatter plot,which been then plotted below.But nothing could be concluded from it.It may be used for machine learning on this dataset.

This is the link for the dataset

https://www.google.com/url?q=http://stat-computing.org/dataexpo/2009/the-data.html&sa=D&ust=1555126089948000
