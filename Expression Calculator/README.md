# 🧮 Expression Calculator (Python)

A Python-based **Expression Calculator** that evaluates arithmetic expressions using **stacks**.  
This project demonstrates how to convert **infix expressions** (human-readable) into **postfix expressions** (machine-friendly) and then evaluate them.  

---

## 📌 Overview
The Expression Calculator:
- Accepts **infix expressions** (e.g., `3 + 4 * 2`).
- Converts them into **postfix notation** using the **Shunting Yard Algorithm**.
- Evaluates the postfix expression using a **stack-based evaluation method**.
- Supports operators: `+`, `-`, `*`, `/`, `^`, and parentheses `()`.  

---

## ✨ Features
- 🔄 **Infix to Postfix Conversion** – Ensures correct operator precedence and associativity.  
- 🧾 **Expression Evaluation** – Computes the result from postfix expressions.  
- ⚡ **Supports Multiple Operators** – Addition, subtraction, multiplication, division, exponentiation.  
- 🧩 **Parentheses Handling** – Correctly handles nested expressions.  
- 📋 **Stack-based implementation** – Demonstrates core **data structures**.  

---

## 🛠 Data Structures Used
- **Stack (using Python `list`)**  
  - Used in **infix → postfix conversion** to manage operators.  
  - Used in **postfix evaluation** to compute results.  

- **String Processing**  
  - Tokenizes the input expression into numbers, operators, and parentheses.  

---

## ▶️ How It Runs
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/expression-calculator.git
   cd expression-calculator
