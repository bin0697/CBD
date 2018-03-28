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


#bid table (Bid_Id, Price, Item_Id)
cur.execute("DROP TABLE IF EXISTS bid ")
cur.execute("CREATE TABLE bid( Bid_Id SERIAL PRIMARY KEY NOT NULL, Price NUMERIC NOT NULL,Item_Id INT NOT NULL, FOREIGN KEY(Item_Id) REFERENCES items(Item_Id)); ")

#user_bid table (Bid_Id, User_Id)
cur.execute("DROP TABLE IF EXISTS user_bid ")
cur.execute("CREATE TABLE user_bid( Bid_Id INT, User_Id INT, PRIMARY KEY(User_Id,Bid_Id) , FOREIGN KEY(Bid_Id) REFERENCES bid(Bid_Id) ,FOREIGN KEY(User_Id) REFERENCES users(User_ID)); ")


#add 3 user to database
cur.execute("INSERT INTO users (Username, Password) VALUES ( 'u1', 'u1'), ( 'u2', 'u2'), ('u3', 'u3')")


#add Baseball to bid
cur.execute("INSERT INTO items VALUES (1, 'Baseball', 'good status', TIMESTAMP '2015-05-18 15:02:11', 1)")

#add 2 bid for each user
#user2
cur.execute("INSERT INTO bid (Price, Item_Id) VALUES (8, 1)")
cur.execute("INSERT INTO user_bid (Bid_Id, User_Id) VALUES (1, 2)")
cur.execute("INSERT INTO bid (Price, Item_Id) VALUES (10, 1)")
cur.execute("INSERT INTO user_bid (Bid_Id, User_Id) VALUES (2, 2)")
#user3
cur.execute("INSERT INTO bid (Price, Item_Id) VALUES (3, 1)")
cur.execute("INSERT INTO user_bid (Bid_Id, User_Id) VALUES (3, 3)")
cur.execute("INSERT INTO bid (Price, Item_Id) VALUES (15, 1)")
cur.execute("INSERT INTO user_bid (Bid_Id, User_Id) VALUES (4, 3)")


#print out the max bid
cur.execute("SELECT * FROM bid WHERE Price = (select max(Price) FROM bid)")
while True:
    row = cur.fetchone()
    if row == None:
         break
    print("Bid_Id: " + str(row[0]) + "\t\tPrice: " + str(row[1]))

con.close()