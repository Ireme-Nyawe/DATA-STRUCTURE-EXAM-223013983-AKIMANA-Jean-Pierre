# GROUP 1: Student Gradebook System

## Objective
This project demonstrates the use of Object-Oriented Programming in C++ to manage different types of students and compute their GPAs.
The system uses inheritance to classify students and a central `GradeSystem` to manage them.

## Class Design

- **Student (Base Class)**  
  Contains common attributes such as `name`, `studentID`, and `grades`. Also includes functions to add grades, compute GPA, and display student information.

- **UGStudent (Undergraduate)**  
  Inherits from `Student` to represent undergraduate students. Demonstrates hierarchical inheritance.

- **PGStudent (Postgraduate)**  
  Inherits from `Student` to represent postgraduate students. Also part of hierarchical inheritance.

- **ResearchStudent**  
  Inherits from `PGStudent` to demonstrate **multilevel inheritance**.

- **GradeSystem**  
  Manages multiple students using a `vector<Student*>`, demonstrating **hybrid inheritance** by aggregating objects of derived classes.

## Features

- Add grades and compute GPA for each student
- Display detailed student information
- Proper memory management using virtual destructors
- Use of polymorphism for flexible object handling


## How to Run

1. Save the code as `main.cpp`.
2. Compile the code using:

```bash
g++ -o gradebook main.cpp

```
-------------------------------------------------------------------------------------
## Participants 
| S/N | REG        | Last Name     | First Name     |
|-----|------------|---------------|----------------|
| 1   | 223013983  | AKIMANA       | Jean Pierre    |             
| 2   | 223007511  | NIYONSABA     | Erina          |   
| 3   | 223004810  | NIYONSENGA    | Ange Carine    |             
| 4   | 223016138  | Niyonsenga    | Aphrodis       |             
| 5   | 223011216  | NIYONSHUTI    | Florence       |             
| 6   | 223011370  | NICYOGIHE     | Rebeca         |             
| 7   | 221007304  | MUTONI        | AIMABLE        |             
| 8   | 223018803  | MUKAMA        | UYISENGA Lea   |       
| 9   | 223010019  | MUKAMAKOMBE   |  Violette      |        
| 10  | 223009957  | MUNEZERO      | Grace          |   
