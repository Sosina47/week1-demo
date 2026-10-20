import csv
import numpy as np 

def load_data(filename):
    # load csv rows
    with open(filename, 'r', newline="") as file: 
        return list(csv.DictReader(file))

def clean_data(data): 
    # remove duplicate and reject records with invalid scores. 
    cleaned = []
    rejected = []
    seen = set()

    for row in data: 
        student = row['student']

        # 1. skip exact duplicate records. 
        record_key = tuple(row.items())

        if record_key in seen: 
            continue
        seen.add(record_key)

        # 2. check scores are numeric
        try: 
            math_score = float(row["math_score"])
            python_score = float(row["python_score"])

        except ValueError:
            rejected.append((student, "missing or non-numeric score"))
            continue

        # 3. check scores are within the valid range
        if not(0 <= math_score <= 100 and 0 <= python_score <= 100):
            rejected.append((student, "score outside 0 - 100"))
            continue

        # 4. store valid scores as numbers. 
        cleaned.append({
            "student": student, 
            "math_score": math_score, 
            "python_score": python_score
        })

    return cleaned, rejected

def analyze_data(cleaned): 
    # calculate statics using numpy
    math_score = np.array(
        [row["math_score"] for row in cleaned]
    )
    python_score = np.array(
        [row["python_score"] for row in cleaned]
    )

    subjects = {
        "math": math_score, 
        "pyton": python_score
    }

    for subject, score in subjects.items():
        print(f"\n{subject} statistics")
        print("-" * 25)
        print(f"Number of scores:", score.size)
        print(f"Mean: {np.mean(score):.2f}")
        print(f"Median: {np.median(score):.2f}")
        print(f"minimum: {np.min(score):.2f}")
        print(f"maximum: {np.max(score):.2f}")
        print(f"standard deviation: {np.std(score):.2f}")


data = load_data("data.csv")
cleaned_data, rejected_data = clean_data(data) 

print("cleaned records:")
for row in cleaned_data:
    print(row)

print("\nRejected recors:")
for student, reason in rejected_data:
    print(f"{student}: {reason}")

analyze_data(cleaned_data)