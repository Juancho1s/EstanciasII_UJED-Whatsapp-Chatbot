import mysql.connector
from ... import config


class SectionsModel:
    """
    The function initializes a connection to a MySQL database using credentials from a configuration
    file.
    """
    def __init__(self):
        connection = config.dbCredentials
        self.connection = mysql.connector.connect(host=connection["host"], user=connection["user"], password=connection["password"], database=config["database"])
        
        
        
    """
    This function retrieves sections by name from a database and returns their IDs and names in a
    dictionary.
    
    :param sectionName: The `getSectionsByName` method you provided is a Python function that
    queries a database to retrieve sections based on the provided `sectionName`. The function
    executes a SQL query to select the `id` and `name` of sections where the name matches the input
    `sectionName`
    :type sectionName: str
    :return: The function `getSectionsByName` returns a dictionary containing the "id" and "name" of
    sections that match the provided section name. If there are matching entries found in the
    database, the function returns the dictionary with the corresponding data. If no matching
    entries are found, it prints an error message and returns `None`. If an error occurs during the
    execution of the SQL query, it prints an
    """
    def getSectionsByName(self, sectionName: str):
        query = (
            "SELECT id, name FROM sections AS sc "
            "WHERE sc.name == (%s);"
        )
        
        cursor = self.connection.cursor(buffered=True)
        try:
            #  Execute the query
            cursor.execute(query, sectionName)
            
            # Fetch all the rows
            rows = cursor.fetchall()
            # Close the cursor
            cursor.close()
            return self.fetchingData(rows)
        
        except Exception as e:
            # An error occurred while executing the query
            print(f"Error executing SQL Query: {e}")
            cursor.close()
        
        return None
            
            
    
    """
    This function retrieves all sections connected to a specified initial section from a database.
    
    :param initialSection: It is a method for retrieving all sections
    connected to an initial section from a database. The `initialSection` parameter is the name of
    the section you want to find connections for
    :type initialSection: str
    :return: a dictionary containing the "id" and "name" of sections connected to the initialSection
    provided as input. If sections are found based on the query, the function returns the dictionary
    with the section details. If no sections are found, it prints "No sections found." and returns
    None. If an error occurs during the execution of the query, it prints an error message and
    returns
    """
    def getAllSectionsConnected(self, initialSection: str):
        query = (
            "SELECT id, name FROM sections AS sc "
            "WHERE pr.section_id == ( "
            "   SELECT id FROM sections AS scFltr "
            "   WHERE prFltr.name == %s); "
        )
        
        cursor = self.connection.cursor(buffered=True)
        
        try:
            # Execute the query
            cursor.execute(query, initialSection)
            
            # Fetch all the rows
            rows = cursor.fetchall()
            # Close the cursor
            cursor.close()
            return self.fetchingData(rows)
        
        except Exception as e:
            # An error occurred while executing the query
            print(f"Error filtering sections connected to '{initialSection}': {e}")
            
            cursor.close()
            
        return None
    
    
    """
    The function `fetchingData` retrieves and organizes data from rows into a dictionary format.
    
    :param rows: The `fetchingData` function takes two parameters: `self` and `rows`. The `rows`
    parameter is expected to be a list of tuples where each tuple contains two elements - an ID and
    a name. The function then processes this data and returns a dictionary `results` with keys "
    :return: The `fetchingData` function returns a dictionary `results` containing keys "id" and
    "name" with corresponding lists of values. If there are rows provided as input, the function
    populates the lists with data from the rows and returns the results dictionary. If there are no
    rows provided, it prints "No sections found." and returns `None`.
    """
    def fetchingData(self, rows):
        results = {
                "id": [], 
                "name": []
            }
        # Check if any rows were returned by the database
        if len(rows) > 0:
                for row in rows:
                    results["id"].append(row[0])
                    results["name"].append(row[1])
                    
                return results
        else:
            # No data found matching the query
            print("No sections found.")
            
            return None