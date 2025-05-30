HSN Code Validation and Suggestion Agent

--> Overview
This project implements an intelligent agent using the ADK framework to validate and suggest Harmonized System Nomenclature (HSN) codes. The agent uses a master Excel dataset of HSN codes and their descriptions to:

* Validate if a given HSN code is valid and provide hierarchical info.
* Suggest HSN codes based on product/service descriptions.

-->Folder Structure

hsn-agent/
│
├── agents/
│   └── hsn_agent.py            # HSNValidationAgent class implementation
│
├── data/
│   └── HSN_Master_Data.xlsx    # Master dataset of HSN codes (Excel file)
│
├── main.py                    # Main script to run the agent CLI
│
└── README.md                  # This file
---

-->Setup Instructions

1. Clone the repository or download the project files.

2. Install required Python packages:
```bash
pip install pandas openpyxl
```
 `pandas` for Excel data handling
 `openpyxl` as Excel engine for `.xlsx` files

3. Place the `HSN_Master_Data.xlsx` Excel file inside the `data/` folder.

4. Ensure your folder structure matches the above layout.
---
How to Run
Open a terminal or command prompt, navigate to the project folder, and run:

```bash
python main.py
```
You will be presented with a simple menu:
```
Choose an option:
1. Validate an HSN Code
2. Get HSN Code Suggestions by Description
3. Exit
Enter choice (1/2/3):
```

---> Choose **1** to enter an HSN code and validate it.
---> Choose **2** to input a description and get suggested HSN codes.
---> Choose **3** to exit the program.

---
Notes

* The program reads the `HSN_Master_Data.xlsx` file at startup.
* Input HSN codes should be numeric strings matching the dataset’s code format.
* Descriptions are matched approximately to suggest relevant HSN codes.

---

If you face any issues running the program, ensure:

* The Excel file path is correct.
* Required libraries are installed.
* You are using Python 3.x.

---

Feel free to extend or modify the agent logic as per your requirements.

---

If you want, I can also help you draft a sample `main.py` or `hsn_agent.py` file structure!
