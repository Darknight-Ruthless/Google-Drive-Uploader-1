import os
import subprocess
import wget

def wget_dl(url):
        try:
            print("Downloading Started")
            # i was facing some problem in filename That's Why i did this ,
            #  i will fix it later :(

            filename = os.path.basename(url)
            output = wget.download(url)

            print("Downloading Complete",filename)
            return filename
        except Exception as e:
            print("DOWNLAOD ERROR :",e)
           
            return "error",filename
        
# wget_dl(url)
