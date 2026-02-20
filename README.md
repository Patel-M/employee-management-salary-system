# 💼 Employee Management and Salary Processing System

![Thumbnail](assets/thumbnail.png)

> **A Python–MySQL based system designed to manage employee records and automate salary calculation and reporting through a structured database-driven interface.**

---

## 📌 Overview

The **Employee Management and Salary Processing System** is a database-driven backend application built using **Python and MySQL**. It streamlines employee record management and automates salary computation using structured relational database design.

The system enables storage, retrieval, modification, and reporting of employee and salary data through a menu-driven console interface. This project demonstrates practical implementation of database connectivity, CRUD operations, and backend business logic aligned with real-world HR management workflows.

---

## 🎯 Problem Statement

Manual handling of employee records and salary calculations is time-consuming and prone to errors.  

This project provides a **centralized, reliable, and automated system** to:

- Maintain structured employee records  
- Process salary components programmatically  
- Generate employee-wise and month-wise reports  
- Ensure data consistency using relational database design  

---

## 🚀 Key Features

### 👥 Employee Details Management
- Add new employee records  
- Modify existing employee information  
- Delete employee records  
- Display all employee data  
- Search employee by unique ID  

### 💰 Employee Salary Management
- Enter salary details with automatic calculation of:
  - Dearness Allowance (DA)
  - House Rent Allowance (HRA)
  - Medical Allowance (MA)
  - Provident Fund (PF)
  - Gross Salary
- Generate month-wise salary statements  
- Generate employee-wise salary history  

### ⚙️ System Capabilities
- Menu-driven console interface  
- Automatic database and table creation  
- Input validation and error handling  
- Confirmation messages after each transaction  

---

## 🛠️ Tools & Technologies

- **Programming Language:** Python  
- **Database:** MySQL  
- **Connector:** `mysql.connector`  
- **Concepts Applied:**
  - SQL (CRUD operations)
  - Relational database design
  - Backend logic implementation
  - Conditional flows and loops
  - Error handling

---

## 🗄️ Database Structure

### Employee Table
- Employee Number  |  Name  |  Address  |  Contact Number  |  Designation  

### Salary Table
- Employee Number  |  Salary Date  |   Basic Salary  |  DA  |  HRA  |  MA  |  PF  |  Gross Salary  

---

## 📊 System Preview

### 🗃️ Tables in Database
![Tables](assets/tables_in_database.png)

### 🧱 Employee Table Structure
![Employee Table Structure](assets/employee_table_structure.png)

### 🧾 Salary Table Structure
![Salary Table Structure](assets/emp_salary_table_structure.png)

### 📄 Employee Data Sample Output
![Employee Sample Output](assets/employee_sample_output.png)

### 📄 Salary Data Sample Output
![Salary Sample Output](assets/emp_salary_sample_output.png)

---

## 🔄 Project Flow

### 1️⃣ Main Menu
- Employee Detail Management  
- Employee Salary Management  
- Exit  

### 2️⃣ Employee Detail Module
- Insert  Employee Record
- Modify  Employee Record
- Delete  Employee Record
- Search  Employee Record
- Display  Employee Record

### 3️⃣ Salary Module
- Insert salary details  
- View month-wise salary statements  
- View employee-wise salary history  

---

## ▶️ How to Run the Project

1. Install **Python** and **MySQL**
2. Install MySQL connector:

```bash
pip install mysql-connector-python
```

3. Update MySQL credentials in the Python file
4. Run the script:

```bash
python employee_management.py
```

5. Follow the on-screen menu options

---

## 📦 Output

- Console-based interactive Employee Management System  
- Persistent employee and salary data stored in MySQL  
- Automated salary calculations  
- Structured salary reporting  

---

## 📚 Learning Outcomes

- Hands-on experience with Python–MySQL integration  
- Practical understanding of relational database schema design  
- Implementation of SQL-based CRUD operations  
- Backend business logic development  
- Structured data validation and error handling  

---

## 🔮 Future Enhancements

- GUI-based interface using Tkinter or PyQt  
- Role-based access control (Admin / HR)  
- Export salary reports to Excel or PDF  
- Web-based version using Flask or Django  
- Dashboard visualization using BI tools  

---
## 📌 Project Category

**Backend Development | Database Systems | HR Data Management | Business Logic Automation*
