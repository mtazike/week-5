import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Generate survival demographics table
df_result = survival_demographics(df)

st.subheader("Titanic Visualization 1")
st.write("Question: Were children in third class more likely to survive than adults in third class?")
                 
# Generate and display the figure
fig1 = visualize_demographic(df_result)
st.plotly_chart(fig1, use_container_width=True)



st.write(""".......""")
         
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)