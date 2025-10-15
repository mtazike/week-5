import pandas as pd
import plotly.express as px

# Exercise 1
def survival_demographics(df):
    # Step 1: create AgeGroup column as categorical
    df['AgeGroup'] = pd.cut(
        df['Age'],
        bins=[0, 12, 19, 59, 120],
        labels=['Child', 'Teen', 'Adult', 'Senior']
    ).astype('category')   # categorical dtype

    # Step 2+3: group and calculate
    grouped = df.groupby(['Pclass', 'Sex', 'AgeGroup'])

    # Step 4: aggregate
    result = grouped['Survived'].agg(
        n_passengers="count",
        n_survivors="sum",
        survival_rate="mean"
    ).reset_index()

    # Step 5: sort results for clarity
    result = result.sort_values(
        by=['Pclass', 'Sex', 'survival_rate'],
        ascending=[True, True, False]
    )

    return result

# Visualization for Exercise 1
def visualize_demographic(df_result):
    fig = px.bar(
        df_result,
        x="AgeGroup",
        y="survival_rate",
        color="Sex",
        barmode="group",
        text="survival_rate",
        title="Survival Rate by Age Group and Sex",
        hover_data=["n_passengers", "n_survivors", "survival_rate"]
    )
    fig.update_traces(
        texttemplate='%{text:.2f}',
        textposition='outside'
    )
    return fig



# Exercise 2
def family_groups(df):
    # Step 1: family_size
    df['family_size'] = df['SibSp'] + df['Parch'] + 1

    # Step 2: group
    grouped = df.groupby(['family_size', 'Pclass']).agg(
        n_passengers=('PassengerId', 'count'),
        avg_fare=('Fare', 'mean'),
        min_fare=('Fare', 'min'),
        max_fare=('Fare', 'max')
    ).reset_index()

    # Step 3: sort for clarity
    grouped = grouped.sort_values(by=['Pclass', 'family_size']).reset_index(drop=True)

    return grouped


def last_names(df):
    # Extract and count last names
    df['LastName'] = df['Name'].apply(lambda x: x.split(',')[0].strip())
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
