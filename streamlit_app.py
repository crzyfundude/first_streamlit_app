import streamlit
import snowflake.connector
#-----Lesson12
streamlit.title('-------------------------------------')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
#-----Lesson12+++

add_my_fruit = streamlit.text_input('What fruit would you like to add to the list?','jackfruit')
streamlit.write('The user entered',fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())  #just writes data to screen

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
