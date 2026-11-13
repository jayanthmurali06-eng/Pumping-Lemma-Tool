# Pumping Lemma Demonstration Tool

An interactive Python-based application that demonstrates the **Pumping Lemma for Regular Languages** using string generation, decomposition, pumping operations, and graphical visualizations.

## Project Overview

The Pumping Lemma is an important concept in Formal Automata and Formal Languages (FAFL). It is used to understand properties of regular languages and to demonstrate why certain languages are not regular.

This project provides an interactive tool where users can select a language, specify a pumping length, generate candidate strings, divide strings into `x`, `y`, and `z`, and observe how the strings change for different pumping values.

## Features

- **Language Selection:** Choose between two predefined languages:
  - `a*b*` – A regular language.
  - `a^n b^n` – A non-regular language.
- **Pumping Length:** Set the pumping length `p`.
- **Candidate String Generation:** Automatically generate suitable strings.
- **String Decomposition:** Divide a selected string into `x`, `y`, and `z`.
- **Pumping Operation:** Generate pumped strings using `xy^iz` for different values of `i`.
- **Condition Verification:** Check the basic decomposition conditions.
- **Graphical Visualization:**
  - X-Y-Z string decomposition diagram.
  - Pumping graph showing string length against pumping value.
  - Membership graph showing accepted and rejected strings.
- **Results Table:** Display all pumped strings and their membership status.

## Technologies Used

- Python
- Streamlit
- Pandas
- HTML and CSS

## Pumping Lemma

For a regular language `L`, there exists a pumping length `p` such that every string `w` in `L`, with length at least `p`, can be divided into three parts:

`w = xyz`

The following conditions must hold:

1. `|xy| <= p`
2. `|y| > 0`
3. `xy^i z` belongs to `L` for every integer `i >= 0`.

Here:
- `x` – First part of the string.
- `y` – Part that is repeated or removed.
- `z` – Remaining part of the string.
- `i` – Pumping value.

## Supported Languages

### 1. Regular Language: a*b*

`L = { a^m b^n | m,n >= 0 }`

This language contains zero or more `a` characters followed by zero or more `b` characters.

Examples:
- `ab`
- `aab`
- `abb`
- `aaabbb`
- `ε`

### 2. Non-Regular Language: a^n b^n

`L = { a^n b^n | n >= 0 }`

This language contains an equal number of `a` and `b` characters, with all `a` characters appearing before the `b` characters.

Examples:
- `ab`
- `aabb`
- `aaabbb`

Strings such as `abb` and `aaabb` are not members of this language.

## Installation and Execution

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/jayanthmurali06-eng/Pumping-Lemma-Tool.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Pumping-Lemma-Tool
```

### Step 3: Create a Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements file yet, install the packages directly:

```bash
pip install streamlit pandas
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## How to Use the Application

1. Select a language from the dropdown.
2. Enter the pumping length.
3. Click **Generate Strings**.
4. Select a candidate string.
5. Choose a valid decomposition into `x`, `y`, and `z`.
6. View the X-Y-Z decomposition visualization.
7. Check the pumping conditions.
8. Enter pumping values such as `0,1,2,3,4`.
9. Click **Pump and Generate Graphs**.
10. Observe the pumped strings, graphs, and results table.

## Sample Demonstration

Consider the non-regular language:

`L = { a^n b^n | n >= 0 }`

Select:

- Pumping length: `p = 2`
- Candidate string: `aabb`
- Decomposition: `x = ε`, `y = a`, `z = abb`
- Pumping values: `0,1,2`

Expected results:

| Pumping value (i) | Pumped string | Membership |
|---|---|---|
| 0 | abb | Rejected |
| 1 | aabb | Accepted |
| 2 | aaabb | Rejected |

The graphs demonstrate the change in string length and the membership results for the selected decomposition.

## Project Structure

```text
Pumping-Lemma-Tool/
│
├── app.py
├── pumping_lemma.py
├── requirements.txt
├── README.md
└── venv/
```

**File descriptions:**

- `app.py` – Streamlit user interface and graphical visualizations.
- `pumping_lemma.py` – Core logic for language checking, candidate generation, string decomposition, and pumping operations.
- `requirements.txt` – Required Python packages.
- `README.md` – Project documentation.

The virtual environment folder is local to the developer's machine and should not be committed to GitHub.

## Learning Outcomes

- Understand the Pumping Lemma for regular languages.
- Learn string decomposition using `w = xyz`.
- Understand the effect of pumping values on strings.
- Differentiate between regular and non-regular language examples.
- Visualize string length changes and language membership.
- Apply Python programming to concepts in Formal Automata and Formal Languages.

## Limitations

This application is an educational demonstration tool supporting two predefined languages. Testing a selected decomposition for several pumping values does not independently prove that a language is regular or non-regular. A formal non-regularity proof must establish that every valid decomposition fails for at least one pumping value.

## Author

**Jayanth Murali**

GitHub: https://github.com/jayanthmurali06-eng

## Repository

https://github.com/jayanthmurali06-eng/Pumping-Lemma-Tool

---

Developed as part of the **Formal Automata and Formal Languages (FAFL) Activity**.