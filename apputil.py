import plotly.express as px
import pandas as pd

# Exercise 1
def survival_demographics(df):
    # Step 1: create AgeGroup column
    df['AgeGroup'] = pd.cut(
        df['Age'],
        bins=[0, 12, 19, 59, 120],
        labels=['Child', 'Teen', 'Adult', 'Senior']
    )
    
    # Step 2 + 3: group and calculate
    grouped = df.groupby(['Pclass', 'Sex', 'AgeGroup'])
    
    # Step 4: aggregate
    result = grouped['Survived'].agg(
        n_passengers="count",
        n_survivors="sum",
        survival_rate="mean"
    ).reset_index()
    
    
     # Step 5: sort result by survival_rate descending
    result = result.sort_values(
        by=['Pclass', 'Sex', 'survival_rate'], 
        ascending=[True, True, False]
    )
  
    return result

# Step 6 + 7: create visualization function
def visualize_demographic(df_result):
    subset = df_result[(df_result['Pclass'] == 3) & (df_result['AgeGroup'].isin(['Child', 'Adult']))]
    
    fig = px.bar(
        subset,
        x="AgeGroup",
        y="survival_rate",
        color="Sex",
        barmode="group",
        text="survival_rate",   # adds numbers on bars
        title="Survival Rate: Children vs Adults in 3rd Class",
        hover_data={
            "n_passengers": True,
            "n_survivors": True,
            "survival_rate": ':.2f'   # format to 2 decimal places
        }
    )
    
    fig.update_traces(
        texttemplate='%{text:.2f}',
    textposition='outside',
    hovertemplate="Age Group: %{x}<br>Survival Rate: %{y:.2%}<br>Passengers: %{customdata[0]}<br>Survivors: %{customdata[1]}<extra></extra>"
    )  # format as %
    
    return fig