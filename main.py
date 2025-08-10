# .\venv\Scripts\Activate
#uvicorn main:app --reload

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/run")
def run_code(code: dict):
    return {"result": "Code executed"}

@app.post("/api/tc")
def time_complexity(code: dict):
    return {"result": "Time complexity"}

@app.post("/api/sc")
def space_complexity(code: dict):
    return {"result": "Space complexity"}

@app.post("/api/optimal")
def optimal_code(code: dict):
    return {"result": "Optimized code"}



load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeInput(BaseModel):
    code: str


@app.post("/api/run")
def run_code(data: CodeInput):
    prompt = f"""
You are a professional programming assistant.
1. Find the output of the given code.
2. If the code contains any **errors**, identify them along with the **line number**.
3. Dont provide any explanation, just the output.
4. If there is an error please provide a 2 line explaination of that error along with solution **Error solving**  
5. If input is given (input is given in form of comments in last line after the code) take that input and genarate corresponding output.
6. If input is not provided genarate concurrent input and provide corresponding output.

Code:
{data.code}
"""
    response = model.generate_content(prompt)
    return {"result": response.text}

@app.post("/api/tc")
def time_complexity(data: CodeInput):
    prompt = f"""You are a professional programming assistant.
1. Determine the **time complexity** of the given code.
2. Also give **optimal time complexity**, no explanation.

Code:
{data.code}
"""
    response = model.generate_content(prompt)
    return {"result": response.text}

@app.post("/api/sc")
def space_complexity(data: CodeInput):
    prompt = f"""You are a professional programming assistant.
1. Determine the **space complexity** of the given code.
2. Give only the complexity, no explanation.

Code:
{data.code}
"""
    response = model.generate_content(prompt)
    return {"result": response.text}

@app.post("/api/optimal")
def optimal_code(data: CodeInput):
    prompt = f"""You are a professional programming assistant.
1. Provide an **optimal version** of the given code.
2. Also include the time complexity.
3. No explanation, just optimal code.
4. Note: please remove comments while you are genrating an optimal solution. 

Code:
{data.code}
"""
    response = model.generate_content(prompt)
    return {"result": response.text}


