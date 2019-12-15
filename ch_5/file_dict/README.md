In this exercise, we’ll be working with /etc/passwd, the file in which Unix and Linux systems store information about their users. If you don’t have access to such a file, you can download one that I’ve uploaded, at https://gist.github.com/reuven/7647d1af56cc8c6a9744 .

Here’s a sample of what the file looks like:
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false

Each line is one user record, divided into colon-separated fields. The first field (index 0) is the username, and the third field (index 2) is user’s unique ID number. In the system from which I took the above /etc/passwd file, nobody has ID -2, root has ID 0, and daemon has ID 1. For our purposes, you can ignore all but these two fields.

Sometimes, the file will contain lines that fail to adhere to this format. For example, we generally ignore lines containing nothing but whitespace. Some vendors (e.g., Apple) include comments in their /etc/passwd files, in which the line starts with a # character.

For this exercise, create a dictionary based on /etc/passwd, in which the dict’s keys are usernames and the values are the users' IDs. Once you have created the dictionary, iterate over it, displaying the usernames and associated IDs in alphabetical order.