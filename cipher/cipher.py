import argparse
import time
from random import randint
import sys

parser = argparse.ArgumentParser(description="Number of Players")
parser.add_argument("-p", "--players", type=int, default=1)
parser.add_argument("-r", "--rounds", type=int, default=3)
args = parser.parse_args()
players = args.players
rounds = args.rounds

if players > 4:
	print("Duhh ... way too many players.")
	sys.exit(0)
elif rounds > 3:
	print("Duhh ... way too many rounds.")
	sys.exit(0)

rules = f"There shall be {rounds} rounds. In each round a word shall be given to each player. The word has been encrypted using Caesar cipher by the mighty Caesar himself. Each player has to decipher the word. Each correct answer will get one point. In case of a tie. Player who took less time to guess the correct words shall win."

print("\n")
print(rules+"\n")
input("Ready Players ?")

points = [0 for i in range(players)]
times = [0 for i in range(players)]

words = ["tree", "ferrari", "oxford", "rushmore", "chains", "apple", "swimming", "cranberry", "connection", "france", "tennis", "efficiency", "teaching", "music", "trainer", "disk", "drama", "dealer", "attention", "video", "variety", "employee", "failure", "guidance", "freedom", "science", "injury", "vehicle", "imagination", "government", "dawn", "oral", "meaning", "knife", "wolf", "tradition", "music", "movies", "china", "phone",
"duke", "owner", "mountain", "destruction", "fragment", "inception", "prestige", "chicken"]

indexes = set()
while len(indexes) < players*rounds:
	indexes.add(randint(0, len(words)-1))

answers = [words[x] for x in indexes]
ques = []
for i in range(len(answers)):
	word = answers[i]
	ahead = randint(1, 25)
	newWord = "".join(chr(((ord(x)-97+ahead)%26)+97) for x in word)
	ques.append(newWord)
cur = 0

for roundNumber in range(1, rounds+1):
	print("\n")
	print(f"Round {roundNumber}")
	print("\n")
	for player in range(players):
		input(f"Ready player {player+1} ?")
		print(f"The encrypted word is : {ques[cur]}")

		t = time.time()
		res = input("Your answer : ")
		times[player] += time.time()-t
		if res == answers[cur]:
			points[player] += 1
		
		cur += 1

m = -1
t = float("inf")
for i in range(players):
	print(f"Player{i+1}	Points:{points[i]}	Time:{round(times[i], 2)}")
	if (points[i] > m) or (points[i] == m and times[i] < t):
		m = points[i]
		t = times[i]
		winner = i

print(f"The winner is Player{i+1} with {m} points and {round(t, 2)} seconds.")

