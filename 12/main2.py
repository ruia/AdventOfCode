import time
 
start_time=time.time()

data= []
with open("input.txt") as file:
    for idx1,line in enumerate(file):
        data.append([])
        for idx2,char in enumerate(line.strip()):
            data[idx1].append(char)
            if char=="S":
                S=(idx1,idx2)
                data[S[0]][S[1]]="a"
            elif char=="E":
                E=(idx1,idx2)
                data[E[0]][E[1]]="z"

 
 
def BFS(data,start,end,part2):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    row = len(data)
    col = len(data[0])
 
    visited=[]
 
    q = []
    q.append(start)
 
    v=[[0 for i in range(col)] for _ in range(row)]
    
    while(len(q) > 0) :
        p = q[0]
        q.pop(0)
            
        
        if part2 and data[p[0]][p[1]]=="a":
            return (v[p[0]][p[1]])
        elif not part2 and p==end:
            return v[end[0]][end[1]]
 
        for i in range(4) :
            a = p[0] + dirs[i][0]
            b = p[1] + dirs[i][1]
 
            if(a >= 0 and b >= 0 and a < row and b < col and (ord(data[a][b])>=ord((data[p[0]][p[1]])) or ord(data[a][b])+1==ord((data[p[0]][p[1]]))) and (a,b) not in visited):  
                q.append((a, b))
                visited.append((a,b))
                v[a][b]=v[p[0]][p[1]]+1
 
    return None
 
 
 
print("Part 1:",BFS(data,E,S,False))
print("Part 2:",BFS(data,E,S,True))
 
end=time.time()
print("Time:", end-start_time)
