class Airport:
        location=""
        arrival={}
        def set_arrival(self,arrival):
                self.arrival=arrival
        def set_location(self,location):
                self.location=location
def set_up():
        N=int(raw_input())
        airports={}
        for i in range(N):
                c=Airport()
                b=raw_input()
                a=b.split()
                M=int(a[1])
                c.set_location(a[0])
                d=raw_input().split()
                e={}
                c.set_arrival(e)
                for i in range(M):
                        e[d[i*2]]=int(d[i*2+1])
                c.set_arrival(e)
                airports[c.location]=c.arrival
        return airports

######################################
## pa2.1 function       
def get_min(dist):
        for i in dist:
                tmp=dist[i]
                tmp_i=i
                break
        for i in dist:
                if tmp>dist[i]:
                        tmp=dist[i]
                        tmp_i=i
        return tmp_i

def dijkstra(graph,source,target):
        dist={}
        previous={}
        Q={}
        dist[source]=0
        for i in graph:
                if i!=source:
                        dist[i]=float("inf")    
                        previous[i]=0
                Q[i]=dist[i]
        while(len(Q)!=0):
                u=get_min(Q)
                del Q[get_min(Q)]
                

                for i in graph[u]:
                        alt=dist[u]+graph[u][i]
                        if i in dist:
                                if alt<dist[i]:
                                        del dist[i]
                                        dist[i]=alt
                                        del previous[i]
                                        previous[i]=u
                        else:
                                dist[i]=float("inf")
                                previous[i]=0
                                if alt<dist[i]:
                                        del dist[i]
                                        dist[i]=alt
                                        del previous[i]
                                        previous[i]=u
        if(dist[target]!=float("inf")):
                route=[]
                route.append(target)
                tmp=target
                while(tmp!=source):
                        route.append(previous[tmp])
                        tmp=previous[tmp]
        else:
                route=[]
        return [dist,route]
                                
def get_src_N_dest():
        a=raw_input("Src:")
        b=raw_input("Dst:")
        return [a,b]

def make_answer_string(a,b):
        
        if a[0][b]!=float("inf"):
                answer="Routes: "
                for i in range(len(a[1])):
                        if i!=len(a[1])-1:
                                answer+=str(a[1][-i-1])+"->"
                        else:
                                answer+=str(a[1][-i-1])
                answer+="\nFlight time: "+str(a[0][b])
        else:
                answer="No air route"
        return answer
##############################################
##   pa2.2 function

def initial_table(graph):
        a={}
        for i in graph:
                a[i]=[0,0]
        return a
        
def DFS_V(graph,v,table, time, course,S):
        del table[v]
        table[v]=[time[0]+1,0]
        time[0]+=1
        course.append(v)
        if v in graph:
                for i in graph[v]:
                        if table[i][0]==0:
                                DFS_V(graph,i,table,time,course,S)
                tmp=table[v][0]
                del table[v]
                table[v]=[tmp,time[0]+1]
                time[0]+=1
                S.append(v)
        else:
                tmp=table[v][0]
                del table[v]
                table[v]=[tmp,time[0]+1]
                time[0]+=1
                S.append(v)
        
def make_transpose(graph):
        graph_1={}
        for i in graph:
                for j in graph[i]:
                        if j not in graph_1:
                                tmp={}
                                tmp[i]=graph[i][j]
                                graph_1[j]=tmp
                        else:
                                tmp=graph_1[j]
                                tmp[i]=graph[i][j]
                                del graph_1[j]
                                graph_1[j]=tmp
                                
        return graph_1


def make_one(graph,l):
        graph_2={}      
        for i in l:
                if len(i)>1:
                        c=Airport()
                        for start in i:
                                if start in graph:
                                        c.set_location(start)
                                        break
                        tmp={}
                        for j in i:
                                for k in graph[j]:
                                        if k not in i:
                                                tmp[k]=graph[j][k]
                                        
                                                
                        c.set_arrival(tmp)
                        graph_2[c.location]=c.arrival
                else:
                        if i[0] in graph:
                                c=Airport()
                                tmp={}
                                c.set_location(i[0])
                                for j in graph[i[0]]:
                                        tmp[j]=graph[i[0]][j]
                                c.set_arrival(tmp)
                                graph_2[c.location]=c.arrival
                        else:
                                graph_2[i[0]]=""
        return graph_2
