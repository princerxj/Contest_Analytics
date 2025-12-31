import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_rank_distribution(db_name="contest.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql("SELECT rank FROM standings", conn)
    conn.close()

    plt.hist(df["rank"], bins=50)
    plt.xlabel("Rank")
    plt.ylabel("Number of Participants")
    plt.title("Rank Distribution")
    plt.show()


def plot_points_vs_rank(db_name="contest.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql("SELECT rank, points FROM standings", conn)
    conn.close()

    plt.scatter(df["rank"], df["points"], s=10)
    plt.xlabel("Rank")
    plt.ylabel("Points")
    plt.title("Points vs Rank")
    plt.show()
