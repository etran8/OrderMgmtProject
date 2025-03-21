# OrderMgmtProject
This project implement a RESTFul Web Service that consumes and produces ‘JSON’ data. The business domain model deals with Order Management and the entities are Customer, Address, Order, and Order Items.

The entities have the relationships according to the following:
1)	A Customer Object should have one or many Address Objects (OneToMany)
2)	A Customer Object should have one or many Order Objects (OneToMany)
3)	An Order Object should have one or many Order Item Objects (OneToMany)

This project develops a RESTFul Web Service that publishes the following API:
1)	AddCustomer – Creates a new Customer.
2)	GetCustomers – Returns all the customers it has in the database. Returns the objects as JSON list
3)	UpdateCustomer – Updates an existing customer
4)	AddAddress – Creates a new Address and links it with an existing Customer.
5)	UpdateAddress – Updates an existing address
6)	GetAddresses related to a Customer – Returns all the Addresses associated with a customer as a JSON list
7)	AddOrder – Creates a new Order and links it with an existing Customer
8)	UpdateOrder – Updates an existing Order
9)	GetOrders related to a Customer – Returns all the Orders associated with a customer as a JSON list
10)	AddProduct – Creates a new Product and associates it with an Order
11)	GetProducts related to an Order – Returns all the Products associated with an Order as a JSON list

To run this project, you will need to do the following:
1. Download all these codes to your local folder and open them up in PyCharm.
2. If the code is compiled without any errors then you should see this URL http://127.0.0.1:8000/
3. You may first need to go to http://127.0.0.1:8000/admin/ to sign in with User ID: eric and password: eric.
   ![image](https://github.com/user-attachments/assets/8eb5227e-343c-4560-a54c-79eeee0fd843)
4. You then go back to the home page: http://127.0.0.1:8000/home
5. You then can click on the URL links on the screen or manually enter the below URLs on the browser.
6. http://127.0.0.1:8000/AddCustomer/
7. http://127.0.0.1:8000/GetCustomers/
8. http://127.0.0.1:8000/UpdateCustomer/1  (where 1 is a customer id)
9. http://127.0.0.1:8000/AddAddress/1  (where 1 is a customer id)
10. http://127.0.0.1:8000/GetAddresses/1 (where 1 is a customer id)
11. http://127.0.0.1:8000/UpdateAddress/2 (where 2 is the address id)
12. http://127.0.0.1:8000/AddOrder/1   (where 1 is a customer id)
13. http://127.0.0.1:8000/GetOrders/1  (where 1 is a customer id)
14. http://127.0.0.1:8000/UpdateOrder/3 (where 3 is the order id)
15. http://127.0.0.1:8000/AddProduct/3 (where 3 is the order id)
16. http://127.0.0.1:8000/GetProducts/3  (where 3 is the order id)
17. 

