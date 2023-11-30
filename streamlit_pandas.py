import streamlit
import pandas

streamlit.title('Import File From 3s Bucket - Snowflake course2:lesson3')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# lets pick the list
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#display the data
streamlit.dataframe(my_fruit_list)
