import mysql.connector
import config


class ProceduresModel:
    """
    The function initializes a connection to a MySQL database using credentials from a configuration
    file.
    """
    
    connection = None
    
    def __init__(self):
            connection = config.dbCredentials
            self.connection = mysql.connector.connect(host=connection["host"], user=connection["user"], password=connection["password"], database=connection["database"])
            
    

    def getConnectedProceduresBySection(self, sectionId: list):
       # Set the query statement to retrive the data from the database
        query = (
            """
            SELECT id, btn_name FROM procedures AS pr 
            WHERE pr.section_table_id = (%s);
            """
        )
        # Create a cursor object and execute the SQL command
        cursor = self.connection.cursor(buffered=True)
        
        try:
            # Execute the SQL command
            cursor.execute(query, sectionId)
            results = {
                "id": [],
                "name": []
            }
            # Fetch all the rows
            rows = cursor.fetchall()
            # For each row returned by the select statement
            if len(rows) > 0:
                for row in rows:
                    results["id"].append(row[0])
                    results["name"].append(row[1])
                    
                return results
            
            else:
                # No data found matching the query
                print("No procedures found.")
            
        except Exception as e:
            # An error occurred while executing the query
            print(f"Error getting connected procedures by section ID: {e}")
        
        cursor.close()
        return None
    
    
    def getDataByName(self, btnName: list):
        # Define the SQL command to be executed
        query = (
            "SELECT name, content, url FROM procedures "
            "WHERE btn_name = %s;"
        )
        # Create a new cursor object using the connection
        cursor = self.connection.cursor()
        
        try:
            # Execute the query
            cursor.execute(query, btnName)
            results = {
                "name": [],
                "content": [],
                "url": []
            }
            # Fetch all the returned rows
            rows = cursor.fetchall()
            if len(rows) > 0:
                for row in rows:
                    results["name"].append(row[0])
                    results["content"].append(row[1])
                    results["url"].append(row[2])
                # Close the database cursor and return the results
                cursor.close()
                return  results
            
            else:
                print("No procedure found with that name.")
            
        except Exception as e:
            print(f"An error occurred when trying to retrieve data by name: {e}")
        
        cursor.close()
        return None