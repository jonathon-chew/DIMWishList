# DIM Wish List Cleaner

This Python script automates the process of downloading, filtering, and saving a Destiny Item Manager (DIM)

## 📜 Overview

The script performs the following steps:

Downloads the latest voltron.txt wish list file from GitHub.

Saves a copy of the unmodified wish list for archival or debugging purposes.

Filters out any wish list items that contain the username "pandapaxxy" anywhere in the text or comments.

Writes the cleaned wish list to a new file (wish_list.txt) formatted properly for DIM to use.

## 🧰 Requirements

Python 3.10+

The following Python packages:

requests

Install dependencies with:

```bash
pip install requests
```

## ⚙️ Usage

Clone or download this repository (or just the script).

Run the script from the terminal:
```bash
python script.py
```
After running, you’ll find:

voltron.txt → The original, unmodified wish list file.

wish_list.txt → The cleaned version (with "pandapaxxy" entries removed).

## 🧩 Customization

To remove a different creator’s items, simply update the username in the filter section of the script:

```python
if "pandapaxxy" not in eachWishListItem:
    final_file.append(eachWishListItem)
```
Replace "pandapaxxy" with another username as needed.

## 🛠️ Notes

The script expects the wish list to be formatted with two consecutive newline characters (\n\n) separating entries.

Any entry containing the target username anywhere in its text or comments will be removed.

Make sure you have a stable internet connection when fetching the wish list from GitHub.
