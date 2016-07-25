import fileinput

indexID = 2
indexT = 3

split = ';'

for line in fileinput.input():

value = line.split(split)
machine = values[indexID]
downT = values[indexT].replace("\n","")
print(('{0}\t{1}'.format(machine, downT)))