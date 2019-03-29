def openfile(filename):
    with open(filename, "r") as file:
        years = []
        for line in file:
            year = line.strip("\n").split("\t")
            if year[1] == '':
                year[1] = '2018'
            year[0] = int(year[0])
            year[1] = int(year[1])
            years.append(year)
    return years
def average(turnovers):
    totalturnover = 0
    for turnover in turnovers:
        yearworked = turnover[1]-turnover[0]
        totalturnover = totalturnover + yearworked
    averageturnover = totalturnover / len(turnovers)
    return averageturnover

turnovers = openfile("employees.txt")
average_turnover = average(turnovers)
print("average turnover for company is:", average_turnover)
       