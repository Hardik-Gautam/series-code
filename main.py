from win32api import GetLogicalDriveStrings,SetFileAttributes
from os import walk,path
import getpass
from tkinter import *
from mutagen.mp3 import MP3
import win32con
import eyed3
from tkinter import ttk
from random import randrange
from PIL import Image,ImageTk
from pygame import mixer
from tkinter import messagebox
from mutagen.mp3 import MP3
import datetime
import mp3play
from tkinter import filedialog
#$$$$$$$$$$$$This is flag variables$$$$$$$$$$$$$$$
flag = 0
recenttext = []
faviouritelist = []
rootmusicList = []
rootmusicAddress = []
rootimgAddress = []
frameIndecator = 0
selfname = []
musicChoice = ""
musicCount = 0
eixt = 1
ReapetFlag = 0
firsttime = 0
secondtime=0
previousframe = 0
shuffle=0
prograss_level = 0
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#5%%%%%%%%%%%%%%%For move the name
count=0
a=0
i=""
k=""
# %%%%%%%%%%%%%%%%%%

class MainControls:

    # Image maker working proparly
    @staticmethod
    def ImageMaker(arg,name):
        for i in arg:
            try:
                audio_file = eyed3.load(i)
                # title = audio_file.tag.title
                for j in name:
                    if i.find(j) != -1:
                        # lst = title.find("(")
                        # b = title[0:lst]
                        for image in audio_file.tag.images:
                            image_file = open("images\\{0}.png".format(j.replace(".mp3","")), 'wb')
                            image_file.write(image.image_data)
                            image_file.close()
                    # else:
                    #    for image in audio_file.tag.images:
                    # image_file = open("images\\{0}.png".format(title), 'wb')
                    # image_file.write(image.image_data)
                    #  image_file.close()
            except FileNotFoundError as e:
                print("this is your exception ", e)
            except TypeError as e1:
                print("1 this is your exception ", e1)
            except UnicodeError as o:
                print("this is your object exception ", o)
            except OSError as e:
                print(e)
            except AttributeError as a:
                print(a)
            except Exception as b:
                print(b)

    # For files hiding
    def directory_hide(self,file):
        for i in range(0, len(file)):
            SetFileAttributes(file[i], win32con.FILE_ATTRIBUTE_HIDDEN)

    # Get computer Drives
    def Drive_finder(self):
        drives = GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        dri = []
        for i in range(0, len(drives)):
            dri.append(drives[i].replace("\\", ""))
        return dri

    # Get all song names with their address
    def Song_address(self, drives):
        music_list = []
        Song_Name = []
        username = getpass.getuser()
        for i in range(0, len(drives)):
            if drives[i] != "C:":
                for root, dirs, files in walk(drives[i]):
                    for file in files:
                        audio_file = path.join(root, file)
                        if audio_file.endswith(".mp3") == True:
                            music_list.append(audio_file)
                            Song_Name.append(file)
                Song_Name.sort()
                dp = drives[i].replace(":", "")
                with open("song Addres and Names\\"+dp + " Address" + ".txt", "w") as f:
                    for address in music_list:
                        f.write(address + "\n")
                with open("song Addres and Names\\"+dp + " Song_NM" + ".txt", "w") as f:
                    for Name in Song_Name:
                        f.write(Name + "\n")
                music_list = []
                Song_Name = []

            # C Drive portition
            if drives[i] == "C:":
                for root, dirs, files in walk(drives[i]):
                    if root.find(username+"\\Downloads") != -1:
                        for file in files:
                            audio_file = path.join(root, file)
                            if audio_file.endswith(".mp3") == True:
                                music_list.append(audio_file)
                                Song_Name.append(file)
                Song_Name.sort()
                dp = drives[i].replace(":", "")
                with open("song Addres and Names\\"+dp + " Address" + ".txt", "w") as f:
                    for address in music_list:
                        f.write(address + "\n")
                with open("song Addres and Names\\"+dp + " Song_NM" + ".txt", "w") as f:
                    for Name in Song_Name:
                        f.write(Name + "\n")
                music_list=[]
                Song_Name=[]

        # return music_list, Song_Name
    # Get read all txt file and create in a list form
    def txt_to_list_maker(self):
        ADDRESS = []
        NAME = []
        images = []
        it = ""
        address = []
        item = ""
        name = []
        # for search file and folders
        for root, dirs, files in walk("song Addres and Names\\"):
            for file in files:
                audio_file = path.join(root, file)
                if audio_file.endswith(".txt") == True and audio_file.find("Address") != -1:
                    ADDRESS.append(audio_file)
                if audio_file.endswith(".txt") == True and audio_file.find("Song_NM") != -1:
                    NAME.append(audio_file)

        for r, d, f in walk("images\\"):
            for file in f:
                im = path.join(r, file)
                if im.endswith(".png") == True:
                    images.append(im)

        # for song names
        for i in range(0, len(NAME)):
            with open(NAME[i], "r") as f:
                data = f.read()
                for temp in data:
                    if temp != "\n":
                        item = item + temp
                    else:
                        name.append(item)
                        item = ""
        # for address
        for i in range(0, len(ADDRESS)):
            with open(ADDRESS[i], "r") as f:
                data = f.read()
                for temp in data:
                    if temp != "\n":
                        it = it + temp
                    else:
                        address.append(it)
                        it = ""
        return name,images ,address
    # *********************************************** List box start here *************************************************
    def deletefav(self):
        global faviouritelist
        new = []
        fault = self.listbox3.get(ACTIVE)
        for i in faviouritelist:
            if i != fault:
                new.append(i)
        faviouritelist = new
        with open("song Addres and Names\\favorites\\fav.txt","w") as f:
            for i in faviouritelist:
                f.write(i + "\n")
        self.listbox3.delete(0, END)
        self.faviourite()
    def do_pop(self,event):
        self.m.tk_popup(event.x_root, event.y_root)
        self.m.grab_release()
    def searchfunction(self):
        self.songList()
        self.listbox.delete(0, END)
        txt = self.searchtexts.get()
        for i in self.name:
            if i.find(txt) != -1:
                self.listbox.insert("end", i)
                self.listbox.insert("end", "\n")

    def faviourite(self):
        global faviouritelist,rootmusicList, rootmusicAddress
        it = ""
        faviouritelist = []
        with open("song Addres and Names\\favorites\\fav.txt", "r") as f:
            data = f.read()
            for temp in data:
                if temp != "\n":
                    it = it + temp
                else:
                    faviouritelist.append(it)
                    it = ""
        faviouritelist.sort()
        if len(faviouritelist) != 0:
            for i in faviouritelist:
                    self.listbox3.insert("end", i)
                    self.listbox3.insert("end","\n")
        else:
            self.listbox3.insert("end", "Import your Favorite Music......")
        rootmusicList.clear()
        rootmusicAddress.clear()
        rootimgAddress.clear()
        for i in faviouritelist:
            rootmusicList.append(i)
        for i in range(0, len(rootmusicList)):
            for j in range(0,len(self.address)):
                if self.address[j].find(rootmusicList[i]) != -1:
                    rootmusicAddress.append(self.address[j])

        for i in range(0,len(faviouritelist)):
            for j in range(0, len(self.imgs)):
                if self.imgs[j].find(faviouritelist[i]) != -1:
                    rootimgAddress.append(self.imgs[j])
        pass

    # this is master function start

    def realTimeScan(self):

        dir = self.Drive_finder()
        self.Song_address(dir)
        self.name, self.imgs, self.address = self.txt_to_list_maker()
        self.ImageMaker(self.address,self.name)
        self.root.destroy()
        GUI.__init__(self)

    # List checker that list is empty or not
    def Listchecker(self):
        if len(self.imgs) != 0:
            self.pk = Image.open(self.imgs[0])
            self.pk = self.pk.resize((100, 100), Image.ANTIALIAS)
            self.phot = ImageTk.PhotoImage(self.pk)
            self.pj = Image.open(self.imgs[0])
            self.pj = self.pj.resize((220, 200), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.pj)
            self.btn.config(image=self.phot)
            self.StatusLable3.config(image=self.photo)
        else:
            self.pk = Image.open("icon\\icons8-search-folder-96.png")
            self.pk = self.pk.resize((80, 80), Image.ANTIALIAS)
            self.phot = ImageTk.PhotoImage(self.pk)
            self.btn.config(image=self.phot)
            self.pj = Image.open("icon\\icons8-search-folder-96.png")
            self.pj = self.pj.resize((110, 110), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.pj)
            self.StatusLable3.config(image=self.photo)
        if len(self.name) == 0:
            self.listbox.insert("end", "Required Directory is missing ?............Import Directory")

    # master function end
    def Song_folder_select(self):
        music_list = []
        Song_Name = []
        folder = filedialog.askdirectory(initialdir="audio/", title="Insert New Song Directory")
        for root, dirs, files in walk(folder):
            for file in files:
                audio_file = path.join(root, file)
                if audio_file.endswith(".mp3") == True:
                    music_list.append(audio_file)
                    Song_Name.append(file)
        self.ImageMaker(music_list, Song_Name)
        with open("song Addres and Names\\" + "New" + " Address" + ".txt", "a") as f:
            for address in music_list:
                f.write(address + "\n")
        with open("song Addres and Names\\" + "New" + " Song_NM" + ".txt", "a") as f:
            for Name in Song_Name:
                f.write(Name + "\n")
        self.name, self.imgs, self.address = self.txt_to_list_maker()
        self.name.sort()
        for i in self.name:
            rootmusicList.append(i)  # I'm having to write in such a way because self.name is getting empty there
        for i in self.address:
            rootmusicAddress.append(i)
        # print(rootmusicAddress)
        for i in self.imgs:
            rootimgAddress.append(i)
        self.listbox.delete(0, "end")
        for i in self.name:
            self.listbox.insert("end", i)
            self.listbox.insert("end", "\n")


    def singal_song_select(self):
        music_list = []
        Song_Name = []
        fld = filedialog.askopenfilename(initialdir='audio/')
        a = path.splitext(path.basename(fld))
        if fld.endswith(".mp3") == True:
            music_list.append(fld)
            print(music_list)
            Song_Name.append(a[0] + a[1])
            self.ImageMaker(music_list, Song_Name)
            with open("song Addres and Names\\" + "New" + " Address" + ".txt", "a") as f:
                for address in music_list:
                    f.write(address + "\n")
            with open("song Addres and Names\\" + "New" + " Song_NM" + ".txt", "a") as f:
                for Name in Song_Name:
                    f.write(Name + "\n")
            self.name, self.imgs, self.address = self.txt_to_list_maker()
            self.name.sort()
            for i in self.name:
                rootmusicList.append(i)  # I'm having to write in such a way because self.name is getting empty there
            for i in self.address:
                rootmusicAddress.append(i)
            # print(rootmusicAddress)
            for i in self.imgs:
                rootimgAddress.append(i)
            self.listbox.delete(0,"end")
            for i in self.name:
                self.listbox.insert("end", i)
                self.listbox.insert("end", "\n")

        else:
            messagebox.showerror("Warring", "File is not Mp3")

