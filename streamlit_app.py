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
my_fruit_list = my_fruit_list.set_index(Fruit)
#pick specific fruits
streamlit.multiselect('Pick fruit of your choice:',list( my_fruit_list.index))
#After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:
streamlit.dataframe(my_fruit_list)



