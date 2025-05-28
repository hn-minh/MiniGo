# MiniGo v1.0.2

**MiniGo** is a lightweight compiler built with Python that translates MiniGo source code into Java bytecode (Jasmin), executable on the Java Virtual Machine.

## 🧩 Features

- Lexer and parser generation using ANTLR4
- Static semantic checking implemented in Python
- Jasmin bytecode generation
- Compatible with the JVM runtime

## ⚙️ Requirements

- Python 3.8 or later
- Java Runtime Environment
- To better understand the functionality of MiniGo, please read the attached specification. The repository includes a few sample programs for testing.

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/hn-minh/MiniGo
2. **Navigate to the source directory**
   ```bash
   cd src
3. Create a MiniGo source file

   For example: example.mng

5. Run the file
   ```bash
   python code_run.py example.mng

