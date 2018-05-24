"""This program copies Microsoft Spotlight Images directly to Spotlight
                    Directory in Pictures Directory.

                    - Written from Scratch by
                            Gagan Gulyani

"""

try:
    
    import os
    import os.path
    import shutil
    import time

    try:
        from PIL import Image
        
    except ImportError:
        print ("\nInstall Pillow Image Library to run the Script")
        
    src=os.path.expanduser("~")+r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    src=src.replace("\\","/")
    dest=os.path.expanduser("~")+"\\Pictures\\Spotlight"


    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(dest+"/Portraits"):
        os.makedirs(dest+"/Portraits")
        
    count_existing=count_new=0

    for i in os.listdir(src):

        current_image = src + "/" + i
        portrait = dest + "/Portraits/" + i
        landscape = dest + "/" + i
        
        im = Image.open(current_image)
        width, height = im.size
        
        if os.path.exists(portrait) or os.path.exists(landscape) or os.path.exists(portrait+".jpg") or os.path.exists(landscape+".jpg"):
            count_existing+=1
        
        else:
            if width == 1920 or width == 1080:
                
                if width<height:
                    print ("\nTransfering {} of dimensions {}x{} in {}".format(i,width,height,dest+"/Portraits"))
                    shutil.copy2(current_image,dest+"/Portraits")
                    print("Size :",os.path.getsize(portrait))
                    os.rename(portrait,portrait+".jpg")
                    
                else:
                    print ("\nTransfering {} of dimensions {}x{} in {}".format(i,width,height,dest))
                    shutil.copy2(current_image,dest)
                    print ("Size :",os.path.getsize(landscape))
                    os.rename(landscape,landscape+".jpg")
                    
                count_new+=1
                
    else:
        print ("*"*35 + "\n{} image(s) already exists.\n\n{} New images copied in Spotlight Directory.".format(count_existing,count_new))
        print ("\nOperation Completed Successfully!\n"+"*"*35)

        
except Exception as e:
    logs=r"C://Program Files//Wallpaper_Setter_By_GG//logs.txt"
    
    if os.path.exists(logs):
        f=open(logs,"a")
    else:
        f=open(logs,"a")
        f.write("="*75+"\n\nError Logs of the Wallpaper Setter by GG\n\n"+"="*75+"\n")

    t="\nDate : {}\nTime : {}".format(time.strftime("%H:%M:%\
S",time.gmtime()),time.strftime("%d-%m-%Y",time.gmtime()))
    
    report = "="*75+"\n\n"+t+"\n\n"+"Error Mes\
sage : "+str(e)+"\n\n"+"="*75+"\n"+"\n"+"="*15+"Finished\n"+"="*15+"\n"

    print (report)
    
    f.write(report)

    f.close()
    

