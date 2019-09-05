total_run_times = []
run_count = 0

while True:
    run_time = input("Enter your 10km run time in minutes: ")

    if run_time == "q":
        break
    else:
        run_count += 1
        total_run_times.append(int(run_time))

average = sum(total_run_times) / run_count
print(f"Your average run time is {average:.2f} minutes over {run_count} runs.")
