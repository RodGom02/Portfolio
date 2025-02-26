import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example financial data (Income Statement and Balance Sheet)
data = {
    'Revenue': [500000],            # Total revenue for the period
    'COGS': [200000],               # Cost of Goods Sold
    'Operating_Expenses': [100000], # Operating Expenses
    'Net_Income': [80000],          # Net Income (after taxes)
    'Equity': [400000],             # Shareholder Equity
    'Total_Assets': [1000000],      # Total Assets
    'Total_Liabilities': [600000],  # Total Liabilities
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate Gross Profit
df['Gross_Profit'] = df['Revenue'] - df['COGS']

# Calculate Gross Profit Margin (Gross Profit / Revenue)
df['Gross_Profit_Margin'] = df['Gross_Profit'] / df['Revenue'] * 100

# Calculate Operating Profit (Operating Income)
df['Operating_Profit'] = df['Gross_Profit'] - df['Operating_Expenses']

# Calculate Operating Profit Margin (Operating Profit / Revenue)
df['Operating_Profit_Margin'] = df['Operating_Profit'] / df['Revenue'] * 100

# Calculate Net Profit Margin (Net Income / Revenue)
df['Net_Profit_Margin'] = df['Net_Income'] / df['Revenue'] * 100

# Calculate Return on Equity (Net Income / Equity)
df['ROE'] = df['Net_Income'] / df['Equity'] * 100

# Calculate the Debt-to-Equity Ratio (Total Liabilities / Equity)
df['Debt_to_Equity'] = df['Total_Liabilities'] / df['Equity']

# Print the financial metrics
print("Financial Ratios and Metrics:")
print(df[['Gross_Profit_Margin', 'Operating_Profit_Margin', 'Net_Profit_Margin', 'ROE', 'Debt_to_Equity']])

# Visualization: Create a bar chart for the financial ratios
# Prepare the data for plotting
metrics = ['Gross_Profit_Margin', 'Operating_Profit_Margin', 'Net_Profit_Margin', 'ROE', 'Debt_to_Equity']
values = df[metrics].values.flatten()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=metrics, y=values, palette='viridis')

# Add titles and labels
plt.title("Key Financial Ratios", fontsize=16)
plt.ylabel("Percentage or Ratio Value", fontsize=12)
plt.xlabel("Financial Metrics", fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