class colorCombo:
    def pink1(self):
        self.pink()
        pass
    def seegreen1(self):
        self.seegreen()
        pass
    def lightgreen1(self):
        self.lightgreen()
        pass
    def parple1(self):
        self.parple()
        pass
    def gray1(self):
        self.gray()
        pass
    def pink(self):
        self.searchBarColor = "#2ECC71"
        self.threerow = "#EC407A"
        self.threerowslable = "#2ECC71"
        self.colorlight = "#C2185B"
        self.color = "#E91E63"
        self.fontcolor = "white"
        self.listcolor = "#AD1457"
        try:
            self.frame1.config(bg=self.threerow)
            self.frame1mini.config(bg=self.threerow)
            self.listbox.config(bg=self.listcolor)
        except Exception:pass

        self.frameupper.config(bg=self.colorlight)
        self.searchBar.config(bg=self.searchBarColor)
        self.search.config(bg=self.color)
        try:
            self.frame2.config(bg=self.threerow)
            self.frame2mini.config(bg=self.threerow)
            self.listbox1.config(bg=self.listcolor)
        except Exception:pass
        try:
            self.frame3.config(bg=self.threerow)
            self.frame3mini.config(bg=self.threerow)
            self.listbox3.config(bg=self.listcolor)
        except Exception:
            pass

        self.frame22.config(bg=self.colorlight)
        self.frame2Left.config(bg=self.colorlight)
        self.scan.config(bg=self.colorlight,activebackground=self.colorlight)
        self.searchBarLable.config(bg=self.colorlight)
        self.btn1.config(bg=self.threerow,activebackground=self.threerow)
        self.btn2.config(bg=self.threerow,activebackground=self.threerow)
        self.btn3.config(bg=self.threerow,activebackground=self.threerow)
        self.btn4.config(bg=self.threerow,activebackground=self.threerow)
        self.label.config(bg=self.colorlight)
        self.btn.config(bg=self.threerow)
        self.btn1lable.config(bg=self.colorlight)
        self.btn2lable.config(bg=self.colorlight)
        self.btn3lable.config(bg=self.colorlight)
        self.btn4lable.config(bg=self.colorlight)
        self.ringtone.config(bg=self.colorlight,activebackground=self.colorlight)
        self.settings.config(bg=self.colorlight,activebackground=self.colorlight)
        self.folder.config(bg=self.colorlight,activebackground=self.colorlight)
        self.share.config(bg=self.colorlight,activebackground=self.colorlight)
        self.TitleAhead.config(bg=self.colorlight)
        self.StatusLable3.config(bg=self.colorlight)
        self.ArtistAhead.config(bg=self.colorlight)
        self.AlbumAhead.config(bg=self.colorlight)
        self.StatusLable1.config(bg=self.colorlight)
        self.just.config(bg=self.colorlight)
        self.play.config(bg=self.color,activebackground=self.color)
        self.forward.config(bg=self.color,activebackground=self.color)
        self.backward.config(bg=self.color,activebackground=self.color)
        self.shuffle.config(bg=self.color,activebackground=self.color)
        self.repeat.config(bg=self.color,activebackground=self.color)
        self.heart.config(bg=self.color,activebackground=self.color)
        self.sound.config(bg=self.color,activebackground=self.color)
        self.exit.config(bg=self.color, activebackground=self.color)
        self.startcount.config(bg=self.color)
        self.endcount.config(bg=self.color)
        self.lowerstatus.config(bg=self.threerow)
        self.Bottombar.config(bg=self.color)
        self.volume_scale.config(troughcolor=self.threerow, background=self.color)
        self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor, troughcolor=self.threerow,
                         troughrelief='flat',
                         border="0")
        #del self.pink

        pass

    def seegreen(self):
        self.searchBarColor = "#2ECC71"
        self.threerow = "#00897B"
        self.threerowslable = "#2ECC71"
        self.colorlight = "#00695C"
        self.color = "#26A69A"
        self.fontcolor = "white"
        self.listcolor = "#004D40"
        try:
            self.frame1.config(bg=self.threerow)
            self.frame1mini.config(bg=self.threerow)
            self.listbox.config(bg=self.listcolor)
        except Exception :pass
        self.frameupper.config(bg=self.colorlight)
        self.searchBar.config(bg=self.searchBarColor)
        self.search.config(bg=self.color)
        try:
            self.frame2.config(bg=self.threerow)
            self.frame2mini.config(bg=self.threerow)
            self.listbox1.config(bg=self.listcolor)
        except Exception:pass
        try:
            self.frame3.config(bg=self.threerow)
            self.frame3mini.config(bg=self.threerow)
            self.listbox3.config(bg=self.listcolor)
        except Exception:
            pass

        self.frame22.config(bg=self.colorlight)
        self.frame2Left.config(bg=self.colorlight)
        self.scan.config(bg=self.colorlight,activebackground=self.colorlight)
        self.searchBarLable.config(bg=self.colorlight)
        self.btn1.config(bg=self.threerow,activebackground=self.threerow)
        self.btn2.config(bg=self.threerow,activebackground=self.threerow)
        self.btn3.config(bg=self.threerow,activebackground=self.threerow)
        self.btn4.config(bg=self.threerow,activebackground=self.threerow)
        self.label.config(bg=self.colorlight)
        self.btn.config(bg=self.threerow)
        self.btn1lable.config(bg=self.colorlight)
        self.btn2lable.config(bg=self.colorlight)
        self.btn3lable.config(bg=self.colorlight)
        self.btn4lable.config(bg=self.colorlight)
        self.ringtone.config(bg=self.colorlight,activebackground=self.colorlight)
        self.settings.config(bg=self.colorlight,activebackground=self.colorlight)
        self.folder.config(bg=self.colorlight,activebackground=self.colorlight)
        self.share.config(bg=self.colorlight,activebackground=self.colorlight)
        self.TitleAhead.config(bg=self.colorlight)
        self.StatusLable3.config(bg=self.colorlight)
        self.ArtistAhead.config(bg=self.colorlight)
        self.AlbumAhead.config(bg=self.colorlight)
        self.StatusLable1.config(bg=self.colorlight)
        self.just.config(bg=self.colorlight)
        self.play.config(bg=self.color,activebackground=self.color)
        self.forward.config(bg=self.color,activebackground=self.color)
        self.backward.config(bg=self.color,activebackground=self.color)
        self.shuffle.config(bg=self.color,activebackground=self.color)
        self.repeat.config(bg=self.color,activebackground=self.color)
        self.heart.config(bg=self.color,activebackground=self.color)
        self.sound.config(bg=self.color,activebackground=self.color)
        self.exit.config(bg=self.color, activebackground=self.color)
        self.startcount.config(bg=self.color)
        self.endcount.config(bg=self.color)
        self.lowerstatus.config(bg=self.threerow)
        self.Bottombar.config(bg=self.color)
        self.volume_scale.config(troughcolor=self.threerow, background=self.color)
        self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor, troughcolor=self.threerow,
                         troughrelief='flat',
                         border="0")
        #del self.seegreen
        pass
    def lightgreen(self):

        self.searchBarColor = "#2ECC71"
        self.threerow = "#00ACC1"
        self.threerowslable = "#2ECC71"
        self.colorlight = "#00838F"
        self.color = "#00BCD4"
        self.fontcolor = "white"
        self.listcolor = "#006064"
        try:
            self.frame1.config(bg=self.threerow)
            self.frame1mini.config(bg=self.threerow)
            self.listbox.config(bg=self.listcolor)
        except Exception:pass
        self.frameupper.config(bg=self.colorlight)
        self.searchBar.config(bg=self.searchBarColor)
        self.search.config(bg=self.color)
        try:
            self.frame2.config(bg=self.threerow)
            self.frame2mini.config(bg=self.threerow)
            self.listbox1.config(bg=self.listcolor)
        except Exception:
            pass
        try:
            self.frame3.config(bg=self.threerow)
            self.frame3mini.config(bg=self.threerow)
            self.listbox3.config(bg=self.listcolor)
        except Exception:
            pass

        self.frame22.config(bg=self.colorlight)
        self.frame2Left.config(bg=self.colorlight)
        self.scan.config(bg=self.colorlight, activebackground=self.colorlight)
        self.searchBarLable.config(bg=self.colorlight)
        self.btn1.config(bg=self.threerow, activebackground=self.threerow)
        self.btn2.config(bg=self.threerow, activebackground=self.threerow)
        self.btn3.config(bg=self.threerow, activebackground=self.threerow)
        self.btn4.config(bg=self.threerow, activebackground=self.threerow)
        self.label.config(bg=self.colorlight)
        self.btn.config(bg=self.threerow)
        self.btn1lable.config(bg=self.colorlight)
        self.btn2lable.config(bg=self.colorlight)
        self.btn3lable.config(bg=self.colorlight)
        self.btn4lable.config(bg=self.colorlight)
        self.ringtone.config(bg=self.colorlight, activebackground=self.colorlight)
        self.settings.config(bg=self.colorlight, activebackground=self.colorlight)
        self.folder.config(bg=self.colorlight, activebackground=self.colorlight)
        self.share.config(bg=self.colorlight, activebackground=self.colorlight)
        self.TitleAhead.config(bg=self.colorlight)
        self.StatusLable3.config(bg=self.colorlight)
        self.ArtistAhead.config(bg=self.colorlight)
        self.AlbumAhead.config(bg=self.colorlight)
        self.StatusLable1.config(bg=self.colorlight)
        self.just.config(bg=self.colorlight)
        self.play.config(bg=self.color, activebackground=self.color)
        self.forward.config(bg=self.color, activebackground=self.color)
        self.backward.config(bg=self.color, activebackground=self.color)
        self.shuffle.config(bg=self.color, activebackground=self.color)
        self.repeat.config(bg=self.color, activebackground=self.color)
        self.heart.config(bg=self.color, activebackground=self.color)
        self.sound.config(bg=self.color, activebackground=self.color)
        self.exit.config(bg=self.color, activebackground=self.color)
        self.startcount.config(bg=self.color)
        self.endcount.config(bg=self.color)
        self.lowerstatus.config(bg=self.threerow)
        self.Bottombar.config(bg=self.color)
        self.volume_scale.config(troughcolor=self.threerow, background=self.color)
        self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor, troughcolor=self.threerow,
                         troughrelief='flat',
                         border="0")
        #del self.lightgreen
        pass
    def parple(self):

        self.searchBarColor = "#2ECC71"
        self.threerow = "#AB47BC"
        self.threerowslable = "#2ECC71"
        self.colorlight = "#7B1FA2"
        self.color = "#8E24AA"
        self.fontcolor = "white"
        self.listcolor = "#4A148C"
        try:
            self.frame1.config(bg=self.threerow)
            self.frame1mini.config(bg=self.threerow)
            self.listbox.config(bg=self.listcolor)
        except Exception:pass
        self.frameupper.config(bg=self.colorlight)
        self.searchBar.config(bg=self.searchBarColor)
        self.search.config(bg=self.color)
        try:
            self.frame2.config(bg=self.threerow)
            self.frame2mini.config(bg=self.threerow)
            self.listbox1.config(bg=self.listcolor)
        except Exception:
            pass
        try:
            self.frame3.config(bg=self.threerow)
            self.frame3mini.config(bg=self.threerow)
            self.listbox3.config(bg=self.listcolor)
        except Exception:
            pass

        self.frame22.config(bg=self.colorlight)
        self.frame2Left.config(bg=self.colorlight)
        self.scan.config(bg=self.colorlight, activebackground=self.colorlight)
        self.searchBarLable.config(bg=self.colorlight)
        self.btn1.config(bg=self.threerow, activebackground=self.threerow)
        self.btn2.config(bg=self.threerow, activebackground=self.threerow)
        self.btn3.config(bg=self.threerow, activebackground=self.threerow)
        self.btn4.config(bg=self.threerow, activebackground=self.threerow)
        self.label.config(bg=self.colorlight)
        self.btn.config(bg=self.threerow)
        self.btn1lable.config(bg=self.colorlight)
        self.btn2lable.config(bg=self.colorlight)
        self.btn3lable.config(bg=self.colorlight)
        self.btn4lable.config(bg=self.colorlight)
        self.ringtone.config(bg=self.colorlight, activebackground=self.colorlight)
        self.settings.config(bg=self.colorlight, activebackground=self.colorlight)
        self.folder.config(bg=self.colorlight, activebackground=self.colorlight)
        self.share.config(bg=self.colorlight, activebackground=self.colorlight)
        self.TitleAhead.config(bg=self.colorlight)
        self.StatusLable3.config(bg=self.colorlight)
        self.ArtistAhead.config(bg=self.colorlight)
        self.AlbumAhead.config(bg=self.colorlight)
        self.StatusLable1.config(bg=self.colorlight)
        self.just.config(bg=self.colorlight)
        self.play.config(bg=self.color, activebackground=self.color)
        self.forward.config(bg=self.color, activebackground=self.color)
        self.backward.config(bg=self.color, activebackground=self.color)
        self.shuffle.config(bg=self.color, activebackground=self.color)
        self.repeat.config(bg=self.color, activebackground=self.color)
        self.heart.config(bg=self.color, activebackground=self.color)
        self.sound.config(bg=self.color, activebackground=self.color)
        self.exit.config(bg=self.color, activebackground=self.color)
        self.startcount.config(bg=self.color)
        self.endcount.config(bg=self.color)
        self.lowerstatus.config(bg=self.threerow)
        self.Bottombar.config(bg=self.color)
        self.volume_scale.config(troughcolor=self.threerow, background=self.color)
        self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor, troughcolor=self.threerow,
                         troughrelief='flat',
                         border="0")
        #del self.parple
        pass
    def gray(self):


        self.threerow = "#546E7A"
        self.threerowslable = "#37474F"
        self.colorlight = "#37474F"
        self.color = "#78909C"
        self.listcolor = "#263238"
        try:
            self.frame1.config(bg=self.threerow)
            self.frame1mini.config(bg=self.threerow)
            self.listbox.config(bg=self.listcolor)
        except Exception:pass
        self.frameupper.config(bg=self.colorlight)
        self.searchBar.config(bg=self.searchBarColor)
        self.search.config(bg=self.color)
        try:
            self.frame2.config(bg=self.threerow)
            self.frame2mini.config(bg=self.threerow)
            self.listbox1.config(bg=self.listcolor)
        except Exception:
            pass
        try:
            self.frame3.config(bg=self.threerow)
            self.frame3mini.config(bg=self.threerow)
            self.listbox3.config(bg=self.listcolor)
        except Exception:
            pass

        self.frame22.config(bg=self.colorlight)
        self.frame2Left.config(bg=self.colorlight)
        self.scan.config(bg=self.colorlight, activebackground=self.colorlight)
        self.searchBarLable.config(bg=self.colorlight)
        self.btn1.config(bg=self.threerow, activebackground=self.threerow)
        self.btn2.config(bg=self.threerow, activebackground=self.threerow)
        self.btn3.config(bg=self.threerow, activebackground=self.threerow)
        self.btn4.config(bg=self.threerow, activebackground=self.threerow)
        self.label.config(bg=self.colorlight)
        self.btn.config(bg=self.threerow)
        self.btn1lable.config(bg=self.colorlight)
        self.btn2lable.config(bg=self.colorlight)
        self.btn3lable.config(bg=self.colorlight)
        self.btn4lable.config(bg=self.colorlight)
        self.ringtone.config(bg=self.colorlight, activebackground=self.colorlight)
        self.settings.config(bg=self.colorlight, activebackground=self.colorlight)
        self.folder.config(bg=self.colorlight, activebackground=self.colorlight)
        self.share.config(bg=self.colorlight, activebackground=self.colorlight)
        self.TitleAhead.config(bg=self.colorlight)
        self.StatusLable3.config(bg=self.colorlight)
        self.ArtistAhead.config(bg=self.colorlight)
        self.AlbumAhead.config(bg=self.colorlight)
        self.StatusLable1.config(bg=self.colorlight)
        self.just.config(bg=self.colorlight)
        self.play.config(bg=self.color, activebackground=self.color)
        self.forward.config(bg=self.color, activebackground=self.color)
        self.backward.config(bg=self.color, activebackground=self.color)
        self.shuffle.config(bg=self.color, activebackground=self.color)
        self.repeat.config(bg=self.color, activebackground=self.color)
        self.heart.config(bg=self.color, activebackground=self.color)
        self.sound.config(bg=self.color, activebackground=self.color)
        self.exit.config(bg=self.color, activebackground=self.color)
        self.startcount.config(bg=self.color)
        self.endcount.config(bg=self.color)
        self.lowerstatus.config(bg=self.threerow)
        self.Bottombar.config(bg=self.color)
        self.volume_scale.config(troughcolor=self.threerow, background=self.color)
        self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor, troughcolor=self.threerow,
                         troughrelief='flat',
                         border="0")
        #del self.gray
        pass

