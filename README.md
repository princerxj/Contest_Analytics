# 📊 Codeforces Contest Analytics
![FlowChart](<Untitled (5).jpg>)

A Python-based mini project for analyzing Codeforces contest data. This project fetches contest standings from the Codeforces API, stores them in a local SQLite database, and provides detailed analytics with visualizations to understand your performance and rank distribution.

## 🎯 Project Overview

This project was created as part of my Data Analysis learning journey. It demonstrates:
- **API Integration**: Fetching data from Codeforces API
- **Database Management**: Using SQLite for data storage
- **Data Analysis**: Computing statistics like rank, percentile, and problems solved
- **Data Visualization**: Creating meaningful plots using Matplotlib

## ✨ Features

- 🔍 Fetch complete contest standings from any Codeforces contest
- 💾 Store data locally in SQLite database
- 📈 Calculate user rank, percentile, and problems solved
- 📊 Visualize rank distribution across all participants
- 📉 Analyze correlation between points and rank
- ⚡ Batch processing with API rate limiting

## 🛠️ Technologies Used

- **Python 3.x**
- **Requests**: For API calls
- **SQLite3**: Local database storage
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **NumPy**: Numerical computations

## 📁 Project Structure

```
Contest_Analytics/
│
├── main.py              # Main entry point
├── fetch_data.py        # API data fetching logic
├── database.py          # Database operations
├── analytics.py         # Analytics and statistics functions
├── plots.py             # Visualization functions
├── requirements.txt     # Project dependencies
├── contest.db          # SQLite database (auto-generated)
└── README.md           # Project documentation
```

## 📋 Prerequisites

- Python 3.7 or higher
- Internet connection (for API calls)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone or download this project**
   ```bash
   cd Contest_Analytics
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the program**
   ```bash
   python main.py
   ```

2. **Enter the required information**
   - Contest ID: The Codeforces contest number (e.g., 1900)
   - Handle: Your Codeforces username

3. **View results**
   - The program will display your rank, problems solved, and percentile
   - Two visualization windows will appear:
     - Rank Distribution histogram
     - Points vs Rank scatter plot

### Example Output

```
Enter Codeforces Contest ID: 1900
Enter Codeforces Handle: tourist

 Fetching contest data... Please wait

 Results : 
Handle     : tourist
Rank       : 1
Solved     : 8
Percentile : 99.95%
Time taken to fetch the records : 12.45 seconds
```

## 📊 Features Breakdown

### 1. Data Fetching (`fetch_data.py`)
- Fetches contest standings using Codeforces API
- Implements batch processing (500 records per request)
- Includes rate limiting to respect API guidelines
- Error handling for invalid contests

### 2. Database Management (`database.py`)
- Creates SQLite database automatically
- Stores standings with: rank, handle, points, penalty, problems solved
- Replaces data on each run to ensure fresh analytics

### 3. Analytics (`analytics.py`)
- **get_rank()**: Retrieves user's rank in the contest
- **get_solved()**: Returns number of problems solved
- **get_percentile()**: Calculates percentile rank among all participants

### 4. Visualizations (`plots.py`)
- **Rank Distribution**: Histogram showing participant distribution across ranks
- **Points vs Rank**: Scatter plot showing correlation between points and rank

## 🔧 Code Structure

### Main Workflow
```python
1. Fetch contest standings from API
2. Store data in SQLite database
3. Query user-specific statistics
4. Generate visualizations
5. Display results
```

## 📚 What I Learned

- Working with REST APIs and handling JSON responses
- Database design and SQL queries with SQLite
- Data processing with Pandas DataFrames
- Creating meaningful visualizations with Matplotlib
- Error handling and user input validation
- Batch processing and rate limiting for API calls
- Modular code organization

## 🐛 Error Handling

The project includes comprehensive error handling for:
- Invalid contest IDs
- User not found in contest
- API failures or network issues
- Empty or invalid input
- Rate limiting and timeouts

## 🔮 Future Enhancements

- [ ] Add more visualization types (box plots, heatmaps)
- [ ] Compare performance across multiple contests
- [ ] Track rating changes over time
- [ ] Export analytics to CSV/PDF
- [ ] Add GUI interface using Tkinter
- [ ] Implement caching to reduce API calls
- [ ] Add problem-wise analysis
- [ ] Support for virtual participation data

## 📝 Notes

- The Codeforces API has rate limits. The program includes delays to respect these limits.
- Contest data is refreshed on each run.
- Database file (`contest.db`) is created automatically in the project directory.
- Visualization windows must be closed to continue program execution.

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- [Codeforces](https://codeforces.com/) for providing the API
- Python community for excellent libraries and documentation

## 📞 Contact

Feel free to reach out for questions or suggestions about this project!

---

**Happy Analyzing! 📊🚀**
