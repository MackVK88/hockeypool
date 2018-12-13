from tkinter import *
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
            content = BeautifulSoup(site.content, 'html.parser')                    
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)

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
            
def updatelab():
   lstprint = ""
   for item in lst:
       lstprint = lstprint + item + "\n"
   mylab.configure(text=lstprint) 

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      entry.delete(0, END) 
      updatelab()        
            
def remItem():
   item = entry.get()
   if (len(lst) != 0):
      lst.remove(item)
      entry.delete(0, END) 
      updatelab()
      
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")

def makeList():
    if content != -99:
        names = content.findAll(attrs={"data-stat" : "player"})
        playerlist = []
        for player in names:
            if (player != "None"):
                playerlist.append(player.get('csk'))
            return playerlist

def createlistbox(value):  
    
    var=listbox.get(ANCHOR)
    print(var)
    if var!=type(NONE):
        print("a")
        if var!=None:
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
            listbox2=Listbox(root,bg='SpringGreen2')
            listbox2.grid(row=1,column=0,sticky=N,padx=0,pady=0)
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

lst = []
lstprint = ""
totalpts = 0

print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99

root = Tk()
root.geometry("300x400+0+900")
root.title("hockey pool")
root.configure(background="green")


instlab = Label(root,text="Input (e.g., McDavid,Connor): ")
instlab.pack() 

entry = Entry(root)     
entry.pack()

addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()

rembutton = Button(root, text="Remove", command=remItem)
rembutton.pack()

savebutton = Button(root, text="Save", command=saveList)
savebutton.pack()

mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
mylab.pack()

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.pack()

mypts = Label(root,text=totalpts)
mypts.pack()


root = Tk()
root.geometry("400x325+0+900")
root.configure(background="blue")
root.title("Final pool")

can = Canvas(root, width=400, height=225)
can.grid(row=0, column=0,padx=10, pady=10)
image1 = Image.open("cut.jpg")
photo = ImageTk.PhotoImage(image1)

can.create_oval(325, 25, 375, 75, fill="black", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill="#DDD", width=4)
can.create_text(350,50, text="pool", fill="silver")

# listbox
listbox = Listbox(root,height=7)
listbox.grid(row=1,column=0, sticky=NW, padx=10)
listbox.insert(END, "Patrick Kane", "Jonathan Toews", "Mitch Marner")

OPTIONS = ["Patrick Kane","McDavid,Connor"]
variable = StringVar(root)
variable.set(OPTIONS[0]) # default value)
w = OptionMenu(root, variable, *OPTIONS)
w.grid(row=1, column=0, sticky=E, padx=10)

savebutton = Button(root, text="Save")
savebutton.grid(row=1,column=0, sticky=E, padx=10)



mainloop()
mainloop()