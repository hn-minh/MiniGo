# MiniGo v1.0.1

**MiniGo** is a lightweight compiler built with Python that translates MiniGo source code into Java bytecode (Jasmin), executable on the Java Virtual Machine.

## 🧩 Features

- Lexer and parser generation using ANTLR4
- Static semantic checking implemented in Python
- Jasmin bytecode generation
- Compatible with the JVM runtime

## 📦 Process
MiniGo Source (.mng)
│
▼
[Lexer & Parser] ← ANTLR4
│
▼
[Static Checker] ← Python
│
▼
[Code Generator] ← Jasmin (.j)
│
▼
[Java Bytecode] → Executed on JVM

## ⚙️ Requirements

- Python 3.8 or later
- Java Runtime Environment

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/minigo.git
2. **Navigate to the source directory**
   ```bash
   cd /src
3. Create a MiniGo source file
For example: example.mng

4. Run the file
   ```bash
   python run_code.py example.mng

