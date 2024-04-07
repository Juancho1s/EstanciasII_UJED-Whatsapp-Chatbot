import mysql.connector
from ... import config


class ProceduresModel:
    """
    The function initializes a connection to a MySQL database using credentials from a configuration
    file.
    """
    def __init__(self):
            connection = config.dbCredentials
            self.connection = mysql.connector.connect(host=connection["host"], user=connection["user"], password=connection["password"], database=config["database"])
            
    
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
    def getConnectedProceduresBySection(self, sectionId):
       # Set the query statement to retrive the data from the database
        query = (
            "SELECT name, btn_name, content, url FROM procedures AS pr "
            "WHERE id == (%s);"
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
                print("No sections found.")
                
                return None
            
        except Exception as e:
            # An error occurred while executing the query
            print(f"Error getting connected procedures by section ID: {e}")
        
        return None