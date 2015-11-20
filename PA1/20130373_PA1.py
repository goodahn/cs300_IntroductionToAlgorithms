##direction!
##diag=1 right=2 down=3
def check(a,b,c,d):
    result_x=0
    result_y=0
    for i in range(len(c)):
        if(c[i]==a):
            result_x=i
        if(c[i]==b):
            result_y=i
    return d[result_x][result_y]

if __name__=="__main__":
    list_s=['A','T','G','C']
    score=[]
    table=[]
    table_l=[]
    tmp=''
    local_1=''
    local_2=''
    global_1=''
    global_2=''
    local_p=[0,0,0]
    for i in range(4):
        var=raw_input()
        score.append(var.split( ))
           
    gap_penalty=int(raw_input())
    seq_1=raw_input()
    seq_2=raw_input()
## get input
    for i in range(len(seq_2)+1):
        table.append([])
        for j in range(len(seq_1)+1):
            table[i].append([0,0])

    for i in range(len(seq_1)):
        table[0][i+1][0]=table[0][i][0]+gap_penalty
        table[0][i+1][1]=2

    for i in range(len(seq_2)):
        table[i+1][0][0]=table[i][0][0]+gap_penalty
        table[i+1][0][1]=3
## initialize 1st row and 1st col
    for i in range(len(seq_2)):
        for j in range(len(seq_1)):
            table[i+1][j+1][0]=max(table[i][j][0]+int(check(seq_1[j],seq_2[i],list_s,score)),table[i+1][j][0]+gap_penalty,table[i][j+1][0]+gap_penalty)
            if(table[i+1][j+1][0]==table[i][j][0]+int(check(seq_1[j],seq_2[i],list_s,score))):
                table[i+1][j+1][1]=1
            elif(table[i+1][j+1][0]==table[i+1][j][0]+gap_penalty):
                table[i+1][j+1][1]=2
            elif(table[i+1][j+1][0]==table[i][j+1][0]+gap_penalty):
                table[i+1][j+1][1]=3
## fill the table
    x=len(seq_2)
    y=len(seq_1)
    while(1):
        if(x==0 and y==0):
            break
        if(table[x][y][1]==1):
            x=x-1
            y=y-1
            global_1+=seq_1[y]
            global_2+=seq_2[x]
        elif(table[x][y][1]==2):
            y=y-1
            global_1+=seq_1[y]
            global_2+='-'
        elif(table[x][y][1]==3):
            x=x-1
            global_2+=seq_2[x]
            global_1+='-'
    for i in range(len(global_1)):
        tmp+=global_1[len(global_1)-1-i]
    global_1=tmp
    tmp=''
    for i in range(len(global_2)):
        tmp+=global_2[len(global_2)-1-i]
    global_2=tmp
## trace from table[m][n]
## start local
    for i in range(len(seq_2)+1):
        table_l.append([])
        for j in range(len(seq_1)+1):
            table_l[i].append([0,0])
## initialize table_l
    for i in range(len(seq_2)):
        for j in range(len(seq_1)):
            table_l[i+1][j+1][0]=max(table_l[i][j][0]+int(check(seq_1[j],seq_2[i],list_s,score)),table_l[i+1][j][0]+gap_penalty,table_l[i][j+1][0]+gap_penalty,0)
            tmp=max(table_l[i][j][0]+int(check(seq_1[j],seq_2[i],list_s,score)),table_l[i+1][j][0]+gap_penalty,table_l[i][j+1][0]+gap_penalty,0)
            if(tmp==0):
                table_l[i+1][j+1][1]=0
            else:
                if(tmp==table_l[i][j][0]+int(check(seq_1[j],seq_2[i],list_s,score))):
                    table_l[i+1][j+1][1]=1
                elif(tmp==table_l[i+1][j][0]+gap_penalty):
                    table_l[i+1][j+1][1]=2
                elif(tmp==table_l[i][j+1][0]+gap_penalty):
                    table_l[i+1][j+1][1]=3
                
## fill the table_l
    for i in range(len(seq_2)+1):
        for j in range(len(seq_1)+1):
            if(local_p[0]<table_l[i][j][0]):
                local_p[0]=table_l[i][j][0]
                local_p[1]=i
                local_p[2]=j
## find maximum value
    x=local_p[1]
    y=local_p[2]
    while(table_l[x][y][1]!=0):
        if(table_l[x][y][1]==1):
            x=x-1
            y=y-1
            local_1+=seq_1[y]
            local_2+=seq_2[x]
        elif(table_l[x][y][1]==2):
            y=y-1
            local_1+=seq_1[y]
            local_2+='-'
        elif(table_l[x][y][1]==3):
            x=x-1
            local_2+=seq_2[x]
            local_1+='-'
    tmp=''
    for i in range(len(local_1)):
        tmp+=local_1[len(local_1)-1-i]
    local_1=tmp
    tmp=''
    for i in range(len(local_2)):
        tmp+=local_2[len(local_2)-1-i]
    local_2=tmp
    print(table[len(seq_2)][len(seq_1)][0])
    print(global_1)
    print(global_2)
    print(local_p[0])    
    print(local_1)
    print(local_2)
    
