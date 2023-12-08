import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#-----Lesson12
streamlit.title('-------------------------------------')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

#-----Lesson12++
my_data_rows_all = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows_all)
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows_all)

#-----Lesson12+
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)



streamlit.title('-------------------------------------')
streamlit.title('My Parents New Healthy Dinner- DUDE')
streamlit.title('My Parents New Healthy Dinner- 1')
streamlit.title('My Parents New Healthy Dinner- 2')
streamlit.title('My Parents New Healthy Dinner- 3')
streamlit.title('My Parents New Healthy Dinner- 4')

   
streamlit.header('🥗Breakfast Menu')
streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞🥣 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#create function
streamlit.header('🍌🥭 FRUITY FUNCTION BUTTON 🥝🍇')
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

# add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

#======================================
streamlit.header('🍌🥭 FRUITY VICE  Query API! 🥝🍇')
#create function
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized


try:
   fruit_choice = streamlit.text_input('What fruit woud you like information about?','kiwi')
   if not fruit_choice:
          streamlit.error("please select a fruit to get information.")
   else:
         back_from_function = get_fruityvice_data(fruit_choice)
         streamlit.dataframe(back_from_function)
except URLError as e:
      streamlit.error()   

#======================================
streamlit.header('🍌🥭 ADD FRUIT TO LIST! 🥝🍇')
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('from streamlit')")
        return "thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add to the Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
   
-streamlit.stop();
#-----Lesson12+++
#add_my_fruit = streamlit.text_input('What fruit would you like to add to the list?','jackfruit')
#my_cur.execute("insert into fruit_load_list values('"+ add_my_fruit +"')")
#streamlit.write('thanks for adding ',add_my_fruit)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())  #just writes data to screen
