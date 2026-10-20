
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = (
    ROOT
    / "external"
    / "OneStop-Eye-Movements"
    / "data"
    / "OneStop"
    / "ordinary"
)

files = [
    "ia_Paragraph_ordinary.csv",
    "fixations_Paragraph_ordinary.csv",
]

for filename in files:
    path = DATA_DIR / filename

    print("\n" + "=" * 65)
    print(f"INSPECTING: {filename}")
    print("=" * 65)

    if not path.exists():
        print(f"FILE NOT FOUND: {path}")
        continue

    # Inspect a sample first to avoid loading
    # the entire large dataset into memory.
    df = pd.read_csv(
        path,
        sep=None,
        engine="python",
        na_values=["."],
        nrows=1000,
        low_memory=False if False else True
    )

    print("\n1. SAMPLE DIMENSIONS")
    print(f"Rows sampled: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\n2. COLUMN NAMES")
    for col in df.columns:
        print(col)

    print("\n3. DATA TYPES")
    print(df.dtypes.to_string())

    print("\n4. FIRST THREE ROWS")
    print(df.head(3).to_string())

    print("\n5. MISSING VALUES IN SAMPLE")
    print(
        df.isna()
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .to_string()
    )

    print("\n6. RESEARCH VARIABLES")
    for col in [
        "participant_id",
        "trial_index",
        "list_number",
        "is_correct",
        "difficulty_level",
        "question_preview",
        "repeated_reading_trial",
    ]:
        if col in df.columns:
            print(f"[FOUND] {col}")
        else:
            print(f"[NOT FOUND] {col}")

print("\nInspection finished.")
