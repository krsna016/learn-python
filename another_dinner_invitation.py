guests = ["Anurag","Pareek","Krsna"]
print("Hello, "+guests[0]+" .You are invited for the dinner")
print("Hello, "+guests[1]+" .You are invited for the dinner")
print("Hello, "+guests[2]+" .You are invited for the dinner")
print(guests[1]+" cannot come to the dinner.")
print("Inplace we are inviting \"Mr. Rohan\" for the dinner.")
guests[1] = "Rohan"
print(guests[1]+" .You are invited for the dinner, tonight.")
print(guests[0]+" .You are invited for the dinner, tonight.")
print(guests[2]+" .You are invited for the dinner, tonight.")
print("Now we are having a big dinning table. We would like to invite the following three more guests :\n1.Mr Rohit\n2.Mr Sohan\n3.Mr Sujit")
guests.insert(0,"Mr Rohit")
guests.insert(2,"Mr Sohan")
guests.append("Mr sujit")
print(guests[0]+", you are invited for the dinner tonight.")
print(guests[1]+", you are invited for the dinner tonight.")
print(guests[2]+", you are invited for the dinner tonight.")
print(guests[3]+", you are invited for the dinner tonight.")
print(guests[4]+", you are invited for the dinner tonight.")
print(guests[5]+", you are invited for the dinner tonight.")


