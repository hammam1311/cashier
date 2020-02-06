def main():
	# write code here
	list=[]
	while True :
		item = input("item (enter -done- when finished): ")
		if item == "done":
			break
		price = input("price : ")
		q = input("quantity : ")
		list.append({"item":item , "price":price ,"q":q})
		continue
	total=0
	for x in list :

		i1 = x["item"]
		q1 = x["q"]
		p1 = x["price"]
		print (str(q1) +" "+ str(i1) +" "+ str(int(p1)*int(q1))+" JD ")
		total += int(p1)*int(q1)
		
	print ("Total Price: "+ str(total))

if __name__ == '__main__':
	main()