def floyd(table,graph):
        v={}
        for i in table:
                v[i]=dijkstra(graph,i,i)[0]
        return v
                                
                        

def check_graph(graph,table):
#       no_out=[0,[]]
#       no_in=[0,[]]
#       for i in graph:
#               check=0
#               if len(graph[i])==0:
#                       no_out[0]+=1
#                       no_out[1].append(i)
#               for j in graph:
#                       if i in graph[j]:
#                               check+=1
#               if check==0:
#                       no_in[0]+=1
#                       no_in[1].append(i)
#       return [no_in,no_out]
        no_in={}
        no_out={}
        x=0
        y=0
        for i in table:
                no_in[i]=""
                x+=1
        for i in graph:
                no_out[i]=""
                y+=1
        for i in graph:
                if len(graph[i])!=0:
                        del no_out[i]
                        y=y-1
                for j in graph[i]:
                        if j in no_in:
                                del no_in[j]
                                x=x-1
        answer=[[x,no_in],[y,no_out]]
        
        return answer


if __name__=="__main__":
        graph=set_up()
        mission=get_src_N_dest()
##      print graph
        answer_1=dijkstra(graph,mission[0],mission[1])
        print"Answer"
        print make_answer_string(answer_1,mission[1])
        time=[0]
        time_1=[0]
        table=initial_table(answer_1[0])
        table_1=initial_table(answer_1[0])
        graph_1=make_transpose(graph)
        S=[]
        course_n=[]
##      print graph_1
        while len(S)!=len(table):
                for i in table:
                        if i not in S:
                                tmp=i
                                break
                DFS_V(graph,tmp,table,time,course_n,S)
        l=[]
##      print S
        A=[]
        while len(S)!=0:
                course=[]
                v=S.pop()
                DFS_V(graph_1,v,table_1,time_1,course,A)
                l.append(course)
                for i in course:
                        if i in graph_1:
                                del graph_1[i]
                                if i in S:
                                        S.remove(i)

        graph_2=make_one(graph,l)
        table_1=initial_table(graph_2)
        answer=check_graph(graph_2,table_1)
                
        max_out_in=max(answer[0][0],answer[1][0])
        print"#new air routes: "+str(max_out_in)
        reachable=floyd(answer_1[0],graph_2)
        x=1
        if max_out_in==answer[1][0]:
                for i in answer[1][1]:
                        check=0
                        deletion=""
                        if x<=answer[0][0]:
                                print"Route"+str(x)
                                for j in answer[0][1]:
                                        if reachable[j][i]==float("inf"):
                                                print"Src: "+i+" Dst: "+j
                                                Dst=j
                                                deletion=j
                                                check=1
                                                break
                                if check==0:
                                        for j in answer[0][1]:
                                                print"Src :"+i+" Dst: "+j
                                                Dst=j
                                                deletion=j
                                                break
                                del answer[0][1][deletion]
                                x+=1
                                                
                        else:
                                print"Route"+str(x)
                                print"Src: "+i+" Dst: "+Dst
                                x+=1
        else:
                for i in answer[1][1]:
                        check=0
                        deletion=""
                        print"Route"+str(x)
                        for j in answer[0][1]:
                                if reachable[j][i]==float("inf"):
                                        print"Src: "+i+" Dst: "+j
                                        Src=i
                                        deletion=j
                                        check=1
                                        break
                        if check==0:
                                for j in answer[0][1]:
                                        print"Src :"+i+" Dst: "+j
                                        Src=i
                                        deletion=j
                                        break
                        del answer[0][1][deletion]
                        x+=1
                for j in answer[0][1]:
                        print"Route"+str(x)
                        print"Src: "+Src+" Dst: "+j
                        

