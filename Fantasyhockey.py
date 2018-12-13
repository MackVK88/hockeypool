from tkinter import *
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image


root = Tk()
root.geometry("600x325+0+900")
root.configure(background="black")
root.title("Final pool")


can = Canvas(root, width=400, height=250)
can.grid(row=0, column=0, sticky=NW, pady=10)
image = Image.open("black-and-white-hockey-badge.png")
photo1 = ImageTk.PhotoImage(image)
can.create_image(0,0, anchor=NW, image=photo1)

can.create_oval(325, 25, 375, 75, fill="black", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 40, 320, 40, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill="#DDD", width=4)
can.create_text(350,50, text="pool", fill="orange")

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
               
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)

def createlistbox(value):  
    
    var= variable.get()
    print(variable)
    if var != None:
            dTag=content.find(attrs={"csk":var})
            parent=dTag.findParent("tr")
            points=int(parent.contents[8].text)
            goals=int(parent.contents[6].text)
            assists=int(parent.contents[7].text)
            games=int(parent.contents[5].text)
            minutes=int(parent.contents[21].text)
            team=parent.contents[3].text
            position=parent.contents[4].text
            age=int(parent.contents[2].text)
            average=float(parent.contents[20].text)
            plusminus=int(parent.contents[9].text)
            listbox2.insert(END, "Age: "+ str(age))
            listbox2.insert(END,"Points: " + str(points))
            listbox2.insert(END,"Goals: " + str(goals))
            listbox2.insert(END,"Assists: "+str(assists))
            listbox2.insert(END,"+/-: "+str(plusminus))
            listbox2.insert(END,"Shooting %: "+str(average))
            listbox2.insert(END,"Games Played: "+str(games))
            listbox2.insert(END,"Minutes Played: "+str(minutes))
            listbox2.insert(END,"Team: "+str(team))
            listbox2.insert(END,"Position: "+str(position))
            

def readfile():
    f=open("myplayers.txt","r")
    cont=f.read().split("---")
    for a in cont:
        if cont!=0:
            listbox.insert(END,a)
            lst.append(a)
    f.close()
          
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers/txt", "players saved to disk")

def saveasList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    root.filename=filedialog.asksaveasfilename(initialdir="/", title="Select file")
    print(root.filename)
    messagebox.showinfo("myplayers/txt", "players saved to disk")

def switchPhoto():
    fullname = listbox.get(ACTIVE)
    full_list = fullname.split(",")
    first = full_list[1]
    last = full_list[0]
    filename = "headshots/" + last[0:5] + first[0:2] + "01.jpg"
    global photo
    my_image = Image.open(filename.lower())
    photo = ImageTk.PhotoImage(my_image)
    can.itemconfig(myimg, image=photo)
    
def updatelab():
   lstprint = ""
   for item in lst:
       lstprint = lstprint + item + "\n"
   mylab.configure(text=lstprint) 

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      listbox.insert(END, item)
      entry.delete(0, END)     
            
def remItem():
   items = listbox.curselection()
   pos = 0
   for i in items :
       idx = int(i) - pos
       listbox.delete( idx,idx )
       lst.remove(idx)
       pos = pos + 1
    

def makeList():
    if content != -99:
        names = content.findAll(attrs={"data-stat" : "player"})
        playerlist = []
        for player in names:
            if (player != "None"):
                playerlist.append(player.get('csk'))
            return playerlist

def addPlayerToList(evt):
    players = []
    name = variable.get()
    if players.count(name) > 0:
        return
    listbox.insert(END, name)
    for i in range(listbox.size()):
        players.append(listbox.get(i))

def addplayers(value):
    var.get
    if lst.count(value)!=0:
        pass
    else:
        listbox.insert(END,value)
        lst.append(value)
        
def remplayers(value):
    var=listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(var)
    
listbox2 = Listbox(root,height=10)
listbox2.grid(row=1, column=1, sticky=N, padx=0)


goallist = []
assistlist = []
pointlist = []
playerlist= []
lst = []
totalpts = 0
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content=-99

def selected(evt):
    global player
    playerLabel.place(x=200, y=405)
    teamLabel.place(x=200, y=430)
    pointsLabel.place(x=200, y=455)
    goalsLabel.place(x=200, y=480)
    assistsLabel.place(x=200, y=505)


if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99

def makeOptions():
    if content != -99:
        names = content.findAll(attrs={"data-stat" : "player"})
        playerlist = []
        for player in names:
            if(player != "None"):
                playerlist.append(player.get('csk'))
        return playerlist


OPTIONS = makeOptions()
variable = StringVar(root)
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS, command=createlistbox)
w.grid(row=3, column=1, sticky=N, padx=10, pady=0)

can = Canvas(root, width=150, height=150)
image1 = Image.open("marnemi01.jpg")
photo = ImageTk.PhotoImage(image1)
myimg = can.create_image(0, 0, anchor=NW, image=photo)
can.grid(row=0,column=1, sticky=N, padx=10, pady=70)

listbox = Listbox(root,height=7)
listbox.grid(row=1,column=0, sticky=NW, padx=10, pady=20)

listbox.bind(createlistbox)


listbox.bind(remplayers)

rembutton = Button(root, text="Remove", command=remItem)
rembutton.grid(row=5, column=1, sticky=N, padx=0)

savebutton = Button(root, text="Save", command=saveList)
savebutton.grid(row=2,column=0, sticky=NW, padx=10)

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.grid(row=3,column=0, sticky=W, padx=10)

photobutton = Button(root, text="change photo", command=switchPhoto)
photobutton.grid(row=5,column=0, sticky=W, padx=10)





mainloop()
