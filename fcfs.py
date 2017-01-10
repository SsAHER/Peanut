arrival_time = []
burst_time = []
waiting_time = [0]
finish_time = []
index=0
index1=0
processes=0

print "Enter number of processes:"
processes = input()

while index<processes :
	print "Enter arrival times:"
	a = input()
	arrival_time.append (a)
	index+=1

while index1<processes :
	print "Enter burst times:"
	b = input()
	burst_time.append (b)

	index1+=1


for x in range(processes):
	a = burst_time[x] + arrival_time[x] + waiting_time[x]
	finish_time.append(a)
	if x<processes-1:
		z = finish_time[x] - arrival_time[x+1]
		waiting_time.append(z)


print "Waiting time is: " , waiting_time

print "Finish time is: " , finish_time

calculate_wait = 0.0
for x in range (processes):
  c = waiting_time[x]
  calculate_wait +=c
print "Average waiting time is: " , calculate_wait/processes





