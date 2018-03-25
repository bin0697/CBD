#Connect to database
import psycopg2
import sys
con = psycopg2.connect(database="postgres", user = "postgres", password = "son", host = "35.194.253.36", port = "5432")
print("Opened database successfully")

#items table (Item_Id, Item_Name, Description, Start_Time, User_Id)
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS items CASCADE ")
cur.execute("CREATE TABLE items( Item_Id SERIAL PRIMARY KEY NOT NULL,Item_Name TEXT NOT NULL, Description TEXT NOT NULL, Start_Time TIMESTAMP WITHOUT TIME ZONE, User_Id INTEGER NOT NULL, FOREIGN KEY(User_Id) REFERENCES users); ")


#user table (User_Id, Username, Password)
cur.execute("DROP TABLE IF EXISTS users CASCADE ")
cur.execute("CREATE TABLE users( User_Id SERIAL PRIMARY KEY NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL); ")


#bid table (Bid_Id, Price, User_Id, Item_Id)
cur.execute("DROP TABLE IF EXISTS bid ")
cur.execute("CREATE TABLE bid( Bid_Id SERIAL PRIMARY KEY NOT NULL, Price NUMERIC NOT NULL,User_Id INT NOT NULL, FOREIGN KEY(User_Id) REFERENCES users(User_ID),Item_Id INT NOT NULL, FOREIGN KEY(Item_Id) REFERENCES items(Item_Id)); ")


#add 3 user to database
cur.execute("INSERT INTO users (Username, Password) VALUES ( 'u1', 'u1'), ( 'u2', 'u2'), ('u3', 'u3')")


#add Baseball to bid
cur.execute("INSERT INTO items VALUES (1, 'Baseball', 'good status', TIMESTAMP '2015-05-18 15:02:11', 1)")

#add 2 bid for each user
#user1
cur.execute("INSERT INTO bid (Price, User_Id, Item_Id) VALUES (10, 1, 1)")
cur.execute("INSERT INTO bid (Price, User_Id, Item_Id) VALUES (12, 1, 1)")
#user2
cur.execute("INSERT INTO bid (Price, User_Id, Item_Id) VALUES (8, 2, 1)")
cur.execute("INSERT INTO bid (Price, User_Id, Item_Id) VALUES (10, 2, 1)")
#user3
cur.execute("INSERT INTO bid (Price, User_Id, Item_Id) VALUES (3, 3, 1)")
cur.execute("INSERT INTO bid (Price, User_Id, Item_Id) VALUES (15, 3, 1)")


#print out the max bid
cur.execute("SELECT * FROM bid WHERE Price = (select max(Price) FROM bid)")
while True:
    row = cur.fetchone()
    if row == None:
         break
    print("Bid_Id: " + str(row[0]) + "\t\tPrice: " + str(row[1]) + "\t\tUser_Id: " + str(row[2]))

con.close()