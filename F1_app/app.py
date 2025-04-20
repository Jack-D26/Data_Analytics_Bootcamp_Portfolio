import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
data = pd.read_csv("data/combined_driver_standings.csv")

# Filter from year 2000 onwards
data = data[data['year'] >= 2000]

# Get Top 10 drivers by total points
top_10_drivers = (
    data.groupby('driverRef')['points'].sum()
    .sort_values(ascending=False)
    .head(10)
    .index.tolist()
)

# Chart 1 – Total points by driver (Top 10)
st.header("Total Points by Driver (Top 10)")

points_by_driver = data.groupby('driverRef')['points'].sum().reset_index()
points_by_driver = points_by_driver[points_by_driver['driverRef'].isin(
    top_10_drivers)]
points_by_driver = points_by_driver.sort_values('points', ascending=False)

fig1 = px.bar(
    points_by_driver,
    x='points',
    y='driverRef',
    orientation='h',
    title="Total Points by Driver (Top 10)",
    labels={'points': 'Total Points', 'driverRef': 'Driver'},
    text='points'
)
fig1.update_traces(texttemplate='%{text:.0f}', textposition='outside')
st.plotly_chart(fig1, use_container_width=True)

st.markdown(
    "This chart shows the total accumulated points by the most successful F1 drivers since the year 2000."
)

# Chart 2 – Wins by driver in selected years
st.header("Wins by Driver in Selected Years (Top 10)")

selected_years = st.multiselect(
    "Select one or more years:",
    options=sorted(data['year'].unique()),
    default=[2022]
)

victories_by_driver = (
    data[data['year'].isin(selected_years) & (data['wins'] > 0)]
    .groupby('driverRef')['wins'].sum()
    .reset_index()
)
victories_by_driver = victories_by_driver[victories_by_driver['driverRef'].isin(
    top_10_drivers)]

fig2 = px.bar(
    victories_by_driver,
    x='driverRef',
    y='wins',
    color='driverRef',
    title="Wins by Driver in Selected Years (Top 10)",
    labels={'wins': 'Wins', 'driverRef': 'Driver'},
    text='wins'
)
fig2.update_traces(texttemplate='%{text:.0f}', textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    "This chart shows the number of wins per driver in the selected years."
)

# Chart 3 – Cumulative points over time
st.header("Cumulative Points by Year (Top 10 Drivers)")

selected_year = st.slider(
    "Select a year:", min_value=2000, max_value=2024, value=2022
)

filtered_data = data[data['year'] <= selected_year]

cumulative_points = (
    filtered_data.groupby(['year', 'driverRef'])['points']
    .sum()
    .groupby(level=1).cumsum()
    .reset_index()
)

cumulative_points = cumulative_points[cumulative_points['driverRef'].isin(
    top_10_drivers)]

fig3 = px.bar(
    cumulative_points[cumulative_points['year'] == selected_year],
    x='driverRef',
    y='points',
    color='driverRef',
    title=f"Cumulative Points by Driver up to {selected_year} (Top 10)",
    labels={'points': 'Cumulative Points', 'driverRef': 'Driver'},
    text='points'
)
fig3.update_traces(texttemplate='%{text:.0f}', textposition='outside')
st.plotly_chart(fig3, use_container_width=True)

st.markdown(
    f"This chart shows how each top driver's points have accumulated up to {selected_year}."
)
