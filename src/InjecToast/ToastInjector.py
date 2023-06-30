#!/usr/bin/env python3

#MADE WITH PASSION BY PATZEDI

#This project is currently WORKING, so give it a star on GitHub! :)

from xml.dom.minidom import parseString
#Notes:
#1. Parameter mainAppPath is the path for the decompiled app.
#This script uses my FinderZ library to locate the files allocated with the MainActivity.
import FinderZ
from FinderZ import GatherInfo
from FinderZ import fileOperands
from FinderZ import callBash

#Main os library 
import os


#Main class that searches through AndroidManifest.xml, searches MainActivity, and goes to the file named under what happens in the main activity.
class Search:
	#First step:
	#Find the directory of the mainActivity file path
	def mainActivityFileDir(mainActivityName, mainAppPath): 
		mainActivityFile = fileOperands.findFiles(mainActivityName, mainAppPath, exactSearch = True)
		#Turn the list into a string:
		mainActivityFile = ' '.join(mainActivityFile)
		#Enter file directory for later use:
		directory = os.path.dirname(mainActivityFile)
		return directory
	#Use the FinderZ library to go directly to the file containing the mainActivity.
	def findMainActivityName(mainAppPath, pattern, smaliCode):
		manifestDirectory = mainAppPath + "/" "AndroidManifest.xml"
		#Turn it into a string:
		print(manifestDirectory)
		try:
			f = open(manifestDirectory, "r")
			contents = f.read()
		except:
			raise Exception("ERR: An error occurred upon opening of AndroidManifest.xml. Is the path correct?")
		#Read the file contents:
		
		#print(contents)
		
		#Find the mainAcitivty inside Android Manifest.xml:
		dom = parseString(contents)
		activities = dom.getElementsByTagName('activity')
		perms = dom.getElementsByTagName('uses-permission')
		
		for activity in activities:
			Activity = activity.getAttribute('android:name')
			
			intents = activity.getElementsByTagName('intent-filter')
			for intent in intents:
				#Search all "actions":
				actions = intent.getElementsByTagName('action')
				for action in actions:
					#Checks if it is in mainactivity section:
					if action.getAttribute('android:name') == 'android.intent.action.MAIN':
						mainActivity = str(action.getAttribute('android:name'))
						#Remove everything before the period of the actual name of the activity:
						MainActivity = Activity.rsplit('.', 1)[1]
						return MainActivity
					else:
						print("I: ERR: No main activity found.")
						planB = int(input("\nWould you like to proceed by scanning all of the files in the app for onCreate (May take a long time/Less accurate)? (1/2): "))
						if planB == 1:
							#Initiate planB:
							Inject.scanFilesForMethod(mainAppPath, pattern, smaliCode, "onCreate")
						elif planB == 1:
							print("\nI: Operation was canceled by user, exiting.")
							exit()
						exit()
	#Based on the MainActivity file name, find that file in the directory of the decompiled app:
	def goToMainActivityFile(mainActivityFileName, mainAppPath): #1
		mainActivityFile = fileOperands.findFiles(mainActivityFileName, mainAppPath, exactSearch = True)
		#Turn the list into a string:
		mainActivityFile = ' '.join(mainActivityFile)
		#Enter file directory for later use:
		directory = os.path.dirname(mainActivityFile)
		#os.chdir(directory)
		
		f = open(mainActivityFile, "r")
		
		return f #Put this function equal to a variable, and put that variable as the fileObject parameter for the injectCode() function below.
	
