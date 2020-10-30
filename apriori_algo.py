import itertools
import time
from decimal import Decimal

def associationRule(finalSupportList,listCount):
	count = 0
	for ele in finalSupportList:
		eleSupport = listCount[finalSupportList.index(ele)]
		for item in finalSupportList:
			if ((len(item) == len(ele) - 1) and set(item).issubset(ele)):
				itemSupport = listCount[finalSupportList.index(item)]
				confidence = eleSupport / itemSupport * 100
				if confidence >= conf:
					if ele > item:
						count += 1
						print(' , '.join(str(x) for x in item)+' ------> '+' , '.join(str(e) for e in set(ele)-set(item))+'\tSupport:'+ str(round(Decimal(eleSupport/len(transaction)*100), 1))+'%\tConfidence:'+str(round(Decimal(confidence), 1))+' %')
	if count == 0:
		print ("No Association Rules formed.")

def stage1(listOfItem,listOfTransaction,minSup):
	itemset = []
	itemDict = {}
	stage1List = []
	for t in listOfTransaction:
		 for j in t:
		 	itemset.append(j)
	for i in itemset:
		itemDict[i] = itemset.count(i)
	print('Stage_1 Items with number of occurance:')
	for x,y in itemDict.items():
		print(str(x)+'\t\t'+str(y))
		if y >= minSup:
			finalList.append(x)
			finalListCount.append(y)
			stage1List.append(x)
	return stage1List

def countItemset(rtransaction,itemSet):
	count = 0
	for trans in rtransaction:
		flag = True
		for item in itemSet:
			if item not in trans:
	 			flag = False
	 			break
		if flag:
	 		count += 1
	return count

def freqItemsetGen(listOfItem,listOfTransaction,minSup):
	nextStageItem = []
	for item in listOfItem:
		occurence = countItemset(listOfTransaction,item)
		if occurence >= minSup:
			finalList.append(item)
			finalListCount.append(occurence)
			nextStageItem.append(item)
	return nextStageItem


def combineItems(itemSet,length):
	if length == 0:
		return [[]]

	comboItems = []
	for i in range(0,len(itemSet)):
		temp = itemSet[i]
		remItem = itemSet[i+1:]
		if remItem == [[]]:
		 	return [[]]
		for item in combineItems(remItem,length-1):
			comboItems.append([temp]+item)
	return comboItems




fn = str(input('Enter the dataset file name: '))
sup = float(input('Enter minimum support (in %):'))
conf = float(input('Enter minimum confidence (in %):'))
# --- Loading Data ---
start_time = time.time()
fileObj = open(fn,'r')
transaction = []
items = []

print("Transactions in dataset:\n")
for l in fileObj:
	print(l)
	line = l.split(' ')
	records = line[1].rstrip('\n').split(',')
	transaction.append(records)
	for i in records:
		if i not in items:
			items.append(i)

print('Unique items : ')
counter = 1
for x in items:
	print(counter,' ',x)
	counter+=1

min_support = sup * len(transaction) / 100
finalList = []
finalListCount = []

freqItems = stage1(items,transaction,min_support)

#--- Stage 2 ---
for i in range(2,len(items)+1):
	if len(freqItems) < 2:
		break
	stageItemset = combineItems(items,i)
	freqItems = freqItemsetGen(stageItemset,transaction,min_support)


print('\n\n*********  Association Rules  *********')
associationRule(finalList,finalListCount)
print("\n********* Time taken to calculate the Association Rules is %s seconds *********\n" % (time.time() - start_time))


