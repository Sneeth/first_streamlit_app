import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('🥗 🐔 🥑Breakfast Menu')
streamlit.text(' 🐔 🥑diary Milk')
streamlit.text(' 🥑Milk')
streamlit.header(' 🥑 🥑 🥑 🥑Build Your Own Chocolate')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries','Grapes'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
import requests
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon)
#fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)

fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi)
streamlit.write('The user entered', fruit choice)
import requests
fruityvice_requests=requets.get("https:fruityvice.com/api/fruit/"+fruit_choice)
                                  
