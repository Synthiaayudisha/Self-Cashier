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
The customer adds 2 new items to the item list using the tambah_item() method. The items added to the shopping list are :
    - Ayam goreng, 2, 20000
    - Pasta gigi, 3, 15000
    
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%201.jpeg?raw=true)
### Test Case 2
It turns out that the customer mistakenly entered one of the items that had been added, then the customer used the delete_item() method to delete the item. The item deleted by the customer is the toothpaste item, so that only the fried chicken item remains. 
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%202.jpeg?raw=true)
### Test Case 3
The customer wants to restart from the beginning, instead of deleting one by one, the customer simply uses the reset_belanjaan() method to delete all the items that have been added. The customer resets all transactions.
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%203.jpeg?raw=true)

### Test Case 4
The customer adds the shopping list, in the form of :
    - Ayam goreng, 2, 20000
    - Pasta gigi, 3, 15000
    - Mainan mobil, 1, 200000
    - Mi instant, 5, 3000
Then the customer checks again using the check_order() method, it turns out that the shopping list that has been entered is correct. After that the customer checks and knows the total price to be paid by the customer, the customer finally checks out and checks how much discount the customer gets using the discount_checkout() method and gets a shopping receipt.
![alt text](https://github.com/Synthiaayudisha/Self-Cashier/blob/main/image/Test%20Case%204.jpeg?raw=true)

## Conclusion and Future Work
