from tkinter import *
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

lst = []
assists = []
goals = []
points = []
lstprint = ""
totalpts = 0
players = []
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

root = Tk()
root.geometry("800x600+0+900")
root.configure(background="blue")
root.title("Hockey pool")

if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99

def addPlayerToList(evt):
    global players
    name = variable.get()
    if players.count(name) > 0:
        return
    listbox.insert(END, name)
    for i in range(listbox.size()):
        players.append(listbox.get(i))

def createlistbox(value):
    var=listbox.get(ANCHOR)
    if var!=NONE:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        #player=str(parent.contents[1].text)
        team=str(parent.contents[3].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        points=int(parent.contents[8].text) 
        gamesplayed=int(parent.contents[5].text)
    listbox2 = Listbox(root, height=9)
    listbox2.place(x=200, y=405)
    listbox2.insert(END, 'Players Stats: ')
    listbox2.insert(END, 'Points: ' + str(points))
    listbox2.insert(END, 'Team: ' + team)
    listbox2.insert(END, 'Goals: ' + str(goals))
    listbox2.insert(END, 'Assists: ' + str(assists))
    listbox2.insert(END, 'Games Played: ' + str(gamesplayed))

def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayer.txt", "Players saved to disk")
  
def selected(evt):
    global player
    playerLabel.place(x=200, y=405)
    teamLabel.place(x=200, y=430)
    pointsLabel.place(x=200, y=455)
    goalsLabel.place(x=200, y=480)
    assistsLabel.place(x=200, y=505)

def switchPhoto(value):
    fullname = listbox.get(ACTIVE)
    full_list = fullname.split(",")
    first = full_list[1]
    last = full_list[0]
    filename = "headshots/" + last[0:5] + first[0:2] + "01.jpg"
    global photo2
    my_image = Image.open(filename.lower())
    photo2 = ImageTk.PhotoImage(my_image)
    can2.itemconfig(myimg2, image=photo2)

#listbox
listbox = Listbox(root,height=10)
listbox.grid(row=1,column =0, sticky=NW, padx=10, pady=10)
#listbox.bind('<<ListboxSelect>>', switchPhoto)
listbox.bind('<<ListboxSelect>>', createlistbox)

listbox = Listbox(root, width=23, height=20)
listbox.grid(row=1, column=0, sticky=NW, padx=10)
listbox.bind('<<ListboxSelect>>', switchPhoto)

def makeOptions():
    if content != -99:
        names = content.findAll(attrs={"data-stat" : "player"})
        playerlist = []
        for player in names:
            if(player != "None"):
                playerlist.append(player.get('csk'))
        return playerlist

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
        content = BeautifulSoup(site.content, 'html.parser')
    else:
        content = -99         
        totalpts = 0
    for myplayer in lst: # loop to check my players
        dTag = content.find(attrs={"csk": myplayer})
        parent = dTag.findParent('tr')
        playerpts = int(parent.contents[8].text) # 8th tag is total points
        print(myplayer + " " + str(playerpts))
        totalpts = totalpts + playerpts         
        mypts.configure(text=totalpts)

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

def addValue(value):
    if (lst.count(value) == 0):
        lst.append(value)
        listbox.insert(END, value)

def remValue(value):
    player = listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(player)

def switchPhoto():
    global photo
    my_image = Image.open("headshots/kesseph01.jpg")
    photo = ImageTk.PhotoImage(my_image)
    can.itemconfig(myimg,image=photo)


# GUI
root = Tk()
root.geometry
root.title("hockey pool")

button = Button(root, text="Change photo", command=switchPhoto)
button.pack()

players = []

for code in players:
    if (code != ""):
        url = "https://d9kjk42l7bfqz.cloudfront.net" + code + "" 
        print(url)
        response = requests.get(url, stream=True)
        with open(code + '.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

            
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
root.configure(background="white")

instlab = Label(root,text="Input (e.g., McDavid,Connor): ")
instlab.grid() 

entry = Entry(root)     
entry.grid()

addbutton = Button(root, text="Add", command=addItem)
addbutton.grid()

rembutton = Button(root, text="Remove", command=remItem)
rembutton.grid()

savebutton = Button(root, text="Save", command=saveList)
savebutton.grid()

mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
mylab.grid()

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.grid()

mypts = Label(root,text=totalpts)
mypts.grid()

mainloop()