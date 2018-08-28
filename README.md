# About
Ticker will be a simple Python app that, when executed, will ask for a stock symbol. It will then open search pages in several pre-specified websites.

---
## Sites:
* zacks.com  
* finviz.com  
* openinsider.com  
* earningswhispers.com  
* shortsqueeze.com  
* insidercow.com  -- This one could be tricky. Due to how the site works I can't build the search url. I am ignoring this one for now.

---
## Goals
To do this project I am going to need to learn a couple new things.

I will need to build a simple ui. I am currently using tkinter to do this. I may do some research on other options.

I will also need to learn how to package this up into an executable. I plan to use pyinstaller for that. As part of this I will also need to make a Mac version. I may need either access to a Mac computer or a VM to run Mac OS on my computer.

# Resources: 
List of blog posts, websites, or other resources consulted while making this.  

## tkinter
* https://docs.python.org/3/faq/gui.html#id5  
* https://docs.python.org/3/library/tk.html#tkinter  
* http://effbot.org/tkinterbook/tkinter-hello-again.htm 

## User sortable list box in tkinter:
* http://effbot.org/tkinterbook/listbox.htm  
* https://flylib.com/books/en/2.9.1.230/1/  

## MVC discussions:
* https://gist.github.com/ajfigueroa/c2af555630d1db3efb5178ece728b017
* https://sukhbinder.wordpress.com/2014/12/25/an-example-of-model-view-controller-design-pattern-with-tkinter-python/  
* https://github.com/python-programmer/kivy-simple-mvc-template

## Info on config file:
* https://docs.python.org/3.7/library/configparser.html
* https://martin-thoma.com/configuration-files-in-python/
* http://buklijas.info/blog/2018/01/01/always-start-with-simple-solution/

## PyInstaller:
* https://www.pyinstaller.org/ 

## Issue with Selenium and PyInstaller  
* https://stackoverflow.com/questions/39563851/how-to-include-chromedriver-with-pyinstaller  

## For creating Mac executable or installer and testing.  
* https://techsviewer.com/install-macos-10-14-mojave-virtualbox-windows/  
* https://www.makeuseof.com/tag/macos-windows-10-virtual-machine/  

## For code signing final exe.  
* https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85)  
* https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Win-Code-Signing  
* https://eclipsesource.com/blogs/2016/09/07/tutorial-code-signing-and-verification-with-openssl/  