#Main class to inject the actual code:
class Inject:
	#Read the contents of the file containg the smali code to inject (SmaliInjectionSnippet.txt):
	def getSmaliInjectContents(toastMessage):#2
	
		#Get the contents:
		contents = "	const/4 v0, 0x1\n\n	const-string v1, \"Message\"\n\n	invoke-static {p0, v1, v0},\n\n	Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;\n\n	move-result-object v0\n\n	invoke-virtual {v0}, Landroid/widget/Toast;->show()V"
		#Replace
		toastCode = contents.replace("Message", toastMessage)
		#Return the smali code to then inject:
		return toastCode
	#Function to execute a "plan b" in case no MainActivity is found or no onCreate method is found in the mainactivity file.
	def scanFilesForMethod(mainAppPath, pattern, smaliCode, method):
		
		print("I: Attempting to find method...")
		searchFile = fileOperands.scanFilesForContent(mainAppPath, pattern, ".smali")
		
		fileObjectPlanB = open(searchFile, 'r')
		#Here, do what you did above again, but this time in another file.
		
		fileLines = fileObjectPlanB.readlines()
		
		#Line count:
		count = 0
		# Strips the newline character
		methodCheck = False
		#Here, make a big while loop. It iterates over each line of the file, and stops when it finds the given method. Once it finds the given method, it goes up two or three lines until the first "line" plus a number is found. The code will then be injected after that "line" plus a number.
		#This goes in a loop, because it cant find the given method.
		for line in fileLines:
			count += 1
			Line = str(line.strip())
			#Put if statement here, whether given method is in that line:
			if (pattern in Line) and methodCheck == False:
				print("I: "+ method + " method found.")
				methodCheck = True
				#Here, search for the lines under, to check for any ".line". The code will be injected right after that ".line".
				creep = 0
				while True:
					creepLineContents = fileLines[count+creep]

					if ".locals" in creepLineContents:
						print("I: Found .locals")
						print("I: Adding a local")
						local = fileLines[creep+count]
						
						#Split the string and turn the number of locals into an int.
						localnumber = int(local.split(".locals",1)[1])
						#Add a local:
						addedlocal = str(localnumber + 1)
						#Add a local:
						fileLines[count+creep] = "	.locals " + addedlocal + "\n"
						#exit()
						
						break
					else:
						print("I: No .locals")
						exit()
					creep += 1
				#PUT INJECTION CODE HERE:
				creep2 = 0
				print("I: Adding new lines...")
				for i in range(5):
					
					creep2 += 1
					creepplus1 = count + creep2
					creepplus21 = str(creepplus1)
					# now change the lines:
					fileLines.insert(creepplus1, "\n")
				fileLines[count+2] = smaliCode
				#Write everything again:
		if methodCheck == False:
			print("I: No "+ method+ " method found, Toast Unsuccessful!")
			exit()
			
		#Write the lines to the file:
		with open(searchFile, 'w') as file:
			file.writelines(fileLines)
			
		#Injection completed:
		print("\nInjection Complete.\n\nLOG END")
		exit()
	#Inject the smali code (Read the SmaliInjectionSnippet.txt):
	def injectCode(smaliCode, fileObject, mainActivityFileDir, mainActivityFileName, mainAppPath, pattern):
		#Read the file contents:
		fileLines = fileObject.readlines()
		#Line count:
		count = 0
		# Strips the newline character
		onCreateCheck = False
		#Here, make a big while loop. It iterates over each line of the file, and stops when it finds the onCreate method. Once it finds the onCreate method, it goes up two or three lines until the first "line" plus a number is found. The code will then be injected after that "line" plus a number.
		#This goes in a loop, because it cant find the on create method (Maybe use regex?)
		for line in fileLines:
			count += 1
			Line = str(line.strip())
			#Put if statement here, whether onCreate() method is in that line:
			if (pattern in Line) and onCreateCheck == False:
				print("I: onCreate method found.")
				onCreateCheck = True
				#Here, search for the lines under, to check for any ".line". The code will be injected right after that ".line".
				creep = 0
				while True:
					creepLineContents = fileLines[count+creep]
					
					if ".locals" in creepLineContents:
						print("I: Found .locals")
						print("I: Adding a local")
						local = fileLines[creep+count]
						#Split the string and turn the number of locals into an int.
						localnumber = int(local.split(".locals",1)[1])
						#Add a local:
						addedlocal = str(localnumber + 1)
						#Add a local:
						fileLines[count+creep] = "	.locals " + addedlocal + "\n"
						#exit()
						break
					else:
						print("I: No .locals")
						exit()
					creep += 1
				#PUT INJECTION CODE HERE:
				creep2 = 0
				print("I: Adding new lines...")
				#Loop to add new lines:
				for i in range(5):
					creep2 += 1
					creepplus1 = count + creep2
					creepplus21 = str(creepplus1)
					# now change the lines:
					fileLines.insert(creepplus1, "\n")
				#Injection:
				fileLines[count+2] = smaliCode
		#BACKUP PLAN STARTS HERE:
		if onCreateCheck == False:
			print("I: ERR: No onCreate method found")
			
			#Put code here to ask if backup plan is wanted in order to proceed:
			planB = int(input("\nWould you like to proceed by scanning all of the files in the app for onCreate (May take a long time/ Less accurate)? (1/2): "))
			if planB == 1:
				#Proceed to put code here, that finds the onCreate method by scanning every single file:
				#New function to replace all of the additional code that was just replicating:
				Inject.scanFilesForMethod(mainAppPath, pattern, smaliCode, "onCreate")
			elif planB == 2:
				print("\nI: Operation canceled by User, no onCreate method found in MainActivity")
				exit()
				
		elif onCreateCheck == True:
			fileDir = mainActivityFileDir + "/" + mainActivityFileName
			print(fileDir)
			
			with open(fileDir, 'w') as file:
				file.writelines(fileLines)
