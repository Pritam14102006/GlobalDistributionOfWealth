import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Global Wealth Distribution Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f4788;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f4788;
    }
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🌍 Global Wealth Distribution Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Interactive Analysis of Global Economic Inequality</p>', unsafe_allow_html=True)

# Data Preparation
wealth_distribution_data = {
    'Wealth_Band': ['>$1 million', '$100k – $1 million', '$10k – $100k', '<$10k'],
    'Number_of_Adults_Millions': [60, 628, 1570, 1550],
    'Percentage_of_Adults': [1.6, 16.4, 41.3, 40.7],
    'Total_Wealth_Trillions': [226.47, 184.51, 56.82, 2.71],
    'Percentage_of_Wealth': [48.1, 39.2, 12.1, 0.6],
    'Order': [1, 2, 3, 4]  # For pyramid ordering
}

df_wealth = pd.DataFrame(wealth_distribution_data)

# Historical data for trends
historical_data = {
    'Year': [2000, 2022, 2027],
    'More_than_1M': [0.4, 1.1, 1.5],
    '100k_to_1M': [5.5, 12.0, 14.8],
    '10k_to_100k': [13.4, 34.4, 37.0],
    'Less_than_10k': [80.7, 52.5, 46.6]
}

df_historical = pd.DataFrame(historical_data)

# Billionaire data
billionaire_data = {
    'Wealth_Band': ['>$100 billion', '$50b – $100b', '$1b – $50b'],
    'Number_of_Individuals': [15, 16, 2860],
    'Percentage_of_Billionaires': [0.5, 0.6, 98.9],
    'Total_Wealth_Trillions': [2.35, 1.15, 12.17],
    'Percentage_of_Billionaire_Wealth': [15.0, 7.3, 77.7]
}

df_billionaires = pd.DataFrame(billionaire_data)

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Global Wealth",
        value="$471T",
        delta="+3.2%"
    )

with col2:
    st.metric(
        label="Global Adult Population",
        value="3.81B",
        delta="+1.8%"
    )

with col3:
    st.metric(
        label="Wealthiest 1.6% Hold",
        value="48.1%",
        delta="+2.1%"
    )

with col4:
    st.metric(
        label="Billionaires",
        value="2,891",
        delta="+145"
    )

st.markdown("---")

# Main Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Wealth Distribution Pyramid")
    
    # Create pyramid chart
    fig_pyramid = go.Figure()
    
    # Reverse order for pyramid (top to bottom)
    colors = ['#1f4788', '#2e5c9a', '#4a7db8', '#6ba3d6']
    
    for i, row in df_wealth.iterrows():
        fig_pyramid.add_trace(go.Bar(
            name=row['Wealth_Band'],
            y=[row['Wealth_Band']],
            x=[row['Percentage_of_Wealth']],
            orientation='h',
            marker_color=colors[i],
            text=[f"{row['Percentage_of_Wealth']}%"],
            textposition='inside',
            hovertemplate=f"<b>{row['Wealth_Band']}</b><br>" +
                          f"Adults: {row['Number_of_Adults_Millions']}M ({row['Percentage_of_Adults']}%)<br>" +
                          f"Wealth: ${row['Total_Wealth_Trillions']}T ({row['Percentage_of_Wealth']}%)<br>" +
                          "<extra></extra>"
        ))
    
    fig_pyramid.update_layout(
        barmode='overlay',
        height=400,
        showlegend=False,
        xaxis_title="Percentage of Global Wealth (%)",
        yaxis_title="Wealth Band",
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        xaxis=dict(range=[0, 55])
    )
    
    st.plotly_chart(fig_pyramid, use_container_width=True)

with col_right:
    st.subheader("💎 Billionaire Wealth Distribution")
    
    fig_billionaires = px.pie(
        df_billionaires,
        values='Total_Wealth_Trillions',
        names='Wealth_Band',
        color_discrete_sequence=['#1f4788', '#4a7db8', '#6ba3d6'],
        hole=0.4
    )
    
    fig_billionaires.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate="<b>%{label}</b><br>" +
                      "Wealth: $%{value}T<br>" +
                      "%{percent}<br>" +
                      "<extra></extra>"
    )
    
    fig_billionaires.update_layout(
        height=400,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=11),
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.1)
    )
    
    st.plotly_chart(fig_billionaires, use_container_width=True)

st.markdown("---")

