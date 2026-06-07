import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("games.csv")

# Title
st.title("🎮 Game Analytics Dashboard")

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Games", len(df))

with col2:
    st.metric(
        "Total Revenue (Million USD)",
        round(df["estimated_revenue_million_usd"].sum(), 2)
    )

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.set_page_config(
    page_title="Game Analytics Dashboard",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Game Analytics Dashboard")
st.markdown("Analyze game sales, score, revenue and trends")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Games", len(df))
col2.metric("Total Revenue", f"${df['estimated_revenue_million_usd'].sum():,.0f}M")
col3.metric("Avg Rating", round(df['user_score'].mean(),2))
col4.metric("Total Sales", round(df['global_sales_million'].sum(),2))
st.sidebar.header("Filters")

genre = st.sidebar.multiselect(
    "Genre",
    df["genre"].unique()
)

platform = st.sidebar.multiselect(
    "Platform",
    df["platform"].unique()
)
import plotly.express as px

fig = px.pie(
    df,
    names="genre",
    title="Genre Distribution"
)

st.plotly_chart(fig, use_container_width=True)
fig = px.scatter(
    df,
    x="user_score",
    y="estimated_revenue_million_usd",
    color="genre",
    hover_name="title"
)

st.plotly_chart(fig, use_container_width=True)
top_games = df.sort_values(
    "global_sales_million",
    ascending=False
).head(10)

fig = px.bar(
    top_games,
    x="title",
    y="global_sales_million"
)

st.plotly_chart(fig)
game = st.text_input("Search Game")

if game:
    result = df[df["title"].str.contains(
        game,
        case=False,
        na=False
    )]

    st.dataframe(result)
csv = df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "filtered_games.csv",
    "text/csv"
)
tab1, tab2, tab3 = st.tabs(
    ["Overview", "Sales Analysis", "Game Search"]
)


