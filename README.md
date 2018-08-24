# ticker

This will be a simple Python app that, when executed, will ask for a stock
symbol. It will then open search pages in several pre-specified websites.


Sites:
zacks.com
finviz.com
openinsider.com
earningswhispers.com
shortsqueeze.com
insidercow.com  -- This one could be tricky. I can't build the search url.
    I talked to Scott. He said to not worry about this one for now.

To do this project I am going to need to learn a couple new things. I will need
to build a simple ui. I will use tkinter to do this. I will also need to learn
how to package this up into an executable. I plan to use pyinstaller for that.

Resources:
https://www.pyinstaller.org/
https://docs.python.org/3/faq/gui.html#id5
https://docs.python.org/3/library/tk.html#tkinter
http://effbot.org/tkinterbook/tkinter-hello-again.htm

Issue with Selenium and PyInstaller
https://stackoverflow.com/questions/39563851/how-to-include-chromedriver-with-pyinstaller

For creating Mac executable or installer and testing.
https://techsviewer.com/install-macos-10-14-mojave-virtualbox-windows/
https://www.makeuseof.com/tag/macos-windows-10-virtual-machine/

For signing generated exe.
https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85)
https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Win-Code-Signing
https://eclipsesource.com/blogs/2016/09/07/tutorial-code-signing-and-verification-with-openssl/
