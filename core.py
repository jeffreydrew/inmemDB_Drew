class InMemoryDB:
    def __init__(self):
        # keys are strings and values are ints
        self.db = {}
        self.transactions = []
        self.in_transaction = False

    def get(self, key):
        #regarless of transaction, return the value of the key from the db
        if key in self.db:
            print("Key: " + key + " Value: " + str(self.db[key]))
            return self.db[key]
        else:
            print("Key: " + key + " Value: None")
            return None
        
    def put(self, key, value):
        # if in transaction, add the key value pair to the transaction
        if self.in_transaction:
            self.transactions.append((key, value))
            print("Key: " + key + " Value: " + str(value) + " added to transaction")
        else:
            print("No transaction in progress")

    def begin_transaction(self):
        # if in transaction, throw error
        if self.in_transaction:
            print("Transaction already in progress")
        else:
            self.in_transaction = True
            print("Transaction started")

    def commit(self):
        # if not in transaction, throw error
        if not self.in_transaction:
            print("No transaction in progress")
        else:
            # commit the transaction
            for key, value in self.transactions:
                self.db[key] = value
            self.transactions = []
            self.in_transaction = False
            print("Transaction committed")

    def rollback(self):
        # if not in transaction, throw error
        if not self.in_transaction:
            print("No transaction in progress")
        else:
            # rollback the transaction
            self.transactions = []
            self.in_transaction = False
            print("Transaction rolled back")


# if main
if __name__ == "__main__":
    inmemoryDB = InMemoryDB()
    inmemoryDB.get("A")  # should return null
    inmemoryDB.put("A", 5)  # should throw error because no transaction

    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5) # not committed
    inmemoryDB.get("A") # should return nothing because not committed
    inmemoryDB.put("A", 6) # update the value

    inmemoryDB.commit() # commit the transaction

    #get a
    inmemoryDB.get("A") # should return 6

    #commit
    inmemoryDB.commit() # should throw error because no transaction

    #rollback
    inmemoryDB.rollback() # error because no transaction

    #get b
    inmemoryDB.get("B") # should return null

    #new transaction
    inmemoryDB.begin_transaction()

    #put b
    inmemoryDB.put("B", 10)

    #rollback
    inmemoryDB.rollback()

    #get b
    inmemoryDB.get("B") # should return null


