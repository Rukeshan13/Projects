# 🏥 Hospital Patient Queue (Python)

A **Hospital Queue Management System** implemented in Python.  
This project demonstrates how to manage **emergency** and **regular** patients using **priority queues** and **normal queues** while estimating patient wait times.  

---

## 📌 Overview
The system simulates a **hospital queue** where:
- **Emergency patients** are given priority and served first.
- **Regular patients** are managed in a **normal FIFO queue**.
- The program displays an **estimated wait time** for each new patient based on average service time.
- Patients are served in the correct order: **Emergency → Regular**.

---

## ✨ Features
- 🚑 **Add Patient** – Add emergency or regular patients to the queue.  
- ⏱ **Estimated Wait Time** – Displays expected wait time when a patient is added.  
- 🩺 **Serve Patient** – Processes patients in the correct priority order.  
- 📋 **Queue Management** – Handles multiple patients efficiently.  
- 🖥 **Menu-driven simulation** (optional for interactive usage).  

---

## 🛠 Data Structures Used
- **Priority Queue (`heapq`)**  
  - Stores **emergency patients**.  
  - Ensures they are always served before regular patients.  

- **Normal Queue (`collections.deque`)**  
  - Stores **regular patients** in **FIFO order**.  

- **Custom `Patient` Class**  
  - Stores patient details: `name`, `is_emergency`, `arrival_time`.  

---

## ▶️ How It Runs
1. Clone this repository:
   git clone https://github.com/your-username/hospital-patient-queue.git
   cd hospital-patient-queue

