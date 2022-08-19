#text to qr code generator
#author:Vicky Aryan(pwnb0y)
import qrcode
import pyfiglet as pf
import sys
from colorama import Fore, Style , init
init()
#Banner
figlet=pf.figlet_format("T3XT2QR")
print("#"*50,end="")
print(Fore.RED,)
print(figlet,end="")
print(Fore.WHITE,Style.DIM,"Created by",end=":")
print(Fore.BLUE,"pwn80y")
print(Style.RESET_ALL)
print("#"*50,end="")
print('\n')
import datetime
uf=str(datetime.datetime.now().time()).replace(':','.')
file='img'+uf+'.png'
fc="black"
bc="white"
#code for qrcode generator
if len(sys.argv)<2:
 text=input("[+]Enter your wishes text:")
 if len(text)<1:
    print("You can't process with empty data!")
    sys.exit(1)
 else:
    text=text
else:
 if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser(description="QR Generator with Input Text")
    parser.add_argument('-t','--text',help="Enter text")
    parser.add_argument('-o','--output',help="Output file name with .png extension",default='pic'+uf+'.png')
    parser.add_argument('-f','--fill',help="Filling color of QR code",default=fc)
    parser.add_argument('-b','--back',help="background color of QR code",default=bc)
    args=parser.parse_args()
    text=args.text
    file=args.output
    fc=args.fill
    bc=args.back
 else:
    pass
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=3,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color=fc,back_color=bc)
img.save(file)
print('File is saved as',end=":")
print(Fore.LIGHTGREEN_EX,file)
print(Style.RESET_ALL)
#end of script