class Buttons:

    # Main player Buttons start
    def Forward(self):
        global frameIndecator,firsttime,previousframe,rootmusicList,recenttext
        if firsttime != 0:
            if previousframe == 0 or previousframe == 1:
                try:
                    recenttext.append(self.musicChoice)
                    self.listbox.after_cancel(self.ForFone)
                    self.ForFrameOne()
                except Exception:
                    pass
            elif previousframe == 2:
                try:
                    self.listbox1.after_cancel(self.ForFtwo)
                    self.ForFrameTow()
                except Exception:
                    pass
            elif previousframe == 3:
                try:
                    self.root.after_cancel(self.ForFthree)
                    self.ForFrameThree()
                except Exception:
                    pass
            elif previousframe == 4:
                try:
                    recenttext.append(self.musicChoice)
                    self.listbox3.after_cancel(self.ForFfour)
                    self.ForFrameFour()
                except Exception:
                    pass
        firsttime += 1

    def Paush_Play(self):
        global flag
        if flag == 0:
            self.playImage = Image.open("icon\\pause.png")
            self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
            self.playImage1 = ImageTk.PhotoImage(self.playImage)
            self.play.config(image=self.playImage1)
            mixer.music.pause()
            flag = 1
            if previousframe == 0 or previousframe == 1:
                # print("off after 0 or 1")
                try:
                    self.listbox.after_cancel(self.ForFone)
                    print("after 1")
                except Exception:
                    pass
            elif previousframe == 2:
                # print("off after 2")
                try:
                    self.listbox1.after_cancel(self.ForFtwo)
                    print("after 2")
                except Exception:
                    pass
            elif previousframe == 3:
                # print("off after 3")
                try:
                    self.root.after_cancel(self.ForFthree)
                    print("after 3")
                except Exception:
                    pass
            elif previousframe == 4:
                # print("off after 4")
                try:
                    self.listbox3.after_cancel(self.ForFfour)
                    print("after 4")
                except Exception:
                    pass
        else:
            self.playImage = Image.open("icon\\play.png")
            #   self.playImage = Image.open("icon\\pause.png")
            self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
            self.playImage1 = ImageTk.PhotoImage(self.playImage)
            self.play.config(image=self.playImage1)
            mixer.music.unpause()
            flag = 0
    def activeHeart(self):
        global faviouritelist,frameIndecator
        if frameIndecator == 1:
            hearttxt = self.listbox.get(ACTIVE)
            if hearttxt != '\n':
                a = hearttxt + "\n"
                with open("song Addres and Names\\favorites\\fav.txt","a") as f:
                    f.write(a)
        elif frameIndecator == 2:
            hearttxt = self.listbox1.get(ACTIVE)
            if hearttxt != '\n':
                a = hearttxt + "\n"
                with open("song Addres and Names\\favorites\\fav.txt","a") as f:
                    f.write(a)
        elif frameIndecator == 3:
            hearttxt = self.listbox3.get(ACTIVE)
            if hearttxt != '\n':
                a = hearttxt + "\n"
                with open("song Addres and Names\\favorites\\fav.txt","a") as f:
                    f.write(a)

    def Backward(self):
        global frameIndecator, firsttime, previousframe, rootmusicList
        if firsttime != 0:
            if previousframe == 0 or previousframe == 1:
                # print("off after 0 or 1")
                try:
                    a = rootmusicList.index(self.musicChoice)
                    self.musicChoice = rootmusicList[a - 2]
                    recenttext.append(self.musicChoice)
                    self.listbox.after_cancel(self.ForFone)
                    self.ForFrameOne()
                except Exception:
                    pass
            elif previousframe == 2:
                # print("off after 2")
                try:
                    a = rootmusicList.index(self.musicChoice)
                    self.musicChoice = rootmusicList[a - 2]
                    self.listbox1.after_cancel(self.ForFtwo)
                    self.ForFrameTow()
                except Exception:
                    pass
            elif previousframe == 3:
                # print("off after 3")
                try:
                    a = rootmusicList.index(self.musicChoice)
                    self.musicChoice = rootmusicList[a - 2]
                    recenttext.append(self.musicChoice)
                    self.root.after_cancel(self.ForFthree)
                    self.ForFrameThree()
                except Exception:
                    pass
            elif previousframe == 4:
                # print("off after 4")
                try:
                    a = rootmusicList.index(self.musicChoice)
                    self.musicChoice = rootmusicList[a - 2]
                    recenttext.append(self.musicChoice)
                    self.listbox3.after_cancel(self.ForFfour)
                    self.ForFrameFour()
                except Exception:
                    pass
        firsttime += 1
    def reapte(self):
        global ReapetFlag
        ReapetFlag = 1

    def shuffleroot(self):
        global rootmusicAddress,rootmusicList
        try:
            for i in range(0, len(rootmusicAddress)):
                if rootmusicAddress[i].find(self.musicChoice) != -1:
                    self.imagechanger()
                    self.playsong(rootmusicAddress[i])
                    # this is temporly comment
                    audio = MP3(rootmusicAddress[i])
                    lent = audio.info.length
                    try:
                        aodi = eyed3.load(rootmusicAddress[i])
                        albm = aodi.tag.album
                        artst = aodi.tag.artist
                        # this is temporly comment
                    except Exception:
                        pass
                    self.lg = lent * 1000
                    self.tempsong = rootmusicList.index(self.musicChoice)
                    self.ArtistAhead.config(text=artst)
                    self.AlbumAhead.config(text=albm)
                    self.playImage = Image.open("icon\\play.png")
                    self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
                    self.playImage1 = ImageTk.PhotoImage(self.playImage)
                    self.play.config(image=self.playImage1)
                    self.songNamelength()
        except IndexError:
            pass
        if ReapetFlag == 1:
            exit(0)
        self.musicChoice = rootmusicList[randrange(0, len(rootmusicAddress))]
        self.shuffletake = self.listbox.after(int(self.lg), self.shuffleroot)
    def shuffle_recent(self):
        global rootmusicAddress, recenttext
        try:
            for i in range(0, len(rootmusicAddress)):
                if rootmusicAddress[i].find(self.musicChoice) != -1:
                    self.imagechanger()
                    self.playsong(rootmusicAddress[i])
                    # this is temporly comment
                    audio = MP3(rootmusicAddress[i])
                    lent = audio.info.length
                    try:
                        aodi = eyed3.load(rootmusicAddress[i])
                        albm = aodi.tag.album
                        artst = aodi.tag.artist
                        # this is temporly comment
                    except Exception:
                        pass
                    self.lg = lent * 1000
                    self.tempsong = recenttext.index(self.musicChoice)
                    self.ArtistAhead.config(text=artst)
                    self.AlbumAhead.config(text=albm)
                    self.playImage = Image.open("icon\\play.png")
                    self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
                    self.playImage1 = ImageTk.PhotoImage(self.playImage)
                    self.play.config(image=self.playImage1)
                    self.songNamelength()
        except IndexError:
            pass
        if ReapetFlag == 1:
            exit(0)
        self.musicChoice = rootmusicList[randrange(0, len(rootmusicAddress))]
        self.shuffletake1 = self.listbox1.after(int(self.lg), self.shuffle_recent)
    def shuffle_fav(self):
        global rootmusicAddress, faviouritelist
        try:
            for i in range(0, len(rootmusicAddress)):
                if rootmusicAddress[i].find(self.musicChoice) != -1:
                    self.imagechanger()
                    self.playsong(rootmusicAddress[i])
                    # this is temporly comment
                    audio = MP3(rootmusicAddress[i])
                    lent = audio.info.length
                    try:
                        aodi = eyed3.load(rootmusicAddress[i])
                        albm = aodi.tag.album
                        artst = aodi.tag.artist
                        # this is temporly comment
                    except Exception:
                       pass
                    self.lg = lent * 1000
                    self.tempsong = faviouritelist.index(self.musicChoice)
                    self.ArtistAhead.config(text=artst)
                    self.AlbumAhead.config(text=albm)
                    self.playImage = Image.open("icon\\play.png")
                    self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
                    self.playImage1 = ImageTk.PhotoImage(self.playImage)
                    self.play.config(image=self.playImage1)
                    self.songNamelength()
        except IndexError:
            pass
        if ReapetFlag == 1:
            exit(0)

        self.musicChoice = rootmusicList[randrange(0, len(rootmusicAddress))]
        self.shuffletake3 = self.listbox3.after(int(self.lg), self.shuffle_fav)
    def shuffle_selector(self):
        global previousframe,firsttime
        if firsttime >= 1:
            if previousframe == 0 or previousframe == 1:
                #print("off after 0 or 1")
                try:
                    self.listbox.after_cancel(self.ForFone)
                except Exception:
                    pass
            elif previousframe == 2:
                #print("off after 2")
                try:
                    self.listbox1.after_cancel(self.ForFtwo)
                except Exception:
                    pass
            elif previousframe == 3:
                #print("off after 3")
                try:
                    self.root.after_cancel(self.ForFthree)
                except Exception:
                    pass
            elif previousframe == 4:
                #print("off after 4")
                try:
                    self.listbox3.after_cancel(self.ForFfour)
                except Exception:
                    pass
        if previousframe == 0 or previousframe == 1:
            # print("off after 0 or 1")
            try:
                self.shuffleroot()
            except Exception:
                pass
        elif previousframe == 2:
            # print("off after 2")
            try:
                self.shuffle_recent()
            except Exception:
                pass
        elif previousframe == 3:
            # print("off after 3")
            try:
                self.shuffle_fav()
            except Exception:
                pass
    def shuffle_destory(self):
        if previousframe == 0 or previousframe == 1:
            # print("off after 0 or 1")
            try:
                self.listbox.after_cancel(self.shuffletake)
            except Exception:
                pass
        elif previousframe == 2:
            # print("off after 2")
            try:
                self.listbox1.after_cancel(self.shuffletake1)
            except Exception:
                pass
        elif previousframe == 3:
            # print("off after 3")
            try:
                self.listbox3.after_cancel(self.shuffletake3)
            except Exception:
                pass
    def shuffle_button(self):
        global shuffle
        if shuffle%2==0:
            self.shuffle_selector()
        else:
            self.shuffle_destory()
        shuffle += 1

