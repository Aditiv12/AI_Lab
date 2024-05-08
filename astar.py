import queue

alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
start='A'
goal='D'
result=''
closed=[]
path=[]
n = int(input("Enter number of vertices: "))
dict_gn={ alpha[i]:{} for i in range(n) }
dict_hn={ alpha[i]:0 for i in range(n) }
print("Enter directed edges with weights below: (press enter to skip edges that are not present)")
for i in range(n):
    for j in range(n):
        if(i!=j):
            try:
                parseIn=int(input(f"Enter weight for edge {alpha[i]}-{alpha[j]}: "))
            except ValueError:
                continue
            dict_gn[alpha[i]][alpha[j]]=parseIn
for i in range(n):
    try:
        dict_hn[alpha[i]] = int(input(f"Enter hueristic value of node {alpha[i]}: "))
    except ValueError:
        print("Invalid value:")

start = input("Enter the start node alphabet: ").upper()
goal = input("Enter the goal node alphabet: ").upper()

print(f'G(n): {dict_gn}')
print(f"H(n): {dict_hn}")

def expand(cityq):
    global result
    global closed
    while not cityq.empty():
        tot, thiscity, g_thisCity=cityq.get()
        closed.append(thiscity)
        path.append(thiscity)
        if thiscity==goal:
            result="-> ".join(path)
            result+='\nTotalCost: {}'.format(tot)
            return 1
        for cty, gn in dict_gn[thiscity].items():
            if cty not in closed:
                cityq.put((dict_hn[cty]+g_thisCity+gn, cty, g_thisCity+gn)) #(Fn, current_city, Gn_tillCurrCity)
        print(f'Queue After processing {thiscity}: ', cityq.queue)
    return 0
def main():
    cityq=queue.PriorityQueue()
    thiscity=start
    cityq.put((0,thiscity, 0)) # Setting highest priority to the start city so it get's popped. 
    if(expand(cityq)):
        print("The A* path with the total cost is: ")
        print(result)
    else:
        print("A* couldn't find a path :/")
main()
