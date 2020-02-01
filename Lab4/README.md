# Boston House Price Prediction Based on Linear Regression Analysis
This project proves that Boston house prices are generally directly proportional to the average number of rooms in the house, and a linear regression model of Boston house prices is established.

## Table of Contents
- [Background](#background)
- [Running result](#running-result)
- [Maintainers](#maintainers)

## Background
1. First import the data set and analyze the data: The Boston data set has 506 samples and 13 feature variables.

2. Perform feature analysis on the independent variables and draw scatter plots to analyze the correlation between the dependent variable and the independent variables and remove irrelevant data. According to the scatter plot analysis, the characteristics of the house's 'RM (rooms per house)', 'LSTAT (how many landlords in the area belong to the low-income group)', 'PTRATIO' The correlation is greatest, so the remaining unrelated features are eliminated.

3. Build a Boston house price prediction model. Through analysis, we can see that the average number of rooms in a house is generally positively related to the final house price.

## Running result
The process of gradient descent is ploted:
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab4/Gradient%20descent.png"/>
</p>
The linear regression curve fits the distribution of historical data, thus proving the feasibility of linear regression.
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab4/Linear%20regression%20result.png"/>
</p>
Thus, Boston house price prediction model is: y=10.67*x-44.65 (x:RM y:House price)

## Maintainers
[@Jianeng](https://github.com/jianengli).
