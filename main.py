import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import plotly.graph_objects as go
import streamlit as st

st.title('Covid-19 Analysis')
covid_df=pd.read_csv(r'C:\Users\KIIT\Desktop\Project Covid 19 data analysis\worldometer_data.csv')

st.title('Country vs Total Cases')
fig1=px.bar(covid_df,x=covid_df['Country/Region'],y=covid_df['TotalCases'],color=covid_df['Population'])
st.plotly_chart(fig1)

st.title(' Continent vs Total Cases')
fig2=px.pie(values=covid_df['TotalCases'].values,names=covid_df['Continent'])
st.plotly_chart(fig2)

st.title('Total Cases vs Total Recovered')
fig3=go.Figure()
fig3.add_trace(go.Scatter(x=covid_df['TotalCases'],y=covid_df['TotalRecovered'],mode='lines+markers',
                    name='lines+markers',line=dict(color='Purple',width=4), text=covid_df['Country/Region']))
fig3.update_layout(xaxis_title='TotalCases',yaxis_title='TotalRecovered')
st.plotly_chart(fig3)

st.title('Total cases vs Total Deaths')
fig4=go.Figure()
fig4.add_trace(go.Scatter(x=covid_df['TotalCases'],y=covid_df['TotalDeaths'],mode='lines+markers',
                    name='lines+markers',
                    line=dict(color='Yellow',width=4),text=covid_df['Country/Region']))
fig4.update_layout(xaxis_title='Total Cases',yaxis_title='Total Deaths')
st.plotly_chart(fig4)
st.title('Total Test vs Country Region')
fig5=px.bar(covid_df,x=covid_df['Country/Region'],y=covid_df['TotalTests'],color=covid_df['ActiveCases'])
st.plotly_chart(fig5)

country_list=covid_df['Country/Region'].values
st.header('Select a Country')
selectvalues=st.selectbox('Select Country from Dropdown',country_list)

def country_statis(c_name):
    return(covid_df[covid_df['Country/Region']==c_name])
if st.button('Show'):
    st.table(country_statis(selectvalues))

st.title('Day Wise Analysis')
date_df=pd.read_csv(r'C:\Users\KIIT\Desktop\Project Covid 19 data analysis\day_wise.csv')
st.title('Date vs Active Cases')
fig6=px.bar(date_df,x=date_df['Date'],y=date_df['Confirmed'],color=date_df['Deaths'])
st.plotly_chart(fig6)
px.scatter(date_df,x=date_df['Date'], y=date_df['New cases'],size=date_df['New cases'],title='New Cases vs Date')
st.title('New Cases vs New Recovered')
fig7=go.Figure()
fig7.add_trace(go.Scatter(x=date_df['Date'],y=date_df['New recovered'],mode='lines+markers',name='New recovered'))
fig7.add_trace(go.Scatter(x=date_df['Date'],y=date_df['New cases'],mode='lines+markers',name='New cases',line=dict(color='Red')))
fig7.add_trace(go.Scatter(x=date_df['Date'],y=date_df['New deaths'],mode='lines+markers',name='New deaths',line=dict(color='greenyellow')))
fig7.update_layout(xaxis_title='Date',yaxis_title='Population')
st.plotly_chart(fig7)
grouped_df=pd.read_csv(r'C:\Users\KIIT\Desktop\Project Covid 19 data analysis\full_grouped.csv')
def daywisereport(gr_cnames,gr_date):
   return (grouped_df[(grouped_df['Country/Region']==gr_cnames)&(grouped_df['Date']==gr_date)])
country_region_list=grouped_df['Country/Region'].unique()
date_list=grouped_df['Date'].unique()
st.title('Specific Day Report')
selectvalues1=st.selectbox('Select country',country_region_list)
selectvalues2=st.selectbox('Select Date',date_list)
if st.button('Search'):
    st.table(daywisereport(selectvalues1,selectvalues2))