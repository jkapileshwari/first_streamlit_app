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
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),["'Lime','Banana'"])


#lets display
streamlit.dataframe(my_fruit_list)

##fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))
#fruits_to_show = my_fruit_list.loc[fruits_selected]



#streamlit.dataframe(fruits_to_show)
