Namaste,

You are few steps away from final installation of both Itrans and miktex. This Readme if for installation on PC under Windows 95, 98. This installation may need some changes for NT.

When done, ITRANS will not be a Window. It is a "Batch" application, and you will execute the command:

C:\itrans\MYfiles>san filename 1 <enter>

where:
"san"(sanskrit)	is command for 'Convert'
"filename" 	is name of file in '.txt', where you ssaved Itrans encoded text.
"1" 		is number of columns you want per page of output. There is no default, and even "1" needs to be specified (for all output in one column).

This will create following files in indian fonts:
filename.htm	- Itrans encoded file capable of being viewed by browser
filename.html 	- The encoded document in indian font ready to put online (needs installation of xdvng font)
filename.itx 	- Text document
filename.ps	- Format for best resolution to view and print(using ghostview), and
filename.dvi	- to view and print using YAP which gets installed with Itrans. ".dvi" files take lesser space than "ps".

If you do not get it once, something is not clear enough here. Try again, as it will help immensely.

1. From 
http://sanskrit.gde.to/processing_tools_software/
download:

itrans_5.21.zip (2.1 MB) and
miktex_for_itrans_5.21.zip (about 6 MB)

The files are 8+ Mbytes so give appropriate time for downloading.

2. Using "Use Folder Names" (Very Important) option during Winzip or -d option with pkunzip, winzip/unzip these 2 ".zip" files into appropriate folders. Unzip to C:. You get 2 subdirectories:
C:\itrans
C:\texmf

You may be asked if you want to replace files. Look at the dates the files were modified. Keep newer versions of files.

3. Edit C:\AUTOEXEC.BAT using EDIT command in DOS. Paste the following at end of file:

SET ITRANSPATH=C:\ITRANS\LIB;C:\ITRANS\LIB\FONTS
path %path%;c:\texmf\miktex\bin;c:\itrans\bin;

REBOOT machine for path info to take effect.

-----------------------------------------------------------------------
4. Update Miktex configuration

>From the "start" menu bar, get the MSDos window. Get:
c:\texmf\miktex\config>
prompt. Update Miktex configuration for your PC by typing:

configure -r c:\texmf <RETURN>

5. Using Windows Explorer, go to "itrans\MYfiles" directory

Find MSDOS icon which says 'Run ITRANS from here'. 
Go to its 'properties'.
Under tab "Program", find window "Working".
Change 
f:\itrans\MYfiles
to 
C:\itrans\MYfiles:
Click "Apply" and "OK" buttons.

Double clicking on 'Run ITRANS from here' should give 
dos window with:

c:\itrans\myfiles> 
prompt. 

(Windows NT users will need to point the program to the Command.com file which is in the "Winnt" directory, as compared to the "Windows" directory for ordinary users).

6. At:
c:\itrans\myfiles> 
prompt, test our installation by typing:

san siddhivinaayaka 1 <enter>

These will create devanagari files in 
A. postscript (siddhivinaayaka.ps). If you have ghostview installed, you can view and print "siddhivinaayaka.ps" and other ps files from it. Highest resolution is obtained with these files. (To install ghostview, visit:
sanskrit.gde.to/marathi/shatataarakaa/ghost.html)

B. HTML (siddhivinaayaka.html), to view output on browser if you have the xdvng font installed (To install this font, please visit the following site:
http://www.sibal.com/sandeep/jtrans/fontinstall.html)

C. ITRANS encoded text(siddhivinaayaka.htm) which can be viewed via browser. 

At the same prompt (c:\itrans\myfiles> )

iform siddhivinaayaka

will create a
D. Device Independent file (siddhivinaayaka.dvi).  Click on "siddhivinayaka.dvi" file in the explorer. You get window asking:
Which program to use for files with such extensions, 
here, browse, and choose "YAP.exe", in c:\texmf\miktex\bin directory.
This will also setup file association for future .dvi file to be seen via YAP.

7. For 'confirmatory test', try on other files supplied:

san madhushaalaa 2 <enter>
sancolor a1008 3 <enter>	(does not work)

The batch files san.bat / sancolor.bat are used for processing (you may want to look at these to see the processing order).

--------------------------------------------------------------------------
For customization of output(fontsize, headers, footers), look into files "1.hdr", "2.hdr" and experiment with changes.
For italics, underline, bullets, (latex commands)look into:
ftp://jaguar.cs.utah.edu/private/sanskrit/processing_tools/latex.commands

Please give it a try as it worth spending time on this.
We should perhaps shorten the steps.
Please save this message for later use.
Questions/suggestions: sanskrit@cheerful.com
----------End of ITRANS-MIKTEX.readme file----------------------