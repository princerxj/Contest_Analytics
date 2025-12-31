import requests
import time

BASE_URL = "https://codeforces.com/api/contest.standings"

def fetch_all_standings(contest_id, batch_size=500):
    """
    Fetches all contest standings from Codeforces API.
    Raises exceptions if contest does not exist or API fails.
    """

    start = 1
    all_records = []

    while True:
        response = requests.get(
            BASE_URL,
            params={
                "contestId": contest_id,
                "from": start,
                "count": batch_size
            }
        )

        data = response.json()
        if data.get("status") != "OK":
            raise ValueError(
                f"Failed to fetch contest {contest_id}: {data.get('comment', 'Unknown error')}"
            )

        rows = data["result"]["rows"]

        if not rows:
            break

        for r in rows:
            solved_count = sum(
                1 for p in r["problemResults"] if p["points"] > 0
            )

            all_records.append({
                "rank": r["rank"],
                "handle": r["party"]["members"][0]["handle"],
                "points": r["points"],
                "penalty": r["penalty"],
                "solved": solved_count
            })

        start += batch_size
        time.sleep(0.3)

    return all_records