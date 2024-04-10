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
            
    
    """
    This function retrieves connected procedures based on a given section ID from a database table.
    
    :param sectionId: The `getConnectedProceduresBySection` method you provided seems to be a part
    of a class, as it takes `self` as the first parameter. This method is designed to retrieve
    information about procedures based on a given `sectionId`
    :return: The function `getConnectedProceduresBySection` returns a dictionary containing lists of
    procedure names, button names, content, and URLs that are connected to a specific section ID. If
    there are matching rows in the database for the given section ID, the function returns the
    dictionary with the corresponding data. If no matching rows are found, it prints "No sections
    found." and returns `None`. If an
    """
    def getConnectedProceduresBySection(self, sectionId: tuple):
       # Set the query statement to retrive the data from the database
        query = (
            """
            SELECT btn_name FROM procedures AS pr 
            WHERE pr.section_table_id = (%s);
            """
        )
        # Create a cursor object and execute the SQL command
        cursor = self.connection.cursor(buffered=True)
        
        try:
            # Execute the SQL command
            cursor.execute(query, sectionId)
            results = {
                "name": [],
                "btn_name": [],
                "content": [],
                "url": [],
            }
            # Fetch all the rows
            rows = cursor.fetchall()
            # For each row returned by the select statement
            if len(rows) > 0:
                for row in rows:
                    results["name"].append(row["name"])
                    results["btn_name"].append(row["btn_name"])
                    results["content"].append(row["content"])
                    results["url"].append(row["url"])
                    
                return results
            
            else:
                # No data found matching the query
                print("No procedures found.")
            
        except Exception as e:
            # An error occurred while executing the query
            print(f"Error getting connected procedures by section ID: {e}")
        
        cursor.close()
        return None
    
    
    def getDataByName(self, btnName: tuple):
        """
        The function `getDataByName` retrieves data from a database table based on a given name.
        
        :param name: The code you provided is a method that retrieves data from a database table called
        "procedures" based on the input name. It constructs and executes an SQL query to fetch the name,
        content, and URL of procedures that match the given name
        :return: The `getDataByName` method returns a dictionary containing the name, content, and URL
        of procedures that match the input name. If no procedures are found with the given name, it
        prints a message stating "No procedure found with that name." If an error occurs during the
        execution of the method, it prints an error message. In all cases, the method closes the
        database cursor before returning either the results
        """
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