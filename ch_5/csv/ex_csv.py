import csv

# with open('example.csv', 'w') as f:
#     #create a csv.writer object
#     o = csv.writer(f)
#     o.writerow(range(5))
#     o.writerow(['a', 'b', 'c', 'd', 'e'])


with open("example.csv", "w") as f:
    # create a csv.writer object with a specific delimiter
    o = csv.writer(f, delimiter=":")
    o.writerow(range(5))
    o.writerow(["a", "b", "c", "d", "e"])


# root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
# root    0
