n = int(input())
maxLength = n // 2

#This portion sorts the boards by height.
boards = [int(s) for s in input().split()]
heights = set(boards)
lHeights = list(heights)
lHeights.sort()

#This portion assesses the possible heights.
possHeights = []
for height in lHeights:
  for i in range(len(lHeights)):
    if lHeights[i] != height:
      possHeights.append(lHeights[i] + height)
setPossHeights = set(possHeights)
print(setPossHeights)

#This portion adds boards of a particular type 
#to a 2d list corresponding to their height.
boardTypes = []
for i in range(len(heights)):
  boardTypes.append([])
for i in range(len(boards)):
  for j in range(len(lHeights)):
    if boards[i] == lHeights[j]:
      boardTypes[j].append(boards[i])
print(boardTypes)