# Second Row of Visualizations
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("📈 Historical Trends (2000-2027)")
    
    fig_trends = go.Figure()
    
    fig_trends.add_trace(go.Scatter(
        x=df_historical['Year'],
        y=df_historical['More_than_1M'],
        name='>$1M',
        mode='lines+markers',
        line=dict(width=3, color='#1f4788'),
        marker=dict(size=8)
    ))
    
    fig_trends.add_trace(go.Scatter(
        x=df_historical['Year'],
        y=df_historical['100k_to_1M'],
        name='$100k-$1M',
        mode='lines+markers',
        line=dict(width=3, color='#4a7db8'),
        marker=dict(size=8)
    ))
    
    fig_trends.add_trace(go.Scatter(
        x=df_historical['Year'],
        y=df_historical['10k_to_100k'],
        name='$10k-$100k',
        mode='lines+markers',
        line=dict(width=3, color='#6ba3d6'),
        marker=dict(size=8)
    ))
    
    fig_trends.add_trace(go.Scatter(
        x=df_historical['Year'],
        y=df_historical['Less_than_10k'],
        name='<$10k',
        mode='lines+markers',
        line=dict(width=3, color='#a8c8e8'),
        marker=dict(size=8)
    ))
    
    fig_trends.update_layout(
        height=400,
        xaxis_title="Year",
        yaxis_title="Percentage of Global Adults (%)",
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_trends, use_container_width=True)

with col_right2:
    st.subheader("📊 Population vs Wealth Comparison")
    
    # Create grouped bar chart
    fig_comparison = go.Figure()
    
    categories = df_wealth['Wealth_Band'].tolist()
    
    fig_comparison.add_trace(go.Bar(
        name='% of Adults',
        x=categories,
        y=df_wealth['Percentage_of_Adults'],
        marker_color='#4a7db8',
        text=df_wealth['Percentage_of_Adults'].apply(lambda x: f"{x}%"),
        textposition='outside'
    ))
    
    fig_comparison.add_trace(go.Bar(
        name='% of Wealth',
        x=categories,
        y=df_wealth['Percentage_of_Wealth'],
        marker_color='#1f4788',
        text=df_wealth['Percentage_of_Wealth'].apply(lambda x: f"{x}%"),
        textposition='outside'
    ))
    
    fig_comparison.update_layout(
        height=400,
        barmode='group',
        xaxis_title="Wealth Band",
        yaxis_title="Percentage (%)",
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(tickangle=-45)
    )
    
    st.plotly_chart(fig_comparison, use_container_width=True)

st.markdown("---")

# Data Tables Section
st.subheader("📋 Detailed Data Tables")

tab1, tab2, tab3 = st.tabs(["Global Wealth Distribution", "Billionaire Breakdown", "Historical Trends"])

with tab1:
    st.write("**Global Wealth Distribution by Band**")
    display_df = df_wealth[['Wealth_Band', 'Number_of_Adults_Millions', 'Percentage_of_Adults', 
                             'Total_Wealth_Trillions', 'Percentage_of_Wealth']].copy()
    display_df.columns = ['Wealth Band (USD)', 'Adults (Millions)', '% of Adults', 
                          'Total Wealth (Trillions USD)', '% of Wealth']
    display_df = display_df.style.format({
        'Adults (Millions)': '{:.0f}',
        '% of Adults': '{:.1f}%',
        'Total Wealth (Trillions USD)': '${:.2f}T',
        '% of Wealth': '{:.1f}%'
    })
    st.dataframe(display_df, use_container_width=True, hide_index=True)

with tab2:
    st.write("**Billionaire Wealth Distribution**")
    display_billionaires = df_billionaires[['Wealth_Band', 'Number_of_Individuals', 
                                           'Percentage_of_Billionaires', 'Total_Wealth_Trillions',
                                           'Percentage_of_Billionaire_Wealth']].copy()
    display_billionaires.columns = ['Wealth Band', 'Number of Individuals', '% of Billionaires',
                                    'Total Wealth (Trillions USD)', '% of Billionaire Wealth']
    display_billionaires = display_billionaires.style.format({
        'Number of Individuals': '{:.0f}',
        '% of Billionaires': '{:.1f}%',
        'Total Wealth (Trillions USD)': '${:.2f}T',
        '% of Billionaire Wealth': '{:.1f}%'
    })
    st.dataframe(display_billionaires, use_container_width=True, hide_index=True)

with tab3:
    st.write("**Historical Wealth Distribution Trends**")
    display_historical = df_historical.copy()
    display_historical.columns = ['Year', '>$1M (%)', '$100k-$1M (%)', 
                                  '$10k-$100k (%)', '<$10k (%)']
    display_historical = display_historical.style.format({
        '>$1M (%)': '{:.1f}%',
        '$100k-$1M (%)': '{:.1f}%',
        '$10k-$100k (%)': '{:.1f}%',
        '<$10k (%)': '{:.1f}%'
    })
    st.dataframe(display_historical, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p><strong>Global Wealth Distribution Dashboard</strong></p>
        <p>Data Source: Visual Capitalist | Based on Credit Suisse/UBS Global Wealth Reports</p>
        <p style='font-size: 0.9rem;'>Last Updated: 2024</p>
    </div>
""", unsafe_allow_html=True)

