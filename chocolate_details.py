from mysql import connector


class Dbconnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="ajiThh**#110",
                database="chocolate_db"
            )
            return self.connection
        except Exception as e:
            return None


class Chocolate_details(Dbconnect):

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = """
            INSERT INTO chocolate_details
            (chocolate_name, brand, price, quantity, expiry_date)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connect.commit()
            print("New chocolate added successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM chocolate_details"
            self.cursor.execute(query)

            records = self.cursor.fetchall()
            return records

        except Exception as e:
            return []

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM chocolate_details WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is None:
                print("Chocolate not found..!")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:
                query = "DELETE FROM chocolate_details WHERE id = %s"
                values = (id,)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Chocolate deleted successfully..!")
            else:
                print("Chocolate not found..!")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record is not None:
                self.cursor = self.connect.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE chocolate_details SET {placeholder} WHERE id = %s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Chocolate updated successfully..!")
            else:
                print("Chocolate not found..!")

        except Exception as e:
            print(e)


connection_instance = Dbconnect()
print(connection_instance.get_connection())

chocolate_view = Chocolate_details()

chocolate_view.post(
    chocolate_name="Dairy Milk",
    brand="Cadbury",
    price="50",
    quantity="100",
    expiry_date="2027-12-31"
)

chocolate_view.get()

print("_____________________")
chocolate_view.retrieve(1)

print("-------------")
chocolate_view.delete(2)

print("-------------")
chocolate_view.get()

print("-------------")
# chocolate_view.put(1, chocolate_name="KitKat", brand="Nestle", price="40", quantity="50", expiry_date="2027-10-31")

chocolate_view.retrieve(1)