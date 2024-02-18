import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def plot_hist(x, bins):
  hist, bins = np.histogram(x, bins=bins)
  plt.hist(x, bins=bins)
  plt.title('Histogram of Arrival Delays')
  plt.xlabel('Length of string ')
  plt.ylabel(f"Probability of consequtive {len(special)} zeroes")
  plt.legend()


#def plot_loghist(x, bins):
#  hist, bins = np.histogram(x, bins=bins)
#  logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
#  plt.hist(x, bins=logbins)
#  plt.xscale('log')
#  plt.title('Histogram of Arrival Delays')
#  plt.xlabel('Length of string ')
#  plt.ylabel(f"Probability of consequtive {len(special)} zeroes")
#  plt.legend()

def Average(lst):
    return sum(lst) / len(lst)

def generate_binary_sequence(length):
	my_list = ''
	for n in range(length):
		r = randrange(2)
		my_list+=str(r)
	return my_list

from random import randrange
#old:lengths=[]
#New for loop in newer version
special = '010111000'
probabilities = []
occurances = {}
Trials = 1000

for how_many_sequences in range(1,2048*64,1):
	occurances[how_many_sequences]=0
	for again_and_again in range(Trials):

		#Generating [X] sequence of length [Len], and find occurences
		occurance=0
		for repeat in range(how_many_sequences+1):
			my_list = generate_binary_sequence(len(special))
#			print(my_list)
			if special == my_list:
				occurance+=1
#		print(f"Sequence {special} occured {occurance} times, in {how_many_sequences} random sequence.")
#		print(f"occurances = {occurances[how_many_sequences]}/{how_many_sequences} -> {occurances[how_many_sequences]/how_many_sequences}")
		occurances[how_many_sequences]+=occurance
	print(f"Sequence {special} occured {occurances[how_many_sequences]} times, in {how_many_sequences} random sequence, with {Trials} trials")
#	probabilities.append(occurances[how_many_sequences]/how_many_sequences)
#	extra=''
#	if Average(probabilities) !=0:
#		extra = f"1/{int(1/Average(probabilities))}"
#	print(f"{how_many_sequences}->{occurances[how_many_sequences]}")
	
#		print(f"max={max(probabilities)}, min={min(probabilities)}, Average(probabilities): {Average(probabilities):05f} {extra}")
#Oldversion
#	for n in range(1000000):
#		r = randrange(2)
#		my_list+=str(r)
#		if special in my_list:
#			lengths.append(len(my_list))
#			print(f"{len(lengths)}: At length {len(my_list)} found consequtive {len(special)} zeroes, at: {my_list[0:10]}...")
#			break

exit()
print(f"len(occurances): {len(occurances)}")
print(f"lengths: {occurances}")
print(f"min(occurances): {min(occurances)}")
print(f"max(occurances): {max(occurances)}")
print(f"Average(occurances): {Average(occurances)}")

plot_hist(occurances, 100)
#plt.show()

#print(f"len(lengths): {len(lengths)}")
#print(f"lengths: {lengths}")
#print(f"min(lengths): {min(lengths)}")
#print(f"max(lengths): {max(lengths)}")
#print(f"Average(lengths): {Average(lengths)}")

#plot_hist(lengths, 100)
#plt.show()

#plot_loghist(lengths, 100)
#plt.show()

