import matplotlib.pyplot as p

list1=["drawing","music","dance","games"]
nos=[130,150,180,75]
c=["pink","green","blue","gold"]
explid=(0.1,0,0,0)
p.figure(figsize=[8,5])
p.title("hobbies")
p.pie(nos,explode=explid,labels=list1,colors=c,shadow=True,startangle=170)

p.show()