class NameMoveClass:
    def spaceCreater(self):
        space = []
        for l in range(0, 2 * len(self.musicChoice)):
            space.append(" ")
        self.space = space
        self.names = self.musicChoice
    def moveSongName(self):
        global count, a, i, k
        if self.divider%2 == 0:
            if count < len(self.space):
                i = i + self.space[count]
                self.lowerstatus.config(text=i + self.names)
                #self.name.replace(i, "")
        elif self.divider%2 == 1:
            if count < len(self.space):
                k = k + self.space[count]
                self.lowerstatus.config(text=self.names + k)
                #self.name.replace(k, "")
        if count == len(self.space):
            count = 0
            k = ""
            i = ""
        self.divider += 1
        count += 1
        self.give = self.lowerstatus.after(900,self.moveSongName)


class events(NameMoveClass):

    def songNamelength(self):
        global firsttime
        if 25 < len(self.musicChoice):
            self.spaceCreater()
            if firsttime !=0:
                try:
                    self.lowerstatus.after_cancel(self.give)
                except Exception:
                    pass
            self.moveSongName()
        else:
            if firsttime !=0:
                try:
                    self.lowerstatus.after_cancel(self.give)
                except Exception:
                    pass
            self.lowerstatus.config(text=self.musicChoice)

    def playsong(self, arg):
        mixer.music.load(arg)
        mixer.music.play(0)

    def imagechanger(self):
        for i in range(0, len(rootimgAddress)):
            if rootimgAddress[i].find(self.musicChoice.replace(".mp3", "")) != -1:
                #print(self.musicChoice.replace(".mp3", ""))
                try:
                    self.pk = Image.open(rootimgAddress[i])
                    self.pk = self.pk.resize((100, 100), Image.ANTIALIAS)
                    self.phot = ImageTk.PhotoImage(self.pk)
                    self.pj = Image.open(rootimgAddress[i])
                    self.pj = self.pj.resize((220, 200), Image.ANTIALIAS)
                    self.photo = ImageTk.PhotoImage(self.pj)
                    self.btn.config(image=self.phot)
                    self.StatusLable3.config(image=self.photo)
                    self.lowerstatus.config(text=self.musicChoice.replace(".mp3", ""))
                    self.TitleAhead.config(text=self.musicChoice.replace(".mp3", ""))
                    break
                except Exception:
                    pass
        else:
            self.pk = Image.open("icon\\apple_music_android_logo_icon_134021.png")
            self.pk = self.pk.resize((80, 80), Image.ANTIALIAS)
            self.phot = ImageTk.PhotoImage(self.pk)
            self.btn.config(image=self.phot)
            self.pj = Image.open("icon\\apple_music_android_logo_icon_134021.png")
            self.pj = self.pj.resize((210, 210), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.pj)
            self.StatusLable3.config(image=self.photo)
            self.lowerstatus.config(text=self.musicChoice.replace(".mp3", ""))
            self.TitleAhead.config(text=self.musicChoice.replace(".mp3", ""))

    def ForFrameOne(self):
        global rootmusicList, rootmusicAddress, rootimgAddress, musicCount, eixt,firsttime
        try:
            for i in range(0, len(rootmusicAddress)):
                if rootmusicAddress[i].find(self.musicChoice) != -1:
                    self.imagechanger()
                    self.playsong(rootmusicAddress[i])
                    # this is temporly comment
                    audio = MP3(rootmusicAddress[i])
                    lent = audio.info.length
                    try:
                        aodi = eyed3.load(rootmusicAddress[i])
                        albm = aodi.tag.album
                        artst = aodi.tag.artist

                        # this is temporly comment
                    except Exception:
                        pass
                    self.lg = lent * 1000
                    self.startcount.config(text="{0}".format(str(datetime.timedelta(seconds=lent))[2:7]))
                    self.ArtistAhead.config(text=artst)
                    self.AlbumAhead.config(text=albm)
                    self.status_artst = artst
                    self.status_albm = albm
                    self.status_title = aodi.tag.title
                    self.playImage = Image.open("icon\\play.png")
                    self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
                    self.playImage1 = ImageTk.PhotoImage(self.playImage)
                    self.play.config(image=self.playImage1)
                    self.songNamelength()
                    if firsttime >= 1:
                        try:self.pb.after_cancel(self.av)
                        except Exception:pass
                    self.prograss()
        except IndexError:
            pass
        if ReapetFlag == 1:
            exit(0)

        try:
            self.tempsong = rootmusicList.index(self.musicChoice)
            self.musicChoice = rootmusicList[self.tempsong + 1]
        except Exception:
            pass
        self.ForFone = self.listbox.after(int(self.lg), self.ForFrameOne)

    def ForFrameTow(self):
        global rootmusicList, rootmusicAddress, rootimgAddress, musicCount, eixt,firsttime
        try:
            for i in range(0, len(rootmusicAddress)):
                if rootmusicAddress[i].find(self.musicChoice) != -1:
                    # self.imagechanger()
                    self.playsong(rootmusicAddress[i])
                    # this is temporly comment
                    audio = MP3(rootmusicAddress[i])
                    lent = audio.info.length
                    try:
                        aodi = eyed3.load(rootmusicAddress[i])
                        albm = aodi.tag.album
                        artst = aodi.tag.artist
                    except Exception:
                            pass
                    self.lg = lent * 1000
                    self.tempsong = rootmusicList.index(self.musicChoice)
                    self.ArtistAhead.config(text=artst)
                    self.AlbumAhead.config(text=albm)
                    self.status_artst = artst
                    self.status_albm = albm
                    self.status_title = aodi.tag.title
                    self.playImage = Image.open("icon\\play.png")
                    self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
                    self.playImage1 = ImageTk.PhotoImage(self.playImage)
                    self.play.config(image=self.playImage1)
                    self.imagechanger()
                    self.songNamelength()
                    if firsttime >= 1:
                        try:self.pb.after_cancel(self.av)
                        except Exception:pass
                    self.prograss()
        except IndexError:
            messagebox.showinfo("Index", "List has been Complete")
            return 0
        if ReapetFlag == 1:
            exit(0)
        try:
            self.musicChoice = rootmusicList[self.tempsong + 1]
        except IndexError:
            messagebox.showinfo("Index", "List has been Complete")
            return 0
        self.ForFtwo = self.listbox1.after(int(self.lg), self.ForFrameTow)

    def ForFrameThree(self):

        global rootmusicList, rootmusicAddress, rootimgAddress, musicCount, eixt
        print(rootmusicList)
        for i in range(0, len(rootmusicAddress)):
            if rootmusicAddress[i].find(self.musicChoice) != -1:
                # print(rootmusicAddress[i])
                mixer.music.load(rootmusicAddress[i])
                mixer.music.play(0)
                audio = MP3(rootmusicAddress[i])
                lent = audio.info.length
                l = lent * 1000
                tempsong = rootmusicList.index(self.musicChoice)
        self.musicChoice = rootmusicList[tempsong + 1]
        firsttime +=1
        self.ForFthree = self.root.after(int(lent), self.ForFrameThree)

    def ForFrameFour(self):
        global rootmusicList, rootmusicAddress, rootimgAddress, musicCount, eixt,firsttime
        try:
            for i in range(0, len(rootmusicAddress)):
                if rootmusicAddress[i].find(self.musicChoice) != -1:
                    self.imagechanger()
                    self.playsong(rootmusicAddress[i])
                    audio = MP3(rootmusicAddress[i])
                    lent = audio.info.length
                    try:
                        aodi = eyed3.load(rootmusicAddress[i])
                        albm = aodi.tag.album
                        artst = aodi.tag.artist
                    except Exception:pass
                    self.lg = lent * 1000
                    if firsttime >= 1:
                        try:self.pb.after_cancel(self.av)
                        except Exception:pass
                    self.prograss()
                    self.tempsong = rootmusicList.index(self.musicChoice)
                    self.ArtistAhead.config(text=artst)
                    self.AlbumAhead.config(text=albm)
                    self.status_artst = artst
                    self.status_albm = albm
                    self.status_tt_n = self.musicChoice
                    self.playImage = Image.open("icon\\play.png")
                    self.playImage = self.playImage.resize((35, 35), Image.ANTIALIAS)
                    self.playImage1 = ImageTk.PhotoImage(self.playImage)
                    self.play.config(image=self.playImage1)
                    self.songNamelength()

        except IndexError:self.listClick3.after_cancel(self.ForFtwo)
        if ReapetFlag == 1:
            exit(0)
        try:self.musicChoice = rootmusicList[self.tempsong + 1]
        except IndexError:pass
        firsttime += 1
        self.ForFfour = self.listbox3.after(int(self.lg), self.ForFrameFour)

    def prograss(self):
        currnetTime = mixer.music.get_pos() // 1000
        total_ms = mixer.music.get_pos()
        progress_percent = total_ms / float(self.lg) * 100
        self.startcount.config(text='{0}'.format(str(datetime.timedelta(seconds=self.lg//1000))[2:7]))
        self.endcount.config(text='{0}'.format(str(datetime.timedelta(seconds=currnetTime))[2:7]))
        # self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor,
        #                    troughcolor=self.threerow, troughrelief='flat', border="0")
        self.pb['value'] = progress_percent
        self.av = self.pb.after(5, self.prograss)

    def start(self):
        pass
    def listClick(self,event):

        global recenttext, frameIndecator,firsttime,previousframe,prograss_level
        previousframe = frameIndecator
        frameIndecator = 1
        prograss_level=0
        item = self.listbox.get(ACTIVE)
        if item != "\n":
            recenttext.append(item)
            self.musicChoice = item
            self.fav = item
            if firsttime >= 1:
                if previousframe == 0 or previousframe == 1:
                    # print("off after 0 or 1")
                    try:
                        self.listbox.after_cancel(self.ForFone)
                        self.pb.after_cancel(self.av)
                        print("yes")
                    except Exception:
                        pass
                elif previousframe == 2:
                    # print("off after 2")
                    try:
                        self.listbox1.after_cancel(self.ForFtwo)
                        self.pb.after_cancel(self.av)
                    except Exception:
                        pass
                elif previousframe == 3:
                    # print("off after 3")
                    try:
                        self.root.after_cancel(self.ForFthree)
                        self.pb.after_cancel(self.av)
                    except Exception:
                        pass
                elif previousframe == 4:
                    # print("off after 4")
                    try:
                        self.listbox3.after_cancel(self.ForFfour)
                        self.pb.after_cancel(self.av)
                    except Exception:
                        pass
            self.ForFrameOne()

            firsttime += 1
    def listClick1(self,event):
        global frameIndecator,previousframe,firsttime,secondtime
        previousframe = frameIndecator
        frameIndecator = 2
        item = self.listbox1.get(ACTIVE)
        if item != "\n":
            recenttext.append(item)
            self.fav = item
            self.musicChoice = item
            if previousframe == 0 or previousframe == 1:
                # print("off after 0 o
                try:
                    self.listbox.after_cancel(self.ForFone)
                    self.pb.after_cancel(self.av)
                except Exception:
                    pass
            elif previousframe == 2:
                # print("off after 2")
                try:
                    self.listbox1.after_cancel(self.ForFtwo)
                    self.pb.after_cancel(self.av)
                except Exception:
                    pass
            elif previousframe == 3:
                # print("off after 3")
                try:
                    self.root.after_cancel(self.ForFthree)
                    self.pb.after_cancel(self.av)
                except Exception:
                    pass
            elif previousframe == 4:
                # print("off after 4")
                try:
                    self.listbox3.after_cancel(self.ForFfour)
                    self.pb.after_cancel(self.av)
                except Exception:
                    pass
            self.ForFrameTow()
    def listClick3(self,event):
        global frameIndecator,previousframe,firsttime,recenttext
        previousframe = frameIndecator
        frameIndecator = 4
        item = self.listbox3.get(ACTIVE)
        if item != "\n":
            recenttext.append(item)
            self.musicChoice = item
            if previousframe == 0 or previousframe == 1:
                #print("off after 0 or 1")
                try:
                    self.listbox.after_cancel(self.ForFone)
                    self.pb.after_cancel(self.av)
                except Exception:
                        pass
            elif previousframe == 2:
                #print("off after 2")
                try:
                    self.listbox1.after_cancel(self.ForFtwo)
                    self.pb.after_cancel(self.av)
                except Exception:
                        pass
            elif previousframe == 3:
                #print("off after 3")
                try:
                    self.root.after_cancel(self.ForFthree)
                    self.pb.after_cancel(self.av)
                except Exception:
                        pass
            elif previousframe == 4:
                #print("off after 4")
                try:
                    self.listbox3.after_cancel(self.ForFfour)
                    self.pb.after_cancel(self.av)
                except Exception :
                        pass
            self.ForFrameFour()
            firsttime += 1
    def btn11(self, event):
        self.btn1lable.config(bg="#2ECC71",height=3)
    def btn22(self, event):
        self.btn2lable.config(bg="#2ECC71",height=3)
    def btn33(self, event):
        self.btn3lable.config(bg="#2ECC71",height=3)
    def btn44(self,event):
        self.btn4lable.config(bg="#2ECC71",height=3)
    def btn111(self, event):
        self.btn1lable.config(bg=self.colorlight)
        self.btn1.config(height=2)
    def btn222(self, event):
        self.btn2lable.config(bg=self.colorlight)
        self.btn2.config(height=2)
    def btn333(self, event):
        self.btn3lable.config(bg=self.colorlight)
        self.btn3.config(height=2)
    def btn444(self,event):
        self.btn4lable.config(bg=self.colorlight)
        self.btn4.config(height=2)

    # Menu Button events start
    def settings44(self,event):
        self.settingsImage = Image.open("icon\\icons8-settings-96.png")
        self.settingsImage = self.settingsImage.resize((45, 45), Image.ANTIALIAS)
        self.settingsImage1 = ImageTk.PhotoImage(self.settingsImage)
        self.settings.config(image=self.settingsImage1)
    def settings444(self,event):
        self.settingsImage = Image.open("icon\\icons8-settings-96.png")
        self.settingsImage = self.settingsImage.resize((35, 35), Image.ANTIALIAS)
        self.settingsImage1 = ImageTk.PhotoImage(self.settingsImage)
        self.settings.config(image=self.settingsImage1)
    def ringtone11(self,event):
        self.ringtoneImage = Image.open("icon\\icons8-audio-file-96.png")
        self.ringtoneImage = self.ringtoneImage.resize((45, 45), Image.ANTIALIAS)
        self.ringtoneImage1 = ImageTk.PhotoImage(self.ringtoneImage)
        self.ringtone.config(image=self.ringtoneImage1)

    def ringtone111(self,event):
        self.ringtoneImage = Image.open("icon\\icons8-audio-file-96.png")
        self.ringtoneImage = self.ringtoneImage.resize((35, 35), Image.ANTIALIAS)
        self.ringtoneImage1 = ImageTk.PhotoImage(self.ringtoneImage)
        self.ringtone.config(image=self.ringtoneImage1)
    def share33(self,event):
        self.shareImage = Image.open("icon\\icons8-share-144.png")
        self.shareImage = self.shareImage.resize((45, 45), Image.ANTIALIAS)
        self.shareImage1 = ImageTk.PhotoImage(self.shareImage)
        self.share.config(image=self.shareImage1)
    def share333(self,event):
        self.shareImage = Image.open("icon\\icons8-share-144.png")
        self.shareImage = self.shareImage.resize((35, 35), Image.ANTIALIAS)
        self.shareImage1 = ImageTk.PhotoImage(self.shareImage)
        self.share.config(image=self.shareImage1)
    def folder22(self,event):
        self.folderImage = Image.open("icon\\icons8-music-folder-96.png")
        self.folderImage = self.folderImage.resize((45, 45), Image.ANTIALIAS)
        self.folderImage1 = ImageTk.PhotoImage(self.folderImage)
        self.folder.config(image=self.folderImage1)
    def folder222(self,event):
        self.folderImage = Image.open("icon\\icons8-music-folder-96.png")
        self.folderImage = self.folderImage.resize((35, 35), Image.ANTIALIAS)
        self.folderImage1 = ImageTk.PhotoImage(self.folderImage)
        self.folder.config(image=self.folderImage1)

    #heart start
    def heartt(self,event):
        self.heartImage = Image.open("icon\\icons8-heart-96.png")
        self.heartImage = self.heartImage.resize((35, 35), Image.ANTIALIAS)
        self.heartImage1 = ImageTk.PhotoImage(self.heartImage)
        self.heart.config(image=self.heartImage1)
    def hearttt(self, event):
        self.heartImage = Image.open("icon\\icons8-heart-96 (1).png")
        self.heartImage = self.heartImage.resize((35, 35), Image.ANTIALIAS)
        self.heartImage1 = ImageTk.PhotoImage(self.heartImage)
        self.heart.config(image=self.heartImage1)
    #heart end

class GUI(MainControls, Buttons, events,colorCombo):

    def __init__(self):
        global selfname,firsttime
        mixer.init()
        mixer.music.set_volume(.5)
        self.root = Tk()
        self.divider=0
        self.searchBarColor = "#2ECC71"
        self.threerow = "#546E7A"
        self.threerowslable = "#37474F"
        self.colorlight = "#37474F"
        self.color = "#78909C"
        self.fontcolor = "white"
        self.listcolor = "#263238"
        self.root.geometry("1430x780")
        self.root.resizable(0, False)
        self.root.iconbitmap("icon\\1.ico")
        self.root.title("Music Discover")
        self.name, self.imgs, self.address = self.txt_to_list_maker()
        self.name.sort()
        self.upper()
        self.songList()
        self.BottomBar()
        self.menu()
        self.Listchecker()
        self.musicChoice = ""

    # There are four Frames which is show the diffrenet Lists
    def songList(self):
        global rootmusicList, frameIndecator, selfname, rootmusicAddress, rootimgAddress
        rootmusicList.clear()
        rootmusicAddress.clear()
        rootimgAddress.clear()
        self.just.config(text="My Music")
        self.frame1 = Frame(self.root, bg=self.threerow, width=1080, height=470)
        self.frame1.place(x=350, y=230)

        self.frame1mini = Frame(self.frame1, bg=self.threerow, width=1060, height=445)
        self.frame1mini.place(x=10, y=7)
        self.listbox = Listbox(self.frame1mini, width=95, bg=self.listcolor, fg="white", height=20, font=('', 14),
                               bd=0,
                               relief=FLAT, selectmode=SINGLE, highlightthickness=0, activestyle=NONE)
        self.listbox.pack(side=LEFT)
        self.listbox.bind("<Double-1>", self.listClick)
        for i in self.name:
            rootmusicList.append(i)  # I'm having to write in such a way because self.name is getting empty there
        for i in self.address:
            rootmusicAddress.append(i)
        #print(rootmusicAddress)
        for i in self.imgs:
            rootimgAddress.append(i)

        for i in self.name :
            self.listbox.insert("end",i)
            self.listbox.insert("end","\n")

        self.scrollbar = Scrollbar(self.frame1mini, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
    def recent(self):

        global recenttext, rootmusicList, frameIndecator, rootmusicAddress, rootimgAddress
        rootmusicList.clear()
        rootmusicAddress.clear()
        rootimgAddress.clear()
        self.just.config(text="Recent")
        self.frame2 = Frame(self.root, bg=self.threerow,  width=1080, height=470)
        self.frame2.place(x=350, y=230)
        self.frame2mini = Frame(self.frame2, bg=self.threerow, width=1060, height=445)
        self.frame2mini.place(x=10, y=7)
        self.listbox1 = Listbox(self.frame2mini, width=95, bg=self.listcolor, fg="white", height=20, font=('', 14),
                               bd=0,
                               relief=FLAT, selectmode=SINGLE, highlightthickness=0, activestyle=NONE)
        self.listbox1.pack(side=LEFT)
        self.listbox1.bind("<Double-1>", self.listClick1)
        for i in recenttext:
            rootmusicList.append(i)

        for i in recenttext:
            cnt = recenttext.count(i)
            for j in recenttext:
                if i == j:
                    if cnt == 1 or cnt == 0:
                        break
                    recenttext.remove(j)
                    cnt -= 1

        for i in range(0,len(recenttext)):
            for j in range(0, len(self.address)):
                if self.address[j].find(recenttext[i]) != -1:
                    rootmusicAddress.append(self.address[j])

        # print(rootmusicAddress)
        for i in range(0, len(recenttext)):
            for j in range(0, len(self.imgs)):
                a = recenttext[i][0:12]
                if self.imgs[j].find(a) != -1:
                    rootimgAddress.append(self.imgs[j])
        # print("image address: ", rootimgAddress)

        if len(recenttext) != 0:
            for i in recenttext:
                self.listbox1.insert("end",i)
                self.listbox1.insert("end", "\n")
        else:self.listbox1.insert("end", "Start Play Music.....")

        self.scrollbar1 = Scrollbar(self.frame2mini, orient=VERTICAL)
        self.scrollbar1.pack(side=RIGHT, fill=BOTH)
        self.listbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)
    def songList3(self):
        pass
        # self.frame1 = Frame(self.root, bg=self.threerow,  width=1080, height=470)
        # self.frame1.place(x=350, y=230)
    def fave(self):

        global rootmusicList, faviouritelist, frameIndecator, rootmusicAddress
        self.just.config(text="Favourite Song")
        self.frame3 = Frame(self.root, bg=self.threerow, width=1080, height=470)
        self.frame3.place(x=350, y=230)
        self.frame3mini = Frame(self.frame3, bg=self.threerow, width=1060, height=445)
        self.frame3mini.place(x=10, y=7)
        self.listbox3 = Listbox(self.frame3mini, width=95, bg=self.listcolor, fg="white", height=20, font=('', 14),
                                bd=0,
                                relief=FLAT, selectmode=SINGLE, highlightthickness=0, activestyle=NONE)
        self.listbox3.pack(side=LEFT)
        self.listbox3.bind("<Double-1>", self.listClick3)
        self.m = Menu(self.listbox3, tearoff=0)
        self.m.add_command(label="Delete", command=self.deletefav)
        self.listbox3.bind("<Button-3>", self.do_pop)
        # print("rootmusiclist (4)", rootmusicList)
        self.faviourite()
        self.scrollbar3 = Scrollbar(self.frame3mini, orient=VERTICAL)
        self.scrollbar3.pack(side=RIGHT, fill=BOTH)
        self.listbox3.config(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.listbox3.yview)
    # There are four Frames which is show the diffrenet Lists [EMD]

    # start bottom work
    def sel(self,x):
        mixer.music.set_volume(float(x)/100)

    def BottomBar(self):


        self.Bottombar = Frame(self.root, bg=self.color, width=1920, height=80)
        self.Bottombar.place(x=0, y=700)
        self.btn = Button(self.Bottombar, bg=self.threerow, activebackground=self.color, width=100, relief=FLAT,bd=0, height=80)
        self.btn.place(x=0, y=0)

        self.s = ttk.Style()
        self.s.theme_use("default")  # it will have to keep it otherwise it will be change the height
        self.s.configure("TProgressbar", thickness=6, background=self.searchBarColor,troughcolor=self.threerow, troughrelief='flat',
                    border="0")
        self.pb = ttk.Progressbar(self.Bottombar,orient=HORIZONTAL, length=900, style="TProgressbar", mode='determinate',value=0)
        self.pb.place(x=440,y=7)

        # self.pb.config(value=)
        self.volume_scale = Scale(self.Bottombar, orient=HORIZONTAL,command=self.sel,tickinterval = 100, sliderlength = 15, width = 8, length = 130, sliderrelief = 'flat', highlightthickness = 0, background = self.color, fg = 'White', troughcolor = self.threerow, activebackground =self.searchBarColor)
        self.volume_scale.set(50)
        self.volume_scale.place(x=1230, y=17)

        # tickinterval = 100, sliderlength = 15, width = 10, length = 200, sliderrelief = 'flat', highlightthickness = 0, background = 'white', fg = 'grey', troughcolor = 'blue', activebackground = 'red'
        self.startcount = Label(self.Bottombar,font=("",9),bg=self.color,fg=self.fontcolor)
        self.startcount.place(x=400, y=2)
        # self.startcount.config(text=)

        self.endcount = Label(self.Bottombar, font=("", 9),bg=self.color,fg=self.fontcolor)
        self.endcount.place(x=1350, y=2)
        # self.endcount.config(text=)

        self.lowerstatus = Label(self.Bottombar,font=("",12),fg="white",width=27,height=4,bg=self.threerow)
        self.lowerstatus.place(x=100, y=1)
        self.playImage = Image.open("icon\\pause.png")
        self.playImage = self.playImage.resize((35,35),Image.ANTIALIAS)
        self.playImage1 = ImageTk.PhotoImage(self.playImage)
        self.forwardImage = Image.open("icon\\forward.png")
        self.forwardImage = self.forwardImage.resize((25, 25), Image.ANTIALIAS)
        self.forwardImage1 = ImageTk.PhotoImage(self.forwardImage)
        self.backwardImage = Image.open("icon\\backward.png")
        self.backwardImage = self.backwardImage.resize((25, 25), Image.ANTIALIAS)
        self.backwardImage1 = ImageTk.PhotoImage(self.backwardImage)
        self.repeatImage = Image.open("icon\\repeat.png")
        self.repeatImage = self.repeatImage.resize((25, 25), Image.ANTIALIAS)
        self.repeatImage1 = ImageTk.PhotoImage(self.repeatImage)
        self.shuffleImage = Image.open("icon\\shuffle.png")
        self.shuffleImage = self.shuffleImage.resize((25, 25), Image.ANTIALIAS)
        self.shuffleImage1 = ImageTk.PhotoImage(self.shuffleImage)
        self.soundImage = Image.open("icon\\sound.png")
        self.soundImage = self.soundImage.resize((25, 25), Image.ANTIALIAS)
        self.soundImage1 = ImageTk.PhotoImage(self.soundImage)
        self.exitImage = Image.open("icon\\red cross.png")
        self.exitImage = self.exitImage.resize((35, 35), Image.ANTIALIAS)
        self.exitImage1 = ImageTk.PhotoImage(self.exitImage)
        self.heartImage = Image.open("icon\\icons8-heart-96 (1).png")
        self.heartImage = self.heartImage.resize((35, 35), Image.ANTIALIAS)
        self.heartImage1 = ImageTk.PhotoImage(self.heartImage)
        self.play = Button(self.Bottombar,image=self.playImage1, bg=self.color,activebackground=self.color,relief=FLAT,bd=0, width=35, height=35, command=self.Paush_Play)
        self.forward = Button(self.Bottombar, image=self.forwardImage1, bg=self.color,activebackground=self.color, relief=FLAT,bd=0, width=25, height=25, command=self.Forward)
        self.backward = Button(self.Bottombar, image=self.backwardImage1, bg=self.color,activebackground=self.color, relief=FLAT,bd=0, width=25, height=25, command=self.Backward)
        self.repeat = Button(self.Bottombar,image=self.repeatImage1, bg=self.color,activebackground=self.color, relief=FLAT,bd=0, width=25, height=25, command=self.reapte)
        self.shuffle = Button(self.Bottombar, image=self.shuffleImage1, bg=self.color, activebackground=self.color, relief=FLAT,bd=0, width=25, height=25, command=self.shuffle_button)
        self.sound = Button(self.Bottombar, image=self.soundImage1, bg=self.color, activebackground=self.color, relief=FLAT,bd=0, width=25, height=25)
        self.exit = Button(self.Bottombar, image=self.exitImage1, bg=self.color, activebackground=self.color, relief=FLAT,bd=0, width=35, height=35,command=exit)
        self.heart = Button(self.Bottombar, image=self.heartImage1, bg=self.color, activebackground=self.color,relief=FLAT, bd=0, width=35, height=35,command=self.activeHeart)
        self.play.place(x=780, y=25)
        self.forward.place(x=880, y=30)
        self.backward.place(x=680, y=30)
        self.repeat.place(x=570, y=30)
        self.shuffle.place(x=980, y=30)
        self.sound.place(x=1200, y=30)
        self.exit.place(x=1390, y=40)
        self.heart.place(x=470, y=25)
        self.heart.bind("<Enter>",self.heartt)
        self.heart.bind("<Leave>", self.hearttt)
    # End botton work
    def upper(self):

        self.frameupper = Frame(self.root, width=1190,bg=self.colorlight, height=230)
        self.frameupper.place(x=350, y=0)
        self.just = Label(self.frameupper, text="46", font=("", 40), fg=self.fontcolor, bg=self.colorlight)
        self.just.place(x=110, y=140)
        self.searchBarLable = Label(self.frameupper,bg=self.colorlight,font=("",18),fg=self.fontcolor, text="Search Songs")
        self.searchBarLable.place(x=120, y=30)

        self.searchBar = Frame(self.frameupper, bg=self.searchBarColor,width=305,height=36)
        self.searchBar.pack(ipadx=5, ipady=5)
        self.searchBar.place(x=50, y=70)
        self.searchtexts = StringVar()
        self.search = Entry(self.searchBar,width=25,bg=self.color,textvariable=self.searchtexts, font=("",15), fg=self.fontcolor,relief=FLAT,bd=0)
        self.search.place(x=2, y=5)
        self.searchImage = Image.open("icon\\search.png")
        self.searchImage = self.searchImage.resize((30, 30), Image.ANTIALIAS)
        self.searchImage1 = ImageTk.PhotoImage(self.searchImage)
        self.searchbtn = Button(self.searchBar, image=self.searchImage1, bg=self.searchBarColor,relief=FLAT, bd=0, activebackground=self.searchBarColor, width=30, height=30,command=self.searchfunction)
        self.searchbtn.place(x=270,y=5)

        self.p = Image.open("icon\\3.png")
        self.p = self.p.resize((100, 100), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.p)
        self.StatusLable1 = Label(self.frameupper, image=self.photo1, bg=self.colorlight)
        self.StatusLable1.place(x=0, y=120)



        self.TitleAhead = Label(self.frameupper, font=("", 25), bg=self.colorlight,fg=self.fontcolor)
        self.TitleAhead.place(x=490, y=20)
        self.AlbumAhead = Label(self.frameupper, font=("", 15), bg=self.colorlight,fg=self.fontcolor)
        self.AlbumAhead.place(x=490, y=100)
        self.ArtistAhead = Label(self.frameupper, font=("", 15), bg=self.colorlight,fg=self.fontcolor)
        self.ArtistAhead.place(x=490, y=170)

        self.StatusLable3 = Label(self.frameupper,bg=self.colorlight, width=260, height=200)
        self.StatusLable3.place(x=800, y=10)

    # Menu window work start

    def f1(self):
        try:self.frame2.destroy()
        except AttributeError:pass
        try:self.frame3.destroy()
        except AttributeError:pass
        self.songList()

    def f2(self):
        self.recent()
        try:
            self.frame3.destroy()
        except AttributeError:
            pass
        try:
            self.frame1.destroy()
        except AttributeError:pass

    def f3(self):
        self.fave()
        try:
            self.frame2.destroy()
        except AttributeError:
            pass
        try:self.frame1.destroy()
        except AttributeError:pass

    def menu(self):
        self.frame22 = Frame(self.root, bg=self.colorlight, width=350, height=700)
        self.frame22.place(x=0, y=0)
        self.label = Label(self.frame22, text="Real time Scan", bg=self.colorlight,font=("",20),fg=self.fontcolor)
        self.label.place(x=100,y=30)
        self.realtimescan = Image.open("icon\\time.png")
        self.realtimescan1 = self.realtimescan.resize((95, 95), Image.ANTIALIAS)
        self.realtimescan1 = ImageTk.PhotoImage(self.realtimescan)
        self.scan = Button(self.frame22,image=self.realtimescan1,bg=self.colorlight,relief=RAISED,bd=0,activebackground=self.colorlight, command=self.realTimeScan)
        self.scan.place(x=130,y=100)
        self.btn1lable = Label(self.frame22,bg=self.threerowslable,width=1,height=4)
        self.btn2lable = Label(self.frame22, bg=self.threerowslable, width=1, height=4)
        self.btn3lable = Label(self.frame22, bg=self.threerowslable, width=1, height=4)
        self.btn4lable = Label(self.frame22, bg=self.threerowslable, width=1, height=4)
        self.btn1lable.place(x=45, y=230)
        self.btn2lable.place(x=45, y=330)
        self.btn3lable.place(x=45, y=430)
        self.btn4lable.place(x=45, y=530)


        self.btn1 = Button(self.frame22,text="My music",font=("",12),bg=self.threerow,fg=self.fontcolor, width=27,height=2,compound=LEFT,relief=RAISED,bd=0,activebackground=self.colorlight,command=self.f1)
        self.btn2 = Button(self.frame22, text="Recent Play",font=("",12),bg=self.threerow,fg=self.fontcolor, width=27,height=2,compound=LEFT,relief=RAISED,bd=0,activebackground=self.colorlight,command=self.f2)
        self.btn3 = Button(self.frame22, text="Now Playing", font=("",12),bg=self.threerow,fg=self.fontcolor, width=27,height=2,compound=LEFT,relief=RAISED,bd=0,activebackground=self.colorlight,command=self.f3)
        self.btn4 = Button(self.frame22, text="Favourite Song", font=("", 12), bg=self.threerow, fg=self.fontcolor, width=27, height=2,
                      compound=LEFT, relief=RAISED, bd=0, activebackground=self.colorlight, command=self.fave)
        self.btn1.place(x=60, y=230)
        self.btn2.place(x=60, y=330)
        self.btn3.place(x=60, y=430)
        self.btn4.place(x=60, y=530)
        self.btn1.bind("<Enter>",self.btn11)
        self.btn2.bind("<Enter>", self.btn22)
        self.btn3.bind("<Enter>", self.btn33)
        self.btn4.bind("<Enter>", self.btn44)
        self.btn1.bind("<Leave>", self.btn111)
        self.btn2.bind("<Leave>", self.btn222)
        self.btn3.bind("<Leave>", self.btn333)
        self.btn4.bind("<Leave>", self.btn444)

        self.frame2Left = Frame(self.frame22, bg=self.colorlight, width=50, height=220)
        self.frame2Left.place(x=0, y=0)

        self.folderImage = Image.open("icon\\icons8-music-folder-96.png")
        self.folderImage = self.folderImage.resize((35,35),Image.ANTIALIAS)
        self.folderImage1 = ImageTk.PhotoImage(self.folderImage)
        self.ringtoneImage = Image.open("icon\\icons8-audio-file-96.png")
        self.ringtoneImage = self.ringtoneImage.resize((35, 35), Image.ANTIALIAS)
        self.ringtoneImage1 = ImageTk.PhotoImage(self.ringtoneImage)
        self.shareImage = Image.open("icon\\icons8-share-144.png")
        self.shareImage = self.shareImage.resize((35, 35), Image.ANTIALIAS)
        self.shareImage1 = ImageTk.PhotoImage(self.shareImage)
        self.settingsImage = Image.open("icon\\icons8-settings-96.png")
        self.settingsImage = self.settingsImage.resize((35, 35), Image.ANTIALIAS)
        self.settingsImage1 = ImageTk.PhotoImage(self.settingsImage)

        self.ringtone = Button(self.frame2Left, image=self.ringtoneImage1,bg=self.colorlight, width=35, height=35,relief=RAISED,bd=0,activebackground=self.colorlight)
        self.folder = Button(self.frame2Left, image=self.folderImage1,bg=self.colorlight, width=35, height=35,relief=RAISED,bd=0,activebackground=self.colorlight,command=self.song_select_window)
        self.share = Button(self.frame2Left, image=self.shareImage1,bg=self.colorlight, width=35, height=35,relief=RAISED,bd=0,activebackground=self.colorlight)
        self.settings = Button(self.frame2Left, image=self.settingsImage1,bg=self.colorlight, width=35, height=35,relief=RAISED,bd=0,activebackground=self.colorlight,command=self.setting)
        self.ringtone.place(x=0, y=0)
        self.share.place(x=0, y=55)
        self.folder.place(x=0, y=115)
        self.settings.place(x=0, y=185)

        self.ringtone.bind("<Enter>", self.ringtone11)
        self.folder.bind("<Enter>", self.folder22)
        self.share.bind("<Enter>", self.share33)
        self.settings.bind("<Enter>", self.settings44)
        self.ringtone.bind("<Leave>", self.ringtone111)
        self.folder.bind("<Leave>", self.folder222)
        self.share.bind("<Leave>", self.share333)
        self.settings.bind("<Leave>", self.settings444)
    def song_select_window(self):
        self.select_song = Frame(self.root,width=150,height=130)
        self.select_song.place(x=0, y=0)
        self.back_btn = Button(self.select_song,text="back",relief=GROOVE,activebackground="white",command=self.select_song.destroy)
        self.back_btn.place(x=110, y=100)
        self.Folder_select = Button(self.select_song, text="Folder Select",relief=GROOVE,activebackground="white", command=self.Song_folder_select)
        self.Folder_select.place(x=30, y=20)
        self.song_select = Button(self.select_song, text="Song Select",relief=GROOVE,activebackground="white", command=self.singal_song_select)
        self.song_select.place(x=30, y=60)

    # END Menu work window
    def setting(self):
        frame = Frame(self.root,width=300,height=300,bg="White")
        frame.place(x=0, y=0)
        btn = Button(frame, text="back",relief=GROOVE,activebackground="white",command=frame.destroy)
        btn.place(x=260, y=10)
        label = Label(frame,text="Select Themes",font=("",11),bg="white")
        label.place(x=100,y=10)
        color1 = Button(frame,width=20,height=2,text="Pink Theme", command=self.pink1,relief=GROOVE,activebackground="white")
        color1.place(x=70, y=50)
        color2 = Button(frame, width=20, height=2, text="SeeGreen Theme", command=self.seegreen1,relief=GROOVE,activebackground="white")
        color2.place(x=70, y=100)
        color3 = Button(frame,width=20,height=2,text="LightGreen Theme", command=self.lightgreen1,relief=GROOVE,activebackground="white")
        color3.place(x=70, y=150)
        color4 = Button(frame, width=20, height=2, text="Parple Theme", command=self.parple1,relief=GROOVE,activebackground="white")
        color4.place(x=70, y=200)
        color5 = Button(frame, width=20, height=2, text="Gray Theme", command=self.gray1,relief=GROOVE,activebackground="white")
        color5.place(x=70, y=250)


Software = GUI()
Software.root.mainloop()

inp = input()