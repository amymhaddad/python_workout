import glob, json, os
from collections import defaultdict

# when necessary to use load()-- reads in -- vs loads() -- turns into python obj--

scores_by_class = {}
# Read in all files in the "scores" dir and parse the json data into python objects --> {class name : {}}
for file in glob.glob("./scores/*"):
    # create a dictionary that adds each class name (ie, file name) and sets the class name to an empty dictionary
    scores_by_class[file] = {}
    with open(file) as json_object:
        class_obj = json.load(json_object)

    # create a new dictionary that's set -- by default -- to a list --> {"math": []}
    # the key is the course name and the value is the list of grades associated with each course. I append the grades to the list by course name
    subject_grades = defaultdict(list)
    for class_data in class_obj:
        for subject, grades in class_data.items():
            subject_grades[subject].append(grades)
    # update the parent dictionary -- scores_by_class -- with information from subject_grade
    for class_name, grades in scores_by_class.items():
        grades.update(subject_grades)

# calculate the totals in each list
totals_per_class = defaultdict(str)
output = ""
for class_name, courses_and_grades in scores_by_class.items():
    output += class_name + "\n"
    for subject, grades in courses_and_grades.items():
        max_grade = max(grades)
        min_grade = min(grades)
        average = sum(grades) / len(grades)
        stats = "min {} max {} ave {:.0f}\n".format(min_grade, max_grade, average)
        output += stats

print(output)