#Simple class to add the .smali file extension to the mainActivityName
class fileExtension:
	def addFileExtension(mainActivityName, fileExtensionType):
		fullFileName = mainActivityName + fileExtensionType
		return fullFileName
#Class to run the code(Main code that runs the code here):
class Run:
	def Execute(mainAppPath, toastMessage, method):
		#RUN THE CODE:
		#Main pattern to find onCreate (used for different purposes):
		if method == 'MainActivity':
			
			pattern = ".method" and "onCreate("
			
			#As initialization, ask the path and toast message to insert first:
	#		mainAppPath = input("\nMain decompiled app directory: ")
	#		codeInject = input("Toast message to inject: ")
			
			#Start the logs:
			print("\nLOG START:\n")

			smaliInjectCode = Inject.getSmaliInjectContents(toastMessage)
			
			#Step 3, get mainActivityName:
			#Gather the name of the MainActivity:
			
			mainActivityName = Search.findMainActivityName(mainAppPath, pattern, smaliInjectCode)
			
			print("\nI: Found main activity, name: " + mainActivityName)
			
			#Step 4, add the extension file type "smali":
			#Add the extension in order for the FinderZ lib to go find that file and go to that file.
			finalFile = fileExtension.addFileExtension(mainActivityName, ".smali")
			
			print("I: Searching for file named: " + finalFile)
			
			#Step 5:
			mainActivityFileDir = Search.mainActivityFileDir(finalFile, mainAppPath)
			
			#Go to the file containing main activity:
			fileObject = Search.goToMainActivityFile(finalFile, mainAppPath)
			
			
			
			#currentdir = os.getcwd()
			
			#Final step, inject:
			print("I: File found, proceeding to inject...")
			Inject.injectCode(smaliInjectCode, fileObject, mainActivityFileDir, finalFile, mainAppPath, pattern)
			print("\nI: Injection Complete.\n\nLOG END")
			exit()
		#If a custom input is put in, execute this:
		else:
			#Custom pattern:
			pattern = ".method" and method
			
			#Start the logs:
			print("\nLOG START:\n")
			
			#Step 2, get smaliinjectionsnippet directory and its contents::
			smaliInjectCode = Inject.getSmaliInjectContents(toastMessage)
			
			#ScanFilesForMethod:
			Inject.scanFilesForMethod(mainAppPath, pattern, smaliInjectCode, method)

		
		
#MainMenu (User interface purposes):
class Menu:
	#Clear the screen
	def clearScreen():
		if(os.name == 'posix'):
			os.system('clear')
		else:
			os.system('cls')
	#MainMenu (Optional, just there for user interface):
	def mainMenu():
		questions = "(1) Inject Toast:\n(2) About:\n(99) Exit: "
		while True:
			#Clear the screen:
			Menu.clearScreen()
			MainMenu = int(input(questions))
			if MainMenu == 1:
				#RUN THE CODE:
				Run.Execute()
			elif MainMenu == 2:
				Menu.clearScreen()
				print("\nThis was created by PatzEdi! This is a script that lets you inject toast messages in Android Apps. It works well, so go ahead, and try it! I created this because I wanted to easily inject toasts instead of having to do it Manually every single time. Thanks for using the program, and happy Toasts!\n")
			elif MainMenu == 99:
				print("\nThank you for using InjecToast!")
				exit()
			else:
				print("\nPlease put a valid option 1-3.\n")
				
				
#All of that, simplified in one line of code!! :)
#Uncomment to execute menu:
#Menu.mainMenu()
