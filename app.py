import streamlit as st
import matplotlib.pyplot as plt

# Hardcoded data
data = [
    {"name": "Microsoft", "Topics": {"Health": 0.6, "Sports": 0.2, "Customer Experience": 0.2}},
    {"name": "Apple", "Topics": {"Innovation": 0.5, "Privacy": 0.3, "Customer Experience": 0.2}},
    {"name": "Google", "Topics": {"Data Privacy": 0.4, "Innovation": 0.4, "Advertising": 0.2}},
    {"name": "Amazon", "Topics": {"E-commerce": 0.5, "Cloud Services": 0.3, "Sustainability": 0.2}},
    {"name": "Tesla", "Topics": {"Innovation": 0.6, "Sustainability": 0.3, "Regulations": 0.1}},
    {"name": "Meta", "Topics": {"Social Media": 0.5, "Data Privacy": 0.3, "Regulations": 0.2}},
    {"name": "Netflix", "Topics": {"Streaming": 0.6, "Content Quality": 0.3, "Partnerships": 0.1}},
    {"name": "Spotify", "Topics": {"Music Streaming": 0.6, "Partnerships": 0.3, "Advertising": 0.1}},
    {"name": "Samsung", "Topics": {"Innovation": 0.5, "Customer Experience": 0.3, "Sustainability": 0.2}},
    {"name": "Intel", "Topics": {"Chip Innovation": 0.5, "Sustainability": 0.3, "AI": 0.2}},
    {"name": "IBM", "Topics": {"Cloud": 0.4, "AI": 0.4, "Sustainability": 0.2}},
    {"name": "Oracle", "Topics": {"Cloud": 0.5, "Security": 0.3, "Customer Experience": 0.2}},
    {"name": "Salesforce", "Topics": {"CRM": 0.5, "Innovation": 0.3, "Sustainability": 0.2}},
    {"name": "Adobe", "Topics": {"Creativity Tools": 0.6, "Cloud": 0.3, "Privacy": 0.1}},
    {"name": "Nvidia", "Topics": {"AI": 0.5, "Graphics": 0.3, "Gaming": 0.2}},
    {"name": "Uber", "Topics": {"Mobility": 0.5, "Regulations": 0.3, "Sustainability": 0.2}},
    {"name": "Airbnb", "Topics": {"Hospitality": 0.6, "Regulations": 0.2, "Sustainability": 0.2}},
    {"name": "Boeing", "Topics": {"Aviation": 0.6, "Innovation": 0.3, "Safety": 0.1}},
    {"name": "Coca-Cola", "Topics": {"Health": 0.4, "Sustainability": 0.4, "Customer Experience": 0.2}},
    {"name": "PepsiCo", "Topics": {"Health": 0.5, "Sustainability": 0.3, "Marketing": 0.2}},
    {"name": "Procter & Gamble", "Topics": {"Health": 0.4, "Sustainability": 0.4, "Customer Experience": 0.2}},
    {"name": "Nike", "Topics": {"Sports": 0.6, "Innovation": 0.3, "Sustainability": 0.1}},
    {"name": "Adidas", "Topics": {"Sports": 0.6, "Sustainability": 0.3, "Customer Experience": 0.1}},
    {"name": "L'Oréal", "Topics": {"Beauty": 0.5, "Sustainability": 0.3, "Innovation": 0.2}},
    {"name": "Unilever", "Topics": {"Sustainability": 0.5, "Health": 0.3, "Innovation": 0.2}},
    {"name": "Pfizer", "Topics": {"Health": 0.6, "Innovation": 0.3, "Regulations": 0.1}},
    {"name": "Johnson & Johnson", "Topics": {"Health": 0.6, "Sustainability": 0.2, "Innovation": 0.2}},
    {"name": "Volkswagen", "Topics": {"Automotive": 0.5, "Sustainability": 0.3, "Innovation": 0.2}},
    {"name": "Toyota", "Topics": {"Automotive": 0.5, "Sustainability": 0.3, "Customer Experience": 0.2}},
    {"name": "Sony", "Topics": {"Entertainment": 0.5, "Gaming": 0.3, "Innovation": 0.2}},
    {"name": "Dell", "Topics": {"Computing": 0.5, "Sustainability": 0.3, "Customer Experience": 0.2}},
]

# Streamlit app
st.title("Company Topic Visualization")

# Dropdown to select a company
company_names = [d["name"] for d in data]
selected_company = st.selectbox("Select a company:", company_names)

# Find the data for the selected company
company_data = next(item for item in data if item["name"] == selected_company)
topics = company_data["Topics"]

# Display a pie chart of the topics
fig, ax = plt.subplots()
ax.pie(topics.values(), labels=topics.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
