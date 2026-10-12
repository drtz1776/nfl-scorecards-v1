
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Directory containing this master script
BASE_DIR = Path(__file__).resolve().parent

# Scripts to execute
scripts = [
    "ff_rankings_to_json.py",
    "load_officials_to_json.py",
    "load_schedules_to_json.py",
    "next_gen_stats_to_json.py",
    "play_by_play_to_json.py",
    "player_info_to_json.py",
    "player_stats_to_json.py",
    "snap_count_to_json.py",
    "team_stats_to_json.py",
    "teams_to_json.py",
]

def run_all():
    print("=" * 60)
    print("NFLVERSE DATA INGESTION")
    print(f"Started: {datetime.now()}")
    print("=" * 60)

    failed = []

    for index, script in enumerate(scripts, start=1):
        print(f"\n[{index}/{len(scripts)}] Running {script}", flush=True)

        script_path = BASE_DIR / script

        if not script_path.exists():
            print(f"ERROR: {script} not found")
            failed.append(script)
            continue

        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=BASE_DIR
        )

        if result.returncode == 0:
            print(f"SUCCESS: {script}")
        else:
            print(f"FAILED: {script}")
            failed.append(script)

    print("\n" + "=" * 60)
    print("INGESTION SUMMARY")
    print("=" * 60)
    print(f"Total: {len(scripts)}")
    print(f"Successful: {len(scripts) - len(failed)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed scripts:")
        for script in failed:
            print(f" - {script}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run_all())
