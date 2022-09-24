import matplotlib.pyplot as p
month = ['Jan','Feb','Mar','Apr','May']
Percentage = [33,42,53,49,47]
p.bar(month, Percentage, color=['skyblue', 'skyblue', '#8390FA', 'skyblue', 'skyblue'])
p.title('Death Rate Of India')
p.xlabel('Month')
p.ylabel('Percentage')
p.show()
