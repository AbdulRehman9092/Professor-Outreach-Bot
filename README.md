# Professor Outreach Bot

This repository contains a set of scripts designed to automate the process of finding and contacting university professors for research opportunities. The solution uses a Python script with Selenium and Perplexity AI to scrape professor information and generate personalized email drafts, and a PowerShell script to send these emails in bulk.

## Features

-   **Automated Professor Discovery**: Scrapes Perplexity AI to find professors in specific fields of study (e.g., Environmental or Civil Engineering) at a list of target universities.
-   **Intelligent Filtering**: Filters results to identify professors with current projects, active labs, or those who are likely accepting new students.
-   **Email Generation**: Automatically drafts personalized outreach emails based on the professor's profile and a customizable template.
-   **Bulk Email Sending**: Includes a PowerShell script to send the generated emails via Gmail's SMTP server, complete with attachments.
-   **Concurrent Processing**: Utilizes multi-threading to scrape multiple universities simultaneously, speeding up the data collection process.

## How It Works

The process is divided into two main parts: data scraping/email generation and bulk sending.

### 1. Generating Emails (`Professor.py`)

The Python script `Professor.py` orchestrates the web scraping process.

1.  It reads a list of university names from `a.txt`.
2.  Using `seleniumbase`, it launches multiple browser instances to process universities concurrently.
3.  For each university, it performs a series of queries on Perplexity AI to:
    -   List all professors in a specified academic field.
    -   Filter the list to find professors with ongoing projects or who are accepting students.
    -   Conduct deep searches to find the email addresses of the most promising candidates.
    -   Randomly select one suitable professor.
    -   Generate a complete, personalized email draft using a detailed prompt that fills in the professor's name and research interests.
4.  The final, formatted email drafts are appended to a file named `adan.txt`.

### 2. Sending Emails (`Bulk Sending.ps1`)

The PowerShell script `Bulk Sending.ps1` handles the email distribution.

1.  It reads the formatted email drafts from a specified data file (e.g., `data.txt`).
2.  It securely prompts the user for a Gmail App Password to authenticate with Google's SMTP server.
3.  It iterates through each entry, sending a personalized email with a specified attachment (e.g., `CV.pdf`).
4.  Progress and status (success or failure) for each email are printed to the console.

## Prerequisites

-   Python 3.x
-   PowerShell (available by default on Windows)
-   A Gmail account with an **App Password**. [Learn how to create one here](https://support.google.com/accounts/answer/185833).
-   Your résumé/CV saved as a PDF file.

## Setup and Usage

### Step 1: Clone the Repository

```bash
git clone https://github.com/AbdulRehman9092/Professor-Outreach-Bot.git
cd Professor-Outreach-Bot
```

### Step 2: Install Python Dependencies

The script relies on the `seleniumbase` library.

```bash
pip install seleniumbase
# Install the necessary webdriver
seleniumbase install chromedriver
```

### Step 3: Configure and Run the Python Scraper (`Professor.py`)

1.  **Edit `a.txt`**: Populate this file with the names of the universities you want to target, with each university on a new line.

2.  **Customize `Professor.py`**:
    -   In `query1`, change `"environmental or Civil Engineering"` to your desired field of study.
    -   In `query8`, carefully edit the email template with your personal information: `YourName`, `Your uni`, graduation date, project details, and internship experiences.
    -   Adjust the paths for the user data directories (`user_data_dirs`) if necessary. The default paths are `C:\\1`, `C:\\2`, etc. Ensure these directories exist.

3.  **Run the script**:
    ```bash
    python Professor.py
    ```
    The script will begin scraping and will create a file named `adan.txt` containing the generated email drafts.

### Step 4: Configure and Run the PowerShell Sender (`Bulk Sending.ps1`)

1.  **Prepare the Data File**:
    -   Review the generated `adan.txt` file for accuracy and make any manual corrections.
    -   Rename `adan.txt` to `data.txt` and move it to your Desktop, or update the `$dataFile` path in the script.

2.  **Prepare Your CV**:
    -   Rename your résumé/CV file to `CV.pdf` and place it on your Desktop, or update the `$attachmentPath` in the script.

3.  **Customize `Bulk Sending.ps1`**:
    -   Open the script and set the `$displayName` to your full name.
    -   Set `$emailFrom` to your Gmail address.

4.  **Run the script**:
    -   Open a PowerShell terminal.
    -   Navigate to the repository directory.
    -   Execute the script:
        ```powershell
        .\'Bulk Sending.ps1'
        ```
    -   When prompted, enter the **16-digit Gmail App Password** you generated (not your regular account password).

The script will begin sending the emails and report its progress.

## File Descriptions

-   **`Professor.py`**: The main Python script for scraping professor data and generating email drafts.
-   **`Bulk Sending.ps1`**: The PowerShell script for sending the generated emails via Gmail SMTP.
-   **`a.txt`**: The input file for `Professor.py` containing a list of target university names.
-   **`data format.txt`**: A sample file demonstrating the required format for the email data used by the sending script.

## Important Notes

-   **Web Scraping Fragility**: This tool depends on the structure of the Perplexity AI website. If the site's HTML changes, the scraper may fail.
-   **Use Responsibly**: Sending a large number of emails in a short time can cause your emails to be marked as spam. Always review generated content and send emails at a reasonable pace.
-   **AI Accuracy**: The AI-generated content may not always be perfect. **Always proofread every email** before sending it to ensure accuracy and professionalism.
