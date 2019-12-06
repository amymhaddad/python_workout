# Option 1
run_times = []

while True:
    user_run_time = input("Enter 10 km run time, or 'q' to exit:  ")
    if user_run_time == "q":
        print(sum([float(num) for num in run_times]) / len(run_times))
        break
    else:
        run_times.append(user_run_time)


# Option 2
run_times = []

while True:
    user_run_time = input("Enter 10 km run time, or 'q' to exit:  ")
    if user_run_time == "q":
        time = sum([num for num in run_times]) / len(run_times)
        print("The average run time is {:.2f} for {} runs".format(time, len(run_times)))
        break

    else:
        try:
            run_times.append(float(user_run_time))
        except ValueError:
            print("You need to enter a number.")
            user_run_time = input("Enter 10 km run time, or 'q' to exit:  ")
