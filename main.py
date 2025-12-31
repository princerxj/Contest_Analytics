from fetch_data import fetch_all_standings
from database import store_standings
from analytics import get_rank, get_percentile, get_solved
from plots import plot_rank_distribution, plot_points_vs_rank
import time

def main():
    try:
        start_time = time.time()
        contest_id = int(input("Enter Codeforces Contest ID: ").strip())
        handle = input("Enter Codeforces Handle: ").strip()

        if not handle:
            raise ValueError("Handle cannot be empty")

        print("\n Fetching contest data... Please wait")

        records = fetch_all_standings(contest_id)

        if not records:
            raise RuntimeError("No standings data found")

        store_standings(records)

        rank = get_rank(handle)
        solved = get_solved(handle)
        percentile = get_percentile(handle)

        if rank is None:
            print(f"\n User '{handle}' not found in contest {contest_id}")
            return

        end_time = time.time()
        print("\n Results : ")
        print(f"Handle     : {handle}")
        print(f"Rank       : {rank}")
        print(f"Solved     : {solved}")
        print(f"Percentile : {percentile}%")
        print(f"Time taken to fetch the records : {format(end_time - start_time)}seconds")

        plot_rank_distribution()
        plot_points_vs_rank()

    except ValueError as ve:
        print(f"\nInput / API Error: {ve}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()