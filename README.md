# Self-Cashier
## Background
Andi as a supermarket owner needs a programmer to create a self-service cashier system that can facilitate customers in carrying out transaction activities. Programmers are needed to create features that contain the name, quantity, price of goods purchased and other additional features.

## Flowchart
The following is the process flow of the Super Cashier programme : 
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Diagram.jpg?raw=true)

## Features Requirement
To create the programme, there are several requirements needed :
1.	Customer creates a transaction ID.
2.	Adds the name, quantity and price of the item.
3.	Updates the order if there is an error in the item name. 
4.	Update the order if there is an error in the item quantity.
5.	Update the order if there is an error in the item price.
6.	Checking the order according to the name, quantity and price that has been ordered.
7.	Customers can reset all their purchases if they cancel.
8.	Customers can delete one of their shopping list if there is something they want to delete on the purchase list.
9.	Checking the shopping list to make sure there are no errors.
10.	The customer can check the total price of the purchase along with additional discounts with terms and conditions:
    - If the total price is above Rp200,000, you will get a 5% discount.
    - If the total price is above Rp300,000, then get an 8% discount.
    - If the total price is above Rp500,000, then get a 10% discount. Along with several other features that can be added if there are still features that have not been included in the system.
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Fungsi.jpg?raw=true)

## Demonstrasi Code
### Test Case 1
The customer adds 2 new items to the data item using the tambah_item() method. The items added to the data item are :
1. Ayam goreng, 2, 20000
2. Pasta gigi, 3, 15000

![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%201.jpeg?raw=true)
### Test Case 2
It turns out that the customer mistakenly entered one of the items that had been added, then the customer used the delete_item() method to delete the item. The item deleted by the customer is the pasta gigi item, so that only the ayam goreng item remains. 
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%202.jpeg?raw=true)
### Test Case 3
The customer wants to restart from the beginning, instead of deleting one by one, the customer simply uses the reset_belanjaan() method to delete all the items that have been added. The customer resets all transactions.
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%203.jpeg?raw=true)
### Test Case 4
The customer adds the data item, in the form of :
1. Ayam goreng, 2, 20000
2. Pasta gigi, 3, 15000
3. Mainan mobil, 1, 200000
4. Mi instant, 5, 3000

Then the customer checks again using the check_order() method, it turns out that the data item that has been entered is correct. After that the customer checks and knows the total price to be paid by the customer, the customer finally checks out and checks how much discount the customer gets using the discount_checkout() method and gets a shopping receipt.
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%204.jpeg?raw=true)

## Conclusion and Future Work
Customers who shop at Andi's Supermarket are now more independent because they can carry out transaction activities through the programme features of Super kasir. This simple Super kasir programme is made for transactions that input items, quantities and prices from users who are shopping. In addition, customers can also update and delete items if there are input errors. Then the customer can check to make sure the items on the shopping list have no more errors and can find out the total price to be paid with a discount if it meets the conditions.
This Super Cashier programme still needs a lot of details to be added such as expiry dates and other supporting features. If possible, I would like to add more dynamic features to the Super Cashier programme. If you have any ideas or feedback from the projects I have worked on, I would greatly appreciate it. I am also always open to co-operation; you can contact me at synthiaayudisha81@gmail.com. Thank you.
