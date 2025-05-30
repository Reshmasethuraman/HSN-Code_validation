from agents.hsn_agent import HSNValidationAgent
agent = HSNValidationAgent()

def validate_hsn():
    input_code = input("Enter HSN code to validate: ").strip()
    result = agent.run({"hsn_code": input_code})
    print("\nValidation Result:\n", result)

def suggest_hsn():
    input_desc = input("Enter description for HSN suggestions: ").strip()
    suggestions = agent.run({"description": input_desc})
    print("\nHSN Code Suggestions:\n", suggestions)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Validate an HSN Code")
        print("2. Get HSN Code Suggestions by Description")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()
        if choice == '1':
            validate_hsn()
        elif choice == '2':
            suggest_hsn()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

