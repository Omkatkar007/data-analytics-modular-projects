# Gurgaon Real Estate Market Analysis 🏙️📊

## 🎯 Overview
This project is an end-to-end data analytics pipeline designed to extract actionable business insights from the Gurgaon real estate market. By leveraging Python, the project transforms raw, messy property data into clean metrics, answering key questions about pricing, locality premiums, and property types.

## 🛠️ Technology Stack
- **Language:** Python 3.x
- **Data Manipulation:** Pandas
- **Data Visualization:** Matplotlib, Seaborn

## 🧹 The ETL & Data Cleaning Process
Real-world data is rarely ready for analysis. This project includes a robust cleaning phase:
- **String Vectorization:** Standardized column names and stripped hidden whitespace.
- **Type Conversion:** Removed formatting commas from prices and areas, converting them from `string` objects to calculable `integers`.
- **Categorical Cleaning:** Normalized text casing for property status, RERA approvals, and flat types to prevent duplicate categories.
- **Data Integrity:** Dropped duplicate records to prevent skewed averages and inaccurate aggregations.

## 📈 Key Business Questions Answered
The analysis script groups, aggregates, and filters the data to answer 10 critical market questions:
1. Which is the absolute costliest flat on the market?
2. Which locality commands the highest average price?
3. Which locality has the highest premium (Rate per SqFt)?
4. How does "Ready-to-Move" pricing compare to "Under-Construction" (using median to mitigate outliers)?
5. Is there a measurable trust premium for RERA-approved properties?
6. How exactly does property area correlate with final price?
7. Which BHK configuration is in highest demand/most expensive?
8. Are standalone plots, floors, or apartments the costliest?
9. Which builders command the highest market prices?
10. Do economies of scale exist? (Does buying a larger home mean a cheaper rate per square foot?)

## 📊 Visualizations
The script automatically generates Seaborn scatter plots to visually represent:
- **Price vs. Area Correlation:** Mapping how property size scales with total cost.
- **Economies of Scale:** Analyzing the relationship between total area and the rate per square foot.

## 🚀 How to Run Locally

1. Clone this repository.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Place your raw dataset (`data.csv`) in the same directory as the script.
4. Run the analysis script:
   ```bash
   python gurgaon_analysis.py
   ```
