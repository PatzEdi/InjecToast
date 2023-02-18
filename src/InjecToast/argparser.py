#!/usr/bin/env python3
#!/usr/bin/env python3

#Testing out the passing of arguments from command line:

import argparse
import sys
from .ToastInjector import Run
#Arguments:
parser = argparse.ArgumentParser(description = 'InjecToast, a tool to inject Toasts in Android applications.')

parser.add_argument('-t','--toastmessage', help='Toast message to inject')
parser.add_argument('-d','--decompiledappdirectory',type = str, help='Directory of decompiled app')
parser.add_argument('-m', '--method', default="MainActivity", type = str, help = "Method to inject (Default = MainActivity, onCreate())")
args = parser.parse_args()
#Main class:
class main:
	#Main function:
	def main():
		#Check if input is less than 1, then print help:
		if len(sys.argv) <= 1:
			parser.print_help()
			sys.exit(1)
			
		#Check if required are given:
		#If no directory is given, raise an error:
		if not args.decompiledappdirectory:
			print("\nERR: Decompiled app directory is required.\n")
			parser.print_help()
			sys.exit(1)
		#If no toast message is given, raise error:
		if not args.toastmessage:
			print("\nERR: A toast message is required.\n")
			parser.print_help()
			sys.exit(1)
		
		#Define the methods:
		mainAppPath = args.decompiledappdirectory
		
		toastMessage = args.toastmessage
		
		method = args.method
		
		#Refine the methods:
		#Removes any spaces from inputted directory:
		mainAppPath = mainAppPath.replace(' ', '')
		#Here, check if there is an additional slash mark, and remove it if there is:
		lastcharacter = mainAppPath[-1]
		if lastcharacter == "/":
			mainAppPath = mainAppPath[:-1]
		#Here, it is a test to determine whether parser input is valid:
		#This currently works. args.method, or any other argument, can be stored into a variable, and then the Toast Injector functions can be called with the given parameters of directory, toast, and the optional parameter of a custom method to inject.
		if args.method == "MainActivity":
			print("MainActivity is selected, proceeding to inject onCreate...")
			Run.Execute(mainAppPath, toastMessage, method)
		else:
			print(method + " is the selected method, proceeding to inject the method...")
			Run.Execute(mainAppPath, toastMessage, method)
main.main()
