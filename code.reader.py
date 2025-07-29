# import os
# from dotenv import load_dotenv
# import google.generativeai as genai


# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# model = genai.GenerativeModel('gemini-2.5-flash')


# def readcode(filepath):
#     """Read code from a file."""
#     try:
#         with open(filepath, "r") as f:
#             return f.read()
#     except FileNotFoundError:
#         print("❌ Error: code file not found.")
#         exit(1)


# def coder(code):
#     """Explain code, inputs, variables, expected output, and errors."""
#     prompt = f"""
# You are a professional programming assistant.

# Given the following code, do the following:
# 1. List the  language used
# 2. List the **Inputs** (if any).
# 3. List all **Variables** used and their purposes.
# 4. Give the **Expected Output** of the code.
# 5. If the code contains an **error**, specify the error and mention the line or part where it occurs.

# Code:
# {code}

# Your explanation should be structured as:
# - Which  language
# - Input:
# - Variables:
# - Expected Output:
# - Errors (if any):
# """

#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         print(f" An error occurred: {e}")
#         exit(1)


# if __name__ == "__main__":
#     code_content = readcode("code.py")
#     result = coder(code_content)

#     print("\n🔍 Code Analysis 🔍\n")
#     print("-" * 50)
#     print(result)

