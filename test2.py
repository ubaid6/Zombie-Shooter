openFile = open("leaderboard.txt", "r")
read = openFile.read()

results =  []

read = read.split('\n')
for i in read:
    results.append(i.strip().split(','))
results.sort(key = lambda x: int(x[1]), reverse = True)
    # results.split(","))
# read.strip()
print(results)
