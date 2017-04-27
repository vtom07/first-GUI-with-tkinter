import tkinter as tk
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from queue import Queue
import sys
class CustomHandler(FileSystemEventHandler):
    def __init__(self, app):
        FileSystemEventHandler.__init__(self)
        self.app = app
    def on_created(self, event): app.notify(event)
    def on_deleted(self, event): app.notify(event)
    def on_modified(self, event): app.notify(event)
    def on_moved(self, event): app.notify(event)

# class App(object):
#     def __init__(self):
#         path = sys.argv[1] if len(sys.argv) > 1 else "."
#         handler = CustomHandler(self)
#         self.observer = Observer()
#         self.observer.schedule(handler, path, recursive=True)
#
#
#
#         self.queue = Queue()
#         self.root = tk.Tk()
#
#         self.text = tk.Text(self.root)
#         self.text.pack(fill="both", expand=True)
#         self.text.insert("end", "Watching %s...\n" % path)
#TOM TK APP
class App(tk.Frame):
    def __init__(self, master=None):
        path = sys.argv[1] if len(sys.argv) > 1 else "."
        handler = CustomHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, path, recursive=True)
        self.queue = Queue()
        self.root = tk.Tk()
        self.helper=0
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        top = tk.Tk("Hello")
        L1 = tk.Label(top, text="User Name")
        L1.pack( side = tk.LEFT)
        E1 = tk.Entry(top, bd =5)

        E1.pack(side = tk.RIGHT)

        label = tk.Message( self, text="last update 25/02/17  13:58", relief=tk.RAISED, bg="#72726a", borderwidth=0, highlightthickness=0)


        label.pack()
        label.place(x=100,y=800)

    #    self.master.title("EZ-MEAL")

        self.configure(background = "#72726a")

        self.pack(fill=tk.BOTH, expand=10)

        logo = PhotoImage(file="Capture.gif")

        w1 = Label(self, image=logo, borderwidth=0, highlightthickness=0)

        w1.image = logo
        w1.pack()
        #w1.place(x=700,y=400)

        quitButton = tk.Button(self, text="Exit",command=self.client_exit, height= 5 , width =15, bg = "#e0b93a" , fg = "black")

        quitButton.place(x=700, y=700)

        AcceptButton = tk.Button(self, text="Accept Order",command =self.OrderAcceptedNotification, height= 5 , width =25, bg = "#e0b93a" , fg = "black")

        AcceptButton.place(x=300, y=200)
        orderisreadyButton = tk.Button(self, text="Order is ready",command =self.OrderisreadyNotification, height= 5 , width =25, bg = "#e0b93a" , fg = "black")

        orderisreadyButton.place(x=500, y=200)

        listbox1 = tk.Listbox(self,height =30, width =25,bg = "beige")
        self.listbox1=listbox1
        listbox1.pack()

        listbox1.insert(1,"Number of the Order:")
        listbox1.place (x=100,y=300)

        listbox2 = tk.Listbox(self,height =30, width =25, bg = "beige")
        self.listbox2=listbox2
        listbox2.pack()

        listbox2.insert(1,"type of food:")

        listbox2.place (x=300,y=300)

        listbox3 = tk.Listbox(self,height =30, width =25, bg = "beige")

        listbox3.pack()
        self.listbox3=listbox3

        listbox3.insert(1,"cost of order:")

        listbox3.place (x=500,y=300)

        w = tk.Label(self, text="Ez meal APP version 0.00.03", bg="red", fg="white")
        w.pack(side= tk.TOP ,fill=tk.X)
        self.root.bind("<Destroy>", self.shutdown)
        self.root.bind("<<WatchdogEvent>>", self.handle_watchdog_event)
        self.observer.start()

    def OrderAcceptedNotification(self):

         msg = messagebox.showinfo( "OrderAccepted", "you accepted the last order")

    def OrderisreadyNotification(self):

         msg = messagebox.showinfo( "OrderisReady", " You sent order ")

    def client_exit(self):
        exit()
    def handle_watchdog_event(self, event):
        """Called when watchdog posts an event"""
        if self.helper==0:
            watchdog_event = self.queue.get(str)
            print("event type:", type(watchdog_event))
            self.listbox1.insert(2, str("1") + "\n")
            self.listbox2.insert(2,str("pizza")+"\n")
            self.listbox3.insert(2,str("12 shekels")+"\n")
            self.helper=1
        else :
            self.helper=0
    def shutdown(self, event):
        """Perform safe shutdown when GUI has been destroyed"""
        self.observer.stop()
        self.observer.join()

    def mainloop(self):
        """Start the GUI loop"""
        self.root.mainloop()

    def notify(self, event):
        """Forward events from watchdog to GUI"""
        self.queue.put(event)
        self.root.event_generate("<<WatchdogEvent>>", when="tail")
root = tk.Tk()
root.geometry("1000x1000")
app = App(root)
app.mainloop()
