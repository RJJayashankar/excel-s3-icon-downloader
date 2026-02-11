import pandas as pd
import requests
import os

# --- Configuration ---
excel_file = 'Book1.xlsx'  # <--- MAKE SURE THIS FILENAME IS CORRECT
output_folder = 'ETF_Reps_NAME_Downloaded_S3_Icons'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

try:
    # 1. Load the Excel file
    df = pd.read_excel(excel_file)
    
    # DEBUG: This helps us see what Python is actually reading
    print("--- Debug Info ---")
    print(f"Columns found: {df.columns.tolist()}")
    print(f"Total rows found: {len(df)}")
    print("------------------\n")

    # 2. Match your specific column names
    # Using 'Stock Reps_nameLink' for the filename and 'namelink' for the URL
    name_col = 'ETF Reps name'
    link_col = 'Link'

    for index, row in df.iterrows():
        # Get data from the row
        raw_name = str(row[name_col]).strip()
        url = str(row[link_col]).strip()
        
        # Skip if the URL is empty or nan
        if url.lower() == 'nan' or not url:
            continue

        # Clean the name for Windows/Mac/Linux compatibility
        clean_name = "".join([c for c in raw_name if c.isalnum() or c in (' ', '_', '-')]).rstrip()
        clean_name = clean_name.replace(" ", "_")
        
        # Get extension
        extension = url.split('.')[-1].split('?')[0]
        if len(extension) > 4: extension = "png" # fallback
        
        filename = f"{clean_name}.{extension}"
        save_path = os.path.join(output_folder, filename)

        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print(f"Done [{index + 1}]: {filename}")
            else:
                print(f"Failed [{index + 1}]: {clean_name} (HTTP {response.status_code})")
        except Exception as e:
            print(f"Error downloading {clean_name}: {e}")

except KeyError as e:
    print(f"COLUMN NAME ERROR: Could not find column {e}.")
    print("Please check if your Excel headers match 'Stock Reps_nameLink' and 'namelink' exactly.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")