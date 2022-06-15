import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥣 Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado toast')

#add header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#PANDAS-python package library
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set index to pick as fruit name
my_fruit_list = my_fruit_list.set_index('Fruit')
#pick specific fruits, create a variable and store the value
fruits_selected=streamlit.multiselect('Pick fruit of your choice:',list( my_fruit_list.index),['Avocado','Strawberries'])
#assign value to a variable
fruits_to_show= my_fruit_list.loc[fruits_selected]
#After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:
streamlit.dataframe(fruits_to_show)


#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('what fruit would you like information about?'+'kiwi')
streamlit.write('The user entered', fruit_choice)
                                  
#calling API from Streamlit
import requests
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#Let's Get the Fruityvice Data Looking a Little Nicer
#take the json response from above and make it normalized
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#dataframe implies output to be displayed as table format
streamlit.dataframe(fruityvice_normalized)

