# My Password Generator v1.0

A simple desktop password generator built with **Python** and **Flet**.

## Features

- Generate random passwords using Python's `secrets` module
- Choose which character groups to include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Punctuation
- Adjust password length from 4 to 30 characters
- Dark interface with a custom color palette

## Preview

![My Password Generator](assets/password-generator.png)

## Requirements

- Python 3
- **Flet 0.28.0**

> **Important:** This project is configured for **Flet 0.28.0**. Install this exact version rather than the latest release. Newer Flet versions may contain API changes that are incompatible with this project's code.

## Download for Windows

A standalone Windows executable is built automatically by GitHub Actions. When a versioned tag (for example, `v1.0.0`) is pushed, the workflow builds the app and attaches `MyPasswordGenerator-Windows.zip` to the GitHub Release.

1. Open the repository's **Releases** page.
2. Download `MyPasswordGenerator-Windows.zip`.
3. Extract the ZIP file.
4. Double-click `MyPasswordGenerator.exe`.

**Python and Flet do not need to be installed on the target PC.** The executable bundles the Python app and its required dependencies. The first launch may take a little longer while the bundled app starts.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/CodeWithAMZ/PasswordManager.git
   cd PasswordManager
   ```

2. (Recommended) Create and activate a virtual environment.

3. Install the required Flet version:

   ```bash
   python -m pip install flet==0.28.0
   ```

## Run

   ```bash
   python PassGenUI.py
   ```

## Project Details

| Item | Details |
|---|---|
| Application | My Password Generator |
| Version | 1.0 |
| Language | Python |
| UI Framework | Flet 0.28.0 |
| Password generation | Python `secrets` module |

---

Created by **Amir Mahdi Zamani** — [CodeWithAMZ](https://github.com/CodeWithAMZ).
