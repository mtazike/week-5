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
        title="Survival Rate: Children vs Adults in 3rd Class (by Sex)",
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


# Exercise 2
def family_groups(df):
    # Step 1: Create family_size column
    df['family_size'] = df['SibSp'] + df['Parch'] + 1  

    # Step 2: Group by family_size and Pclass
    grouped = df.groupby(['family_size', 'Pclass']).agg(
        n_passengers=('PassengerId', 'count'),
        avg_fare=('Fare', 'mean'),
        min_fare=('Fare', 'min'),
        max_fare=('Fare', 'max')
    ).reset_index()

    # NEW: sort for clarity
    grouped = grouped.sort_values(by=['Pclass', 'family_size']).reset_index(drop=True)

    return grouped


def last_names(df):
    # Extract last names
    df['LastName'] = df['Name'].apply(lambda x: x.split(',')[0].strip())
    # Count them
    last_name_counts = df['LastName'].value_counts()
    return last_name_counts


def visualize_families(df_result):
    fig = px.scatter(
        df_result,
        x="family_size",
        y="avg_fare",
        size="n_passengers",
        color="Pclass",
        hover_data=["min_fare", "max_fare"],
        title="Family Size vs Fare by Class (Bubble = Number of Passengers)"
    )
    fig.update_traces(marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
    return fig
