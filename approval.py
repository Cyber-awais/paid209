def main_apv():
    os.system('clear')
    #Wasi ke jaga apna name likhlo 
    ak="AWAIS"
    logo()
    #apni id ke link dal lo 
    os.system('xdg-open https://www.facebook.com/tere.baap.ka.link.hain.kya')
    try:
    	#qureshi ke jaga apna mame lagau
        key1=open('/data/data/com.termux/files/usr/bin/.awaiskhan-cov', 'r').read()
    except IOError:
        os.system("clear")
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("           THIS TOOL IS PAID RS 150")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]--------------------------------------------------------------")
        #qureshi ke jaga apna name or kch ni cherna
        kok=open('/data/data/com.termux/files/usr/bin/.awaiskhan-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(6)
        #nichy number ki hata k apna numbr dal lo 
        os.system("xdg-open https://wa.me/+92452532977")
        #nichy  link hata k apni github ke link lagau
    r1=requests.get("https://github.com/Cyber-awais").text
    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
        R()
    else:
        os.system("clear")
        os.system('xdg-open https://youtube.com/channel/UCXdYPUUNiA6HtutWKd07XMA')
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("          THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]--------------------------------------------------------------")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(3.5)
        #Numbr chnge krlyna
        os.system("xdg-open https://wa.me/+923452532977")