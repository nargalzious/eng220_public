# -*- coding: utf-8 -*-



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

file_path = "https://raw.githubusercontent.com/kassandrasage24-ctrl/ENG220-19/refs/heads/main/global_water_consumption.csv"
water = pd.read_csv(file_path)

# Assuming 'water' DataFrame is already loaded from previous cells.

st.title("Water Consumption and Scarcity Analysis")

# Graph 1: Rainfall Impact vs. Groundwater Depletion Rate (%)
st.header("Rainfall Impact vs. Groundwater Depletion Rate (%)")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Rainfall Impact (Annual Precipitation in mm)', y='Groundwater Depletion Rate (%)', data=water, ax=ax1)
ax1.set_title('Rainfall Impact vs. Groundwater Depletion Rate (%)')
ax1.set_xlabel('Rainfall Impact (Annual Precipitation in mm)')
ax1.set_ylabel('Groundwater Depletion Rate (%)')
st.write("Rainfall Impact vs. Groundwater Depletion Rate (%)")
st.pyplot(fig1)
ax1.grid(True)


# Graph 2: Total Water Consumption vs. Groundwater Depletion Rate
st.header("Total Water Consumption vs. Groundwater Depletion Rate")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Total Water Consumption (Billion Cubic Meters)', y='Groundwater Depletion Rate (%)', data=water, ax=ax2)
ax2.set_title('Total Water Consumption vs. Groundwater Depletion Rate')
ax2.set_xlabel('Total Water Consumption (Billion Cubic Meters)')
ax2.set_ylabel('Groundwater Depletion Rate (%)')
st.write("Total Water Consumption vs. Groundwater Depletion Rate")
st.pyplot(fig2)
ax2.grid(True)


# Graph 3: Water Scarcity Level Distribution
st.header("Water Scarcity Level Distribution")
fig3, ax3 = plt.subplots(figsize=(8, 8))
counts = water["Water Scarcity Level"].value_counts()
ax3.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
ax3.set_title("Water Scarcity Level Distribution")
st.write("Water Scarcity Level Distribution")
st.pyplot(fig3)

# graph 4 Katies graph
st.header("Total water consumption, Rainfall, and Groundwater Depletion")
df = water[(water['Year'] >= 2000) & (water['Year'] <= 2024)]

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
numeric_cols = [col for col in numeric_cols if col not in ['Year']]

for col in numeric_cols:
    fig4, ax4 = plt.subplots(figsize=(12, 7))

    for country, data in df.groupby('Country'):
      if country.lower() in ['united kingdom', 'uk', 'great britain']:
        #bright red line for the UK
        ax4.plot(data['Year'], data[col], label=country, color='#FF0000', linewidth=2.5)
      else:
        # Use the default style for other countries
        ax4.plot(data['Year'], data[col], label=country, alpha=0.7)

    #for country, data in df.groupby('Country'):
        #plt.plot(data['Year'], data[col], label=country)

    ax4.set_title(f'{col} by Country (2000–2024)', fontsize=14)
    ax4.set_xlabel('Year', fontsize=12)
    ax4.set_ylabel(col, fontsize=12)
    ax4.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    ax4.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig4)
 
 #Graph 5 sasha graph
st.header ("Water Usage By Entity")
data_2024 = water[water["Year"] == 2024]
average_ind = data_2024['Industrial Water Use (%)'].mean()
average_house = data_2024['Household Water Use (%)'].mean()
average_ag = data_2024['Agricultural Water Use (%)'].mean()

world_values = [average_ind, average_ag, average_house]
world_labels = ["Industrial", "Agricultural", "Household"]

fig5, ax5 =plt.subplots(figsize=(6,6))
ax5.pie(world_values, labels=world_labels, autopct="%1.1f%%")
ax5.set_title("World Average Water Usage Breakdown (2024)")
st.pyplot(fig5)