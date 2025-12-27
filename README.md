# 🌍 Global Wealth Distribution Dashboard

A professional, interactive HTML dashboard visualizing global wealth distribution patterns, inequality trends, and economic disparities worldwide.

## 📊 Features

- **Wealth Distribution Pyramid Infographic**: Integrated infographic from Visual Capitalist
- **Wealth Distribution Pyramid**: Interactive visual representation of how global wealth is distributed across different wealth bands
- **Billionaire Analysis**: Detailed breakdown of billionaire wealth distribution
- **Historical Trends**: Time-series analysis showing wealth distribution changes from 2000 to 2027 (projected)
- **Population vs Wealth Comparison**: Comparative analysis showing the disconnect between population percentage and wealth ownership
- **Comprehensive Data Tables**: Detailed tables with all data from Visual Capitalist including regional distribution
- **Interactive Charts**: Fully interactive visualizations powered by Plotly.js
- **Professional Design**: Clean, modern UI with responsive layout
- **No Server Required**: Standalone HTML file - just open in any browser!

## 🚀 Quick Start

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Internet connection (for loading Plotly.js library and infographic)

### Installation & Usage

1. **Download the dashboard:**
   - Simply download the `dashboard.html` file

2. **Open the dashboard:**
   - Double-click `dashboard.html` to open it in your default browser
   - Or right-click and select "Open with" to choose a specific browser
   - No installation, no dependencies, no setup required!

3. **Alternative: Run a local server (optional):**
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Then open: http://localhost:8000/dashboard.html
   ```

## 📈 Data Sources

The dashboard is based on data from:
- Visual Capitalist's Global Wealth Distribution reports
- Credit Suisse/UBS Global Wealth Reports
- Updated with latest available statistics (2024)

## 📋 Key Metrics Displayed

- **Total Global Wealth**: $471 Trillion
- **Global Adult Population**: 3.81 Billion
- **Wealth Concentration**: Top 1.6% hold 48.1% of global wealth
- **Billionaire Count**: 2,891 individuals

## 🎨 Visualizations Included

1. **Wealth Distribution Pyramid** - Horizontal bar chart showing wealth distribution by bands
2. **Billionaire Wealth Pie Chart** - Breakdown of billionaire wealth by tier
3. **Historical Trends Line Chart** - Evolution of wealth distribution over time
4. **Population vs Wealth Comparison** - Grouped bar chart highlighting inequality

## 🛠️ Technologies Used

- **HTML5**: Modern web standard
- **CSS3**: Professional styling with responsive design
- **JavaScript**: Interactive functionality
- **Plotly.js**: Interactive data visualizations (loaded via CDN)
- **No Backend Required**: Fully client-side application

## 📝 Project Structure

```
.
├── dashboard.html      # Main HTML dashboard (standalone file)
├── app.py              # Original Streamlit version (optional)
├── requirements.txt    # Python dependencies (for Streamlit version)
└── README.md          # Project documentation
```

## 🔧 Customization

You can easily customize the dashboard by:

- Editing `dashboard.html` directly with any text editor
- Modifying data in the JavaScript sections
- Adjusting color schemes in the CSS `<style>` section
- Adding new charts or metrics
- Integrating with live data sources via API

## 🖼️ About the Infographic

The dashboard includes an embedded infographic from Visual Capitalist. If the image doesn't load:

1. The page includes a fallback placeholder
2. You can download the infographic directly from the [Visual Capitalist website](https://www.visualcapitalist.com/the-global-distribution-of-wealth-shown-in-one-pyramid/)
3. Save it locally and update the image `src` attribute in the HTML file

## 📊 Data Categories

The dashboard displays wealth distribution across four main bands:

- **>$1 million**: Ultra-high net worth individuals
- **$100k – $1 million**: High net worth individuals
- **$10k – $100k**: Middle-class segment
- **<$10k**: Lower wealth segment

## 🌐 Browser Compatibility

The dashboard works best on:
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## 📄 License

This project is open source and available for educational and research purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

---

**Note**: This dashboard is for informational and educational purposes. Data should be verified with original sources for official use.

