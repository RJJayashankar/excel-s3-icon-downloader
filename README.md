# Excel-s3-icon-downloader (Python)

A Python tool that downloads icon or image files stored in S3 buckets using URLs listed in an Excel spreadsheet, then saves them locally with cleaned filenames.

This utility is designed for bulk asset download workflows where file names and S3 links are already maintained in Excel.

---

# What Does This Tool Do?

This script:

- Reads an Excel file using pandas
- Extracts a name column and a URL column
- Downloads each S3-hosted file
- Cleans filenames for cross-platform compatibility
- Saves files into a local output folder
- Skips empty or invalid links
- Prints progress and error messages

---

# When Should You Use This?

Use this tool when you have:

- Icons or images stored in S3
- A spreadsheet containing file names and URLs
- A need to bulk download assets
- A requirement for clean, consistent filenames

Common use cases include:

- Icon libraries
- Logo collections
- UI asset packs
- ETF or financial product icons
- Brand asset backups

---

# Requirements

Python 3.8+

Install dependencies:

```bash
pip install pandas requests openpyxl
```

---

# Required Excel Columns

Your Excel sheet must include:

- A column containing the file display name
- A column containing the download URL

Example structure:

| Name | URL |
|--------|--------|
| Example Icon | https://s3-bucket/path/icon.png |
| Another Icon | https://s3-bucket/path/icon2.jpg |

Column names can be customized inside the script configuration.

---

# How to Configure the Script

Update the configuration section in the script:

```python
excel_file = "your_excel_file.xlsx"
output_folder = "downloaded_icons"
```

## excel_file
Path to the Excel file containing names and URLs.

## output_folder
Folder where downloaded files will be stored. It will be created automatically if it does not exist.

You can also customize which columns are used:

```python
name_col = "Name"
link_col = "URL"
```

---

# How to Run the Script

Place the Excel file in your working directory and run:

```bash
python your_script.py
```

---

# What Happens During Execution?

The script will:

1. Load the Excel file
2. Print detected column names for verification
3. Loop through each row
4. Read the name and URL
5. Clean the filename
6. Detect the file extension
7. Download the file
8. Save it locally
9. Print status messages

---

# Example Console Output

```
Columns found: ['Name', 'URL']
Total rows found: 120

Done [1]: Example_Icon.png
Done [2]: Another_Icon.jpg
Failed [3]: Sample (HTTP 404)
```

---

# How Filenames Are Cleaned

The script automatically:

- Removes invalid filesystem characters
- Keeps letters and numbers
- Allows spaces, underscores, and dashes
- Converts spaces to underscores
- Preserves detected file extensions

Example:

```
"My Icon (v2)!" → My_Icon_v2.png
```

---

# How File Extensions Are Detected

The extension is extracted from the URL string.

If the extension cannot be reliably determined, the script falls back to a safe default image extension.

---

# How Are Download Errors Handled?

The script safely continues when:

- URL is empty
- Cell value is missing
- Request times out
- Server returns non-200 status
- File download fails

Errors are printed without stopping the full batch run.

---

# Why This Script Is Safe for Bulk Downloads

- Timeout protection on requests
- Row-by-row processing
- Filename sanitization
- Automatic folder creation
- Exception handling per download

---

# Common Problems and Fixes

## Column Not Found Error

Cause:
Excel header names do not match the configured column names.

Fix:
Update the column names in the script configuration to match your spreadsheet exactly.

---

## S3 Returns 403 Forbidden

Cause:
Object is not publicly accessible.

Fix:
Use public URLs or valid signed URLs.

---

## Files Not Downloading

Check:

- URL opens in browser
- Signed URL has not expired
- Network access is allowed

---

# Limitations

- Downloads are sequential
- No automatic retry logic
- Assumes one file per row
- Designed for direct HTTP-accessible S3 objects

---

# Possible Enhancements

- Parallel downloads
- Retry with exponential backoff
- Progress bar
- Duplicate detection
- CSV input support
- Logging to file

---

# Last Updated

2026-02
