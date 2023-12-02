import streamlit
import pandas

streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())  #just writes data to screen

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as table
streamlit.dataframe(fruityvice_normalized)
