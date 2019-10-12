people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
 ]


last_names = []

for person in people:
    # for category, details in person.items()
    for cateogory, details in person.items():
        if cateogory == 'last':
            last_names.append(details)

sorted_last_names = sorted(last_names)



        
