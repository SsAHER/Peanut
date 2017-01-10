processes = int(input('Enter no. of processes :  '))
dictonary = {}
process_id = []

for x in range(processes):
    arrival_time = int(input('Enter arrival time :  '))
    burst_time = int(input('Enter burst time :  '))
    priority = int(input('Enter priority :  '))
    process_id.append(x)
    dictonary[int(x)] = [arrival_time, burst_time,priority]

print"Process    Arrival Time    Burst Time    Priority "
for x in range(len(dictonary)):
    print x + 1, "       |     ", dictonary[int(x)][0], "      |      ", dictonary[int(x)][1], "      |      ", dictonary[int(x)][2]

start_t = {}
dictonary2 = dictonary.copy()
time = 0
Wait = 0.0
burst = 0
dict_index = 0
dict_arrival = 0
dict_burst = 0
dict_priority =0
p_index = 0

while 1:
    if len(dictonary) == 0:
        break
    for x in range(len(process_id)):
            dict_index = process_id[x]
            dict_arrival = dictonary[process_id[x]][0]
            dict_burst = dictonary[process_id[x]][1]
            dict_priority = dictonary[process_id[x]][2]
            p_index = x
            break
    for x in range(len(process_id)):
            if dictonary[dict_index][0] >= dictonary[process_id[x]][0] and dictonary[dict_index][2] > dictonary[process_id[x]][2]:
                dict_index = process_id[x]
                p_index = int(x)
                dict_arrival = dictonary[process_id[x]][0]
                dict_burst = dictonary[process_id[x]][1]
                dict_priority = dictonary[process_id[x]][2]

    del dictonary[dict_index]
    del process_id[p_index]

    check_arrival = 0
    burst = 0

    while dict_burst != burst:
        if dict_arrival <= time:
            burst += 1
            if check_arrival == 0:
                start_t[int(dict_index)] = time
                check_arrival = 1
        time += 1

print "\nprocess    Start Time   waiting Time "
for x in range(len(dictonary2)):
    ProcessWait = start_t[x] - dictonary2[int(x)][0]
    Wait += ProcessWait
    print x + 1,"         ",start_t[int(x)],"             ", ProcessWait
    
print "\nAverage waiting time is:", Wait / processes
