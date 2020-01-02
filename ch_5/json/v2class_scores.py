import json, os


dir = "./scores"

filenames = [os.path.join(dir, file) for file in os.listdir(dir) if os.path.isdir(dir)]
print(filenames)
scores = {}

for filename in filenames:
    scores[filename] = {}

    j_obj = open(filename)
    for result in json.load(j_obj):
        for subject, grades in result.items():
            scores[filename].setdefault(subject, [])
            scores[filename][subject].append(grades)

    for subject, grades in scores[filename].items():
        min_scores = min(grades)
        max_scores = max(grades)
        ave_scores = float(sum(grades) / len(grades))
        print(f" {subject}: min {min_scores} max {max_scores} ave {ave_scores}")
