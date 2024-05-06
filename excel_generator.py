import pandas as pd

# Define the start and end date with hourly frequency
start_datetime = '2024-03-04'
end_datetime = '2024-05-06 00:00'
datetimes = pd.date_range(start=start_datetime, end=end_datetime, freq='H')

# Create a DataFrame with the required columns
df = pd.DataFrame({
    'Time': datetimes,
    'Price': [None] * len(datetimes),  # Placeholder values
    'Turnover': [None] * len(datetimes)  # Placeholder values
})

# Write the DataFrame to an Excel file
file_path = 'market_data.xlsx'
df.to_excel(file_path, index=False, engine='openpyxl')

print(f"Data has been successfully written to {file_path}")
