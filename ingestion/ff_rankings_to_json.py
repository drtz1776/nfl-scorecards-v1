
import nflreadpy as nfl
import polars as pl
import json
from pathlib import Path

# Load weekly fantasy football rankings
ff_rankings = nfl.load_ff_rankings(type="week")

# Filter to 2026 if season field exists
if "season" in ff_rankings.columns:
    ff_rankings = ff_rankings.filter(
        pl.col("season") == 2026
    )
else:
    print("Warning: No season column found.")
    print("Exporting available weekly rankings unfiltered.")

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "ff_rankings_2026.json", "w") as f:
    json.dump(
        ff_rankings.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {ff_rankings.height:,}")
print(f"Columns: {ff_rankings.width:,}")

print("\nAvailable columns:")
for col in ff_rankings.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")
