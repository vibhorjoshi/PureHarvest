import openai
import os
import streamlit as st
from dotenv import load_dotenv
import json
# load .env file
load_dotenv()
st.set_page_config(page_title="PUREHARVEST")
st.header("PUREHARVEST")

# set up open ai key 
client=openai.OpenAI(api_key=os.getenv('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'))

# chat based language model system
system_messages=""
def get_personalized_recipes(prompt):
     completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_messages},
            {"role": "user", "content": prompt}
        ]
    )
     return completion.choices[0].message.content

def display_recipe(recipe):
     st.header(recipe['name'])
     st.subheader('Ingredients')
     ingredients = "\n".join("- " + i for i in recipe['ingredients'])
st.write('Ingredients')

st.subheader('Instructions')
st.write(display_recipe["instructions"])

st.write("⏰ Cooking time: " + str(display_recipe["cooking_time"]) + " minutes")

st.write("Servings: " + str(display_recipe["servings"]))

# Add Cuisine Type
st.write("Cuisine Type: " + display_recipe["cuisine_type"])




    




