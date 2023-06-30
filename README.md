# InjecToast

A tool to inject toasts in Android applications.

![injectoast-logofinal](https://user-images.githubusercontent.com/116693779/219882646-4178fc5e-585f-4196-8076-093af1694a3b.png)

<p align="center">
	<img src="https://img.shields.io/badge/Creator-PatzEdi-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Version-Latest-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Name-InjecToast-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/License-MIT-brightgreen"
		height="23">
</p>

This script uses android application decompilation tools and the FinderZ library in order to function properly.
HUGE credits to the authors of the tools that are able to decompile android applications.

**This tool is made for educational purposes only!**

## **A command line application that provides you with the ability to inject toasts in Android Applications, written in Python** 
____________________________________________________________________________
## **CHANGELOG: 1.1.5**
- Release Version 1.1.5
- Fixed comptaibility issue with FinderZ V2.

## **Tool Information (IMPORTANT)**
- Before you proceed, make sure to install my FinderZ library at: [FinderZ](https://pypi.org/project/FinderZ/) This is used in order to manage files properly.
- It is important to understand that a decompilation tool is required. You MUST decompile the .apk file before using the injector, you can not just give the injector the .apk file, you need to decompile it first.
- Concerning which tools to use, HUGE credits to those who decompile android applications:
- Apktool, and ApkToolM.
- Here are the links:
- [ApkTool](https://ibotpeaches.github.io/Apktool/)
- [ApkToolM (For Android Devices only)](https://maximoff.su/apktool/?lang=en)
- FOR ANDROID DEVICES, READ BELOW:
- If you are on an android device, ApkTool M is a useful application that lets you decompile applications on your device. In order to use InjecToast, however, you also need [Termux](https://termux.dev/en/)
- With Termux, you can emulate a terminal, making it very useful. You can run pip commands, run packages, do anything, which is why if you are on an Android device, you need to have this in order to execute InjecToast.

## **Installation**
Install with pip:
```
pip3 install InjecToast
```

## **Usage**
Parameters/Arguments: 
```
-t TOASTMESSAGE
-d DECOMPILEDAPPDIRECTORY
-m METHOD
```
Concerning the Arguments, -t is for the toast message (Important, make sure to put your toast in between quotation marks!), -d is for the decompiled application directory, and -m is optional at a default of onCreate (MainActivity). If you want to inject a custom method, use -m and put the name of the method after the -m. Please note that the toast message and directory arguments are required. 

Execute From Command Line:
```
InjecToast
```
Execute from Command Line with arguments:
```
InjecToast -t "ToastMessage" -d /path/to/decompiledapp/ -m Method #This is optional, default = onCreate / MainActivity.
```
Full steps:

- Decompile the app using apktool (if you are on android, you can use ApkTool M. More information above under Tool Information)
- Copy the directory of the decompiled app.
- Go to your terminal, and enter:

```
InjecToast -t "YourMessageHere" -d TheAppDirectory #Please note that the toast message NEEDS to be in between quotes!
```

- Once the Log and process has finished, you can recompile the app with apktool of ApkToolM (For Android).
- Once it is compiled, make sure the apk is signed, and you will be good to go!

## **Features**
- Inject toasts in Android Applications.
- Error catching, ability to try and attempt to inject the toast even if something fails
- Inject a toast message in any method of the application.
- Very easy to use.
- Command line interface helps save time, rather than having a menu to choose options from..
- Logs to print out at what stage the execution is.
- Cross-platform support, works on Android devices, Mac, PC, Linux, you name it!
- Fast and efficient, no time lost. Just inject, compile, and you are good to go.
____________________________________________________________________________
## **Why?**
- I wanted to showcase how one can easily create a tool that edits other things based off of different code. It was really cool and fun doing this project. 
- Toast messages are a way to decorate an android app, or even debug it. Say, for example, you had your android phone on you, and you experience a bug. You then decompile your app, inject a toast in any method, and look at what happened. 
- Not only that, but many more reasons, one of them being for fun and to showcase how one can easily edit other code by programming in a different language. 
____________________________________________________________________________
## **How?**
- Using the FinderZ library created by myself, everything was much easier to do. Dealing with files was no longer painful. 20 to 30 lines of code, really only became one, thanks to the FinderZ library. 
- Concerning the code, the summary of what it does is that it basically searches the files for the method, gets the smali contents, and then writes those contents to the line number after the ".locals" of the method.
- In case you did not know, smali is a code that is semi human-readable, and you get the code when decompiling android applications.
____________________________________________________________________________
## **User notice**
- **This tool is made for educational purposes only!**
- Please note that you need to know what you are going when it comes to decompiling, recompiling, and signing an android application.
- When dealing with the toast message, -t, put your toast message in between two quotes!
- You MUST have the FinderZ library installed in order for this to function. This provides the application with the needed functions to search for files and file content in the app directory.
- For the application to work, you can use apktool, or, if you are on an Android phone, you can use ApkToolM. More information above under the Tool Information section!
- This project is under MIT license! Enjoy :)
____________________________________________________________________________
## **DEALING WITH ERRORS:**
- If you encounter an error in the compilation of an application, it means that the application is not supported. Overall, the injector works for around 90-95 percent of applications. Sometimes, a compilation tool such as apktool will give you register errors. This means that the application code conflicts with the injector's code.
- If you get other errors, script wise, such as parsing errors, file finding errors, etc, feel free to create an issue on the GitHub page.
## **Services used (Credits):**
- [FinderZ](https://github.com/PatzEdi/FinderZ/)
- [XML](https://docs.python.org/3/library/xml.dom.minidom.html)
- Services used to decompile android apps:
- [ApkTool](https://ibotpeaches.github.io/Apktool/)
- [ApkToolM (For Android Devices only)](https://maximoff.su/apktool/?lang=en)
____________________________________________________________________________
## **Make sure to leave a star!**
- If you like this project, leaving a star is what motivates me in doing more. Thank you, and I hope this is useful to all.