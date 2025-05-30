from base_agent import Agent
import pandas as pd
from fuzzywuzzy import process

class HSNValidationAgent(Agent):
    def __init__(self):
        super().__init__()
        #self.hsn_data = pd.read_excel("data/HSN_Master_Data.xlsx", header=2)
        self.hsn_data = pd.read_excel("data/HSN_Master_Data.xlsx")
        self.hsn_data.columns = self.hsn_data.columns.str.strip()

        print("Actual column names in Excel file:", self.hsn_data.columns.tolist())

        self.hsn_data["HSNCode"] = self.hsn_data["HSNCode"].astype(str)

    def validate_hsn_code(self, code):
        code = str(code)
        if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
            return {"valid": False, "reason": "Invalid format"}
        if code in self.hsn_data["HSNCode"].values:
            description = self.hsn_data.loc[self.hsn_data["HSNCode"] == code, "Description"].values[0]
            return {"valid": True, "description": description}
        else:
            return {"valid": False, "reason": "HSN code not found"}

    def hierarchical_validation(self, code):
        code = str(code)
        hierarchy = [code[:i] for i in range(2, len(code)+1, 2)]
        results = {}
        for h in hierarchy:
            found = h in self.hsn_data["HSNCode"].values
            desc = self.hsn_data.loc[self.hsn_data["HSNCode"] == h, "Description"].values[0] if found else "Not Found"
            results[h] = {"exists": found, "description": desc}
        return results

    def suggest_hsn(self, description):
        matches = process.extract(description, self.hsn_data["Description"], limit=5)
        suggestions = []
        for match in matches:
            desc = match[0]
            score = match[1]
            code_row = self.hsn_data[self.hsn_data["Description"] == desc]
            if not code_row.empty:
                code = code_row["HSNCode"].values[0]
                suggestions.append({"HSNCode": code, "Description": desc, "Score": score})
        return suggestions



    def run(self, inputs):
        if "hsn_code" in inputs:
            code = inputs["hsn_code"]
            result = self.validate_hsn_code(code)
            if result["valid"]:
                hierarchy = self.hierarchical_validation(code)
                result["hierarchy"] = hierarchy
            return result
        elif "description" in inputs:
            return self.suggest_hsn(inputs["description"])
        else:
            return {"error": "No valid input provided. Expecting 'hsn_code' or 'description'."}
