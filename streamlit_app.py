import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("Select * from fruit_load_list")
        return my_cur.fetchall()
    
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('" + new_fruit "')")
        return "Thanks for adding" + add_my_fruit    

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


try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit to receive information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()




streamlit.header("View our fruit list - Add your favourites")

        
if streamlit.button("Get fruit list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
   

add_my_fruit = streamlit.text_input("What fruit would you like to add")    
if streamlit.button("Add a fruit to the list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)


#streamlit.write("Thanks for adding" , add_my_fruit)

#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")

