import streamlit as st

from apputil import *
from apputil import survival_demographics, visualize_demographic
from apputil import family_groups, last_names, visualize_families

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Generate survival demographics table
df_result = survival_demographics(df)

st.subheader("Titanic Visualization 1")
st.write("Question: Were children in third class more likely to survive than adults in third class?")
                 
# Generate and display the figure
fig1 = visualize_demographic(df_result)
st.plotly_chart(fig1, use_container_width=True)



st.subheader("Last Names vs Family Size")
st.write("We compare surname counts with family sizes from the grouped table.")
st.write(last_names(df).head(15))
         
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)



df_result2 = family_groups(df)

st.subheader("Exercise 2: Family Size and Wealth")
st.write("Do larger families tend to pay lower fares on average?")
st.write(last_names(df).head(15))

fig3 = visualize_families(df_result2)
st.plotly_chart(fig3, use_container_width=True)