import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('🥗 🐔 🥑Breakfast Menu')
streamlit.text(' 🐔 🥑diary Milk')
streamlit.text(' 🥑Milk')
streamlit.header(' 🥑 🥑 🥑 🥑Build Your Own Chocolate')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
               
