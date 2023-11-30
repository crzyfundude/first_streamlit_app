import streamlit
import pandas

streamlit.title('Import File From 3s Bucket - Snowflake course2:lesson3')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
