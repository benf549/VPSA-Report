	#v1.0 of general VPSA information parsing
	#Added emma parsing and output.
from bs4 import BeautifulSoup
import csv
import io
import os
import openpyxl

def main():
	FBexists = os.path.isfile('./facebook.html')
	EMMAexists = os.path.isfile('./emma.html')
	REPXLexists = os.path.isfile('./REPORT.xlsx')

	if FBexists: 
		#mon = "04"
		mon = input("input the number of the month you would like data for (ex: April is 04, December is 12): ")

		Placeholder0 = []
		Placeholder1 = []
		Placeholder2 = []
		dat = []
		indices = []
		Dates = []
		Titles = []
		Views = []
		Clicks = []
		Rxn = []

		with io.open("facebook.html", "r", encoding="utf-8") as infile:
			soup = BeautifulSoup(infile, "html.parser")
		###soup = BeautifulSoup(open("./facebook.html"), "html.parser")

		ind = []
		dates = soup.findAll("tr",{"class":"_5k4c"})
		for link in dates:
			date = link.td
			Placeholder0.append(str(date).split(">")[2].split("<")[0])
		#print(Placeholder0)
		Test = {}
		T2 = []
		j = 0
		for i in Placeholder0:
			if mon in i.split('/'):
				T2.append(i)

		j = Placeholder0.index(T2[0])


		for i in Placeholder0:
			if mon in i.split('/')[0]:
				#print(i)
				Dates.append(i)
				Test[j] = i
				j = j+1

		##print(Dates)
		indices = range(min(Test.keys()),max(Test.keys())+1)
		#####################################################
		#Foud the Dates and added indices according to the number that they were found at.
		#####################################################

		titles = soup.findAll("div", {"class":"_42ef"})
		for title in titles:
		        Titl = title.div
		        Placeholder1.append(str(Titl)[:100].replace("\n","").replace(",", ".").split(">")[1])

		Titles = Placeholder1[indices[0]:indices[-1]+1]

		##print(Titles)

		#####################################################
		#Creates list of titles with corresponfing indices to their dates.
		#####################################################

		numbers = soup.findAll("div", {"class":"_5kn3 ellipsis"})
		for number in numbers:
		       data = number
		       Placeholder2.append(str(data).split(">")[1].split("<")[0])
		#Replaces 1.1k and 2k notation with 1100 and 200o for example.
		d=0
		for shortened in Placeholder2:

			if '.' in shortened:
				for period in shortened:
					if period == ('.'):
						Placeholder2[d] = shortened.replace(period, '').replace('K', '00')
			
			elif 'K' in shortened:
				Placeholder2[d] = shortened.replace('K', '000') 
			
			d = d+1

		Views = (Placeholder2[indices[0]:(indices[-1]+1)*3:3])

		##print(Views)

		#####################################################
		#creates list of the views for each post
		#####################################################

		for number in numbers:
		       data = number
		       Placeholder2.append(str(data).split(">")[1].split("<")[0])
		Clicks = (Placeholder2[(indices[0]+1):(indices[-1]+1)*3:3])

		##print(Clicks)

		#####################################################
		#creates list of the clicks for each post
		#####################################################

		for number in numbers:
				data = number
				Placeholder2.append(str(data).split(">")[1].split("<")[0])
		Rxns = (Placeholder2[(indices[0]+2):(indices[-1]+1)*3:3])

		##print(Rxns)

		#####################################################
		#creates list of the Reactions for each post
		#####################################################

		with open('Facebook' + mon + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
			new_file = csv.writer(csvfile, delimiter=',')
			

			#prints out the headers for csv file
			header = "Date, Titles, Number of Views, Number of Clicks, Number of Reactions"
			X =  header.split(", ")
			#print(X)
			new_file.writerow(X)
			
			#prints the actual data into the csv file
			j = 0
			while j != len(Dates):
			
				line = (Dates[j] + ", " + Titles[j] + ", " + Views[j] + ", " + Clicks[j] + ", " + Rxns[j])
				Y = line.split(", ")
				new_file.writerow(Y)
				j += 1

		#####################################################
		#Organizes and outputs the data from the above lists into an excel readable file!.
		#####################################################

		print("Facebook Output Completed..!")
	else :
		print("Couldn't find facebook.html in the same folder as this script..!")
	if EMMAexists:
		Percent = []
		Percents = []
		FinPercs = []
		allpercent = []

		link = []
		Links = []
		FinLink = []

		
		with io.open("emma.html", "r", encoding='utf-8') as emma:
			soup2 = BeautifulSoup(emma, "html.parser")
			
		### finds the percentage of clicks for a given link.
		Percent = soup2.findAll("span", {"class":"progress-percent"})
		for l in Percent:
			allpercent.append(l.span)
		Percents = allpercent[9:]
		for i in Percents:
			#print(i)
			j = str(i).replace('</span>', '').replace('<span>', '')
			FinPercs.append(j)
		#print(FinPercs)


		### finds the link associated with a given percentage
		Links = soup2.findAll("li", {"class":"ellipsis"})
		for l in Links:
			if l.a != None:
				link.append(str(l.a).split('"')[1])
		#print(link)

		with open('Emma' + mon + '.csv', 'w', encoding='utf-8', newline='') as emmacsv:
			new_file = csv.writer(emmacsv, delimiter=',')

			header = "Percentage of Clicks, Link"
			X =  header.split(", ")
			new_file.writerow(X)

			j = 0
			while j != len(FinPercs):
			
				line = (FinPercs[j] + ", " + link[j])
				Y = line.split(", ")
				new_file.writerow(Y)
				j += 1
			print("Emma Output Completed..!")		
	else :
		print("Couldn't find emma.html in the same folder as this script..!")



	if REPXLexists :
		out = openpyxl.load_workbook(filename = "./REPORT.xlsx")
		FB_Out = out['FACEBOOK DATA ANALYSIS']

		W = []

		colA = FB_Out['A']
		for i in colA:
			if i.value != None:
				W.append(i)
				#print(i)
		first_Open = int(str((W[-1])).replace(">",'').split('.')[1][1:])+1
		print(first_Open)
		with open('Facebook' + mon + '.csv', 'r', encoding='utf-8') as FBcsv:
			count = -1
			for i in FBcsv:
				count += 1
				FBDat = i.split(",")
				if count == 0:
					bufferchar = ('A' + str(first_Open + count))
					FB_Out[bufferchar] = '#'
					
				else:
					Datecell = ('A' + str(first_Open + count))
					date = i.split(",")[0]
					FB_Out[Datecell] = date

					Titlecell = ('C' + str(first_Open + count))
					title = i.split(",")[1]
					FB_Out[Titlecell] = title

					Reachcell = ('D' + str(first_Open + count))
					reach = i.split(",")[2]
					FB_Out[Reachcell] = int(reach)

					Clickscell = ('E' + str(first_Open + count))
					click = i.split(",")[3]
					FB_Out[Clickscell] = int(click)

					Reactioncell = ('F' + str(first_Open + count))
					rxn = i.split(",")[4]
					FB_Out[Reactioncell] = int(rxn)
		FBcsv.close()	

		EM_Out = out['EMMA DATA ANALYSIS']
		W = []
		colB = EM_Out['B']
		for i in colB:
			#print(i)
			if i.value != None:
				W.append(i)
		#print(W)
		first_Open = int(str((W[-1])).replace(">",'').split('.')[1][1:])+1
		print(first_Open)

		#print(EM_Out['C146'].value)
		#month = "april"
		month = input("Input the name of the month you want to add to the spreadsheet (ex: April, May, June). ")
		with open('Emma' + mon + '.csv', 'r', encoding='utf-8') as EMcsv:
			count = -1
			for i in EMcsv:
				#print(i)
				count += 1
				EMDat = i.split(",")
				if count == 0:
					bufferchar = ('C' + str(first_Open + count))
					EM_Out[bufferchar] = '#'
				else: 
					MonName = ('B' + str(first_Open + count))
					EM_Out[MonName] = month

					PercCell = ('C' + str(first_Open + count))
					percentt = i.split(",")[0]
					EM_Out[PercCell] = (float(percentt)/100)
					#EM_Out[PercCell] = FORMAT_PERCENTAGE_00

					LinkCell = ('E' + str(first_Open + count))
					link = i.split(",")[1]
					EM_Out[LinkCell] = link

			#print(EM_Out[('C'+str(first_Open)):('C'+str(count+first_Open))])
		out.save(filename = './NEWREPORT.xlsx')
	else :
		print("Couldn't find the file Report.xlsx in the same folder as this script..!")

	d = input("Press Enter to Close Window. . .")
#main()