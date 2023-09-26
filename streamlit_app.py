import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# store fruits selected
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# create lf fruits to show from fruits selected
fruits_to_show = my_frist ouit_list.loc[fruits_selected]

# display fruits_to_show instead of the entire list
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
import requests
streamlit.header("Fruityvice Fruit Advice!")

# get user input
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "watermelon")
# streamlit.text(fruityvice_response.json())

# normalize json version of response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as a table
streamlit.dataframe(fruityvice_normalized)


