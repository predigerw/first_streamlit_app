import streamlit
import pandas
import requests

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega 3 and Blueberry Meal")

streamlit.text("🥗 Kale, Spinach and Rocket Smoothie")

streamlit.text("🐔 Hard-Boiled Free-Range Egg")

streamlit.text("🥑 🍞 Avocado Toast")

streamlit.header("🍌🥭 Build your own fruit smoothie 🥝🍇")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")


#let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("pick some fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#streamlit.multiselect("pick some fruits", list(my_fruit_list.Fruit))

fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table on the page
streamlit.dataframe(fruits_to_show)

#new section to display the fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Watermelon")
streamlit.text(fruityvice_response.json())

#now we normalize the view
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
