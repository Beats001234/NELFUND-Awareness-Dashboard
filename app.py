import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Data
@st.cache_data
def load_data():
    data = pd.DataFrame({
        "Geopolitical Zone": ["North Central", "North East", "North West", "South East", "South West", "South South"],
        "Total Target Audience": [50000, 45000, 60000, 55000, 70000, 65000],
        "Workshops Conducted": [20, 18, 25, 22, 30, 27],
        "Campus Roadshows": [10, 12, 15, 14, 18, 20],
        "TV/Radio Campaigns": [5, 6, 7, 8, 9, 10],
        "Social Media Reach": [100000, 95000, 110000, 105000, 130000, 120000],
        "SMS Campaigns": [20000, 15000, 25000, 22000, 28000, 26000],
        "NGO Partnerships": [8, 10, 12, 14, 16, 18],
        "Application Conversion Rate (%)": [12, 10, 15, 13, 18, 16]
    })
    return data

data = load_data()

# Streamlit App Layout
st.title("📊 NELFUND Sensitization Dashboard")
st.sidebar.header("Filter Options")

# Dropdown for selecting a region
zone = st.sidebar.selectbox("Select Geopolitical Zone", ["All"] + list(data["Geopolitical Zone"]))

# Filter data
if zone != "All":
    data = data[data["Geopolitical Zone"] == zone]

# Display Data
st.write("### Sensitization Metrics")
st.dataframe(data)

# Bar Chart - Total Audience Reached
fig = px.bar(data, x="Geopolitical Zone", y="Total Target Audience", color="Geopolitical Zone",
             title="Total Audience Reached Per Zone")
st.plotly_chart(fig)

# Line Chart - Workshops & Roadshows
fig2 = px.line(data, x="Geopolitical Zone", y=["Workshops Conducted", "Campus Roadshows"],
               title="Workshops & Roadshows Conducted", markers=True)
st.plotly_chart(fig2)

# Pie Chart - Distribution of Marketing Strategies
fig3 = px.pie(data, names="Geopolitical Zone", values="Social Media Reach",
              title="Social Media Engagement Across Zones")
st.plotly_chart(fig3)

# Heatmap - Sensitization Activities
fig4 = go.Figure(data=go.Heatmap(
    z=[data["Workshops Conducted"], data["Campus Roadshows"], data["TV/Radio Campaigns"],
       data["Social Media Reach"], data["SMS Campaigns"], data["NGO Partnerships"]],
    x=data["Geopolitical Zone"],
    y=["Workshops", "Roadshows", "TV/Radio", "Social Media", "SMS", "NGO Partnerships"],
    colorscale="Viridis"))
fig4.update_layout(title="Heatmap of Sensitization Activities")
st.plotly_chart(fig4)

# Map Visualization (Placeholder for actual coordinates)
data_map = pd.DataFrame({
    "lat": [9.082, 11.823, 12.002, 6.524, 7.377, 4.815],
    "lon": [8.675, 13.151, 8.500, 7.495, 3.947, 7.049],
    "Geopolitical Zone": ["North Central", "North East", "North West", "South East", "South West", "South South"],
    "Total Audience": data["Total Target Audience"]
})
fig5 = px.scatter_mapbox(data_map, lat="lat", lon="lon", size="Total Audience",
                         hover_name="Geopolitical Zone", mapbox_style="open-street-map",
                         title="Geographical Distribution of Sensitization Reach")
st.plotly_chart(fig5)

st.write("### Insights & Recommendations")
st.markdown("- **Focus more on high-engagement zones (e.g., South West, North West).**")
st.markdown("- **Increase radio and TV outreach in underperforming areas.**")
st.markdown("- **Leverage NGO partnerships for rural penetration.**")
