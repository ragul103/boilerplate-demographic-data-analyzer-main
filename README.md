
# 📊 Demographic Data Analyzer

This project analyzes demographic data extracted from the U.S. Census dataset.  
It calculates statistics such as race counts, average age of men, education levels, working hours, income distribution, and occupations.

---

## 🚀 Features
- 📌 Count the number of each race represented in the dataset  
- 👨 Calculate the average age of men  
- 🎓 Compute the percentage of people with a Bachelor's degree  
- 📈 Compare income levels based on education  
- ⏳ Find the minimum number of work hours per week  
- 💰 Identify the percentage of rich people who work the fewest hours  
- 🌍 Determine the country with the highest percentage of people earning >50K  
- 🇮🇳 Find the most popular occupation for rich people in India  
- 🧪 Includes **unit tests** to validate calculations  

---

## 🛠️ Technologies Used
- 🐍 Python 3.x  
- 🐼 Pandas  
- 🔢 NumPy  
- 🧑‍⚖️ Unittest (for testing)  

---

## 📂 Project Structure
```

boilerplate-demographic-data-analyzer-main/
│
├── demographic\_data\_analyzer.py   # Main analysis code
├── test\_module.py                 # Unit tests
├── main.py                        # Script to run the project
├── README.md                      # Project documentation
└── .venv/                         # Virtual environment (not uploaded to GitHub)

````

---

## ▶️ How to Run

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/ragul103/demographic-data-analyzer.git
   cd demographic-data-analyzer
   ```

2. ⚙️ (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```

3. 📦 Install dependencies:

   ```bash
   pip install pandas numpy
   ```

4. ▶️ Run the program:

   ```bash
   python main.py
   ```

5. 🧪 Run tests:

   ```bash
   python -m unittest test_module.py
   ```

---

## ✅ Example Output

```
📊 Number of each race:
 White                 27816
 Black                  3124
 Asian-Pac-Islander     1039
 Amer-Indian-Eskimo      311
 Other                   271

👨 Average age of men: 39.4
🎓 Percentage with Bachelors degrees: 16.4
📈 Percentage with higher education that earn >50K: 46.5
📉 Percentage without higher education that earn >50K: 17.4
⏳ Min work hours: 1
💰 Percentage of rich among those who work fewest hours: 10.0
🌍 Country with highest % of >50K: Iran
🏆 Highest % of rich people in country: 41.9
🇮🇳 Top occupation in India for those who earn >50K: Prof-specialty
```

---

## 👤 Author

* ✍️ **Ragul R** (replace with your name)
* 🐙 GitHub: [ragulr](https://github.com/ragul103)

---

## 📜 License

⚖️ This project is licensed under the MIT License - feel free to use and modify.

```

Would you like me to also **style the headings** with emojis (like `## 🚀 Features` → `## 🚀✨ Features`), or keep them as they are now?
```
