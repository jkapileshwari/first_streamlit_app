import streamlit

streamlit.title('new healty diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞avacado toast')


streamlit.header(' 🍌🥭Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


#lets put a picklist
#streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))


#lets display
#streamlit.dataframe(my_fruit_list)

streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),["Apple","Banana"])
streamlit.dataframe(my_fruit_list)
