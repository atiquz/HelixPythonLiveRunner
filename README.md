# HelixPythonLiveRunner
A simple batch script that lets you **run Python code live inside Helix on Windows**.  
Edit your file in Helix (left pane) and instantly see your output update (right pane) perfect for Python learners!

---

## 🚀 Features
- Auto-runs Python script on every save  
- Split view: code (left) + output (right)  
- Works directly with **Helix editor**  
- No external tools needed  
- Easy one-click setup  

---

## ⚙️ Setup Guide

Follow these simple steps to get started with **HelixPythonLiveRunner** 👇  

1. **Create your workspace:**
   - Make a folder named `Python Learning` in this location:  
     ```
     C:\Users\YOURUSERNAME\Desktop\Python Learning
     ```
   - Inside it, create a file named `main.py`.  
     Example content:
     ```python
     print("Hello, Helix!")
     ```

2. **Create the batch file:**
   - In this location, create a new file named:
     ```
     C:\Users\YOURUSERNAME\Desktop\pythonLearning.bat
     ```
   - Copy the batch script from this repository into that file.

3. **Verify paths in the script:**
   - Make sure the two paths match your setup:
     ```
     C:\Users\YOURUSERNAME\Desktop\Python Learning
     C:\Users\YOURUSERNAME\Desktop\pythonLearning.bat
     ```

4. **Run the script:**
   - Double-click `pythonLearning.bat`.  
   - It will automatically:
     - Open **Helix** in the left pane with `main.py`.
     - Run **Python output** live in the right pane — auto-refreshes whenever you save the file.

---

## 🧩 Requirements

Before running, make sure you have the following installed:

| Tool | Description | Download |
|------|--------------|-----------|
| 🖋️ [Helix Editor](https://helix-editor.com/) | For writing and editing Python code. | Official site |
| 🐍 [Python 3.x](https://www.python.org/downloads/) | For running your Python scripts. | python.org |
| 🪟 [Windows Terminal](https://aka.ms/terminal) | For split-pane live output. | Microsoft Store |

> ⚠️ Make sure all of the above tools are **added to your system PATH**.

---

✅ Once setup is complete — just code, save, and see instant results side by side!

---
![HelixPythonLiveRunner Screenshot](HelixPythonLiveRunnerScreenshot.png)
