import streamlit
import pandas

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
streamlit.multiselect("pick some fruits", list(my_fruit_list.index,['Avocado', 'Strawberries'])
#streamlit.multiselect("pick some fruits", list(my_fruit_list.Fruit))

#display the table on the page
streamlit.dataframe(my_fruit_list)
