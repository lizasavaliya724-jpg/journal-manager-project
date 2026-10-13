# 📓 Personal Journal Manager

## 1. Introduction
Personal Journal Manager is a Python-based project used to manage personal journal entries.  
Users can add, view, search, and delete journal entries. The program also saves the date and time of each entry.

---

## 2. Project Objectives
- Store personal journal entries in a text file.  
- View previously saved entries.  
- Search entries using a keyword or date.  
- Delete all journal entries when required.  
- Understand Python file handling and OOP concepts.  

---

## 3. Features
1. Add a New Entry  
2. View All Entries  
3. Search for an Entry  
4. Delete All Entries  
5. Exit the Program  

---

## 4. Technologies Used
- Python 3.x  
- Object-Oriented Programming (OOP)  
- File Handling  
- Exception Handling  
- Datetime Module  

---

## 5. Code Explanation

### 🔹 Class: `JournalManager`
This class manages all journal operations. It stores the journal filename and contains methods to add, view, search, and delete entries.

### 🔹 Constructor: `__init__()`
The constructor initializes the filename as `journal.txt`.

### 🔹 Add Entry
The `add_entry()` method accepts a journal entry from the user and saves it with the current date and time.  
Append mode (`a`) preserves existing entries.

### 🔹 View Entries
The `view_entries()` method reads and displays all saved journal entries.  
It also handles cases where the file does not exist.

### 🔹 Search Entry
The `search_entry()` method searches the journal file for a keyword or date and displays matching entries.

### 🔹 Delete Entries
The `delete_entries()` method asks for confirmation before deleting all saved entries.  
Write mode (`w`) clears the file content.

### 🔹 Main Function
The `main()` function displays the menu and executes the selected operation.  
A `while` loop keeps the menu running until the user chooses Exit.

### 🔹 Exception Handling
The program uses exception handling to manage errors such as:
- `FileNotFoundError`  
- `PermissionError`  
- `ValueError`  
- `OSError`  

---

## 6. File Structure
```text
Personal-Journal-Manager/
---project6.py
--- journal.txt
--- README.md
