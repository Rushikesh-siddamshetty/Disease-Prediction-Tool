# Disease Prediction Tool


# Medical Diagnosis Assistant & Food Ordering Chatbot

This repository contains two Python applications:

1. **Medical Diagnosis Assistant** (GUI, Tkinter)
2. **Food Ordering Chatbot** (Command-line)

---

## 1. Medical Diagnosis Assistant

A user-friendly desktop application that predicts possible diseases based on selected symptoms. It provides disease descriptions and recommended precautions.

### Features

- Select disease categories (e.g., Respiratory, Digestive, Cardiovascular, etc.)
- Choose symptoms from a dynamic list
- Get disease predictions based on your symptoms
- View disease descriptions and precautions

### Requirements

- Python 3.x
- Tkinter (usually included with Python)
- CSV files:  
  - `dataset1.csv` (disease-symptom mapping)  
  - `symptom_Description.csv` (disease descriptions)  
  - `symptom_precaution.csv` (disease precautions)

### How to Run

```bash
python daa.py
```

A GUI window will open. Follow the on-screen instructions to use the application.

---

## 2. Food Ordering Chatbot

A simple command-line chatbot for placing food orders, viewing the menu, and processing payments.

### Features

- View menu items and prices
- Add items to your order
- View your order summary
- Process payment (simulated)
- Confirm and end your order

### How to Run

```bash
python venkat.py
```

Follow the prompts in your terminal to interact with the chatbot.

---

## File Structure

```
.
├── daa.py
├── venkat.py
├── dataset1.csv
├── symptom_Description.csv
├── symptom_precaution.csv
├── dataset.csv
```

---

## License

This project is for educational purposes.

---

Let me know if you want to customize or add anything else!
