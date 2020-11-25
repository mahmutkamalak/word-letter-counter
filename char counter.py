from tkinter import Tk,Button,Label,StringVar,Entry,DoubleVar
Mahmut Merhaba;


window =Tk()                                                                                                               #boş bi pencere açtık
window.title('Character&word counter') #
window.configure(background='red')                                                                                        #windowun değişkenlerini ayarladık
window.geometry('320x220')
window.resizable(width=True,height=True)                                                                                   ## kullanıcı boyutu değiştiremesin diye ayar yaptık 

######First FUNCTION#######
word_count=0
char_count=0

def calculatee ():
    value=str(ft_entry.get())                                                                                               #get kullanılmasının sebebi uygulamaya girilen değeri fonsiyon için buraya almak
    split_string=value.split()
    word_count=len(split_string)
        
    mt_value.set(word_count)                                                                                              #yüzde 4f ile 4 atne decimal point olsun dedik.
    
    for w in split_string:
        global char_count
        char_count += len(w)
    mt_value2.set(char_count)
    return word_count,char_count
def clear():
    ft_value.set("")
    mt_value.set("")
    mt_value2.set("")





ft_lbl= Label(window,text="TEXT",bg="purple",fg="white",width=14)                               # label oluşturduk ,renklerini ne yazağını belirledik
ft_lbl.grid(column=0,row=0,padx=15,pady=15)                                                      #oluşturulan labelın konumunu belirledik winndowdaki

ft_value = StringVar()                                                                           #aslında değerin tipini belirttik tüm sayılar ve decimal sayılar yazılabilir
ft_entry=Entry(window,textvariable=ft_value,width=14) #
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')                                                                        #uygulama 0 dan başlaması için temizledik

ft_lbl = Label(window,text="Character",bg="black",fg="white",width=14)
ft_lbl.grid(column=0,row=2,padx=15,pady=15)

mt_lbl = Label(window,text="Word",bg="brown",fg="white",width=14)
mt_lbl.grid(column=0,row=1)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=30)
mt_entry.delete(0,'end')

mt_value2 = DoubleVar()
mt_entry2 = Entry(window,textvariable=mt_value2,width=14)
mt_entry2.grid(column=1,row=2,pady=30)
mt_entry2.delete(0,'end')

convert_btn=Button(window,text='calculate',bg='blue',fg='white',width=14,command=calculatee)    #command butonun hangi fonk çağırıcağını gösterir
convert_btn.grid(column=0,row=3,padx=15)

clear_btn = Button(window,text="Clear",bg="black",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)


window.mainloop()                                                                               # prpgramın çalışmasını sağlar

#https://www.codevscolor.com/python-count-words-characters-string/  ###KAYNAK1