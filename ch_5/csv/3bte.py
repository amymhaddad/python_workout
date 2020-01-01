import csv, random


with open("random_nums.csv", "w", newline="") as csvfile:
    number_writer = csv.writer(csvfile, delimiter=" ")
    total_lines = 5

    for line in range(1, total_lines + 1):
        ten_random_numbers = random.sample(range(10, 100), 10)
        number_writer.writerow(ten_random_numbers)


with open("random_nums.csv", "r", newline="") as csvfile:
    number_reader = csv.reader(csvfile, delimiter=" ")

    number_lists = list(number_reader)

    sum_average = {}
    sum_ints = 0
    average = 0
    for i, numbers in enumerate(number_lists):
        for number in numbers:
            sum_ints += int(number)
        average += sum_ints / len(numbers)
        sum_average[i + 1] = [sum_ints, average]

for row, totals in sum_average.items():

    outcome = "Row {}: sum is {}, average is {:.2f}".format(row, totals[0], totals[1])
    print(outcome)
