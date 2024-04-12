import mysql.connector
import config


class SectionsModel:
    """
    The function initializes a connection to a MySQL database using credentials from a configuration
    file.
    """
    def __init__(self):
        connection = config.dbCredentials
        self.connection = mysql.connector.connect(host=connection["host"], user=connection["user"], password=connection["password"], database=connection["database"])
        
        
        
   
    def getSectionsByName(self, sectionName: list):
        query = (
            """
            SELECT id, name FROM sections AS sc 
            WHERE sc.name == (%s);
            """
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
            
            
    
    def getAllSectionsConnected(self, initialSectionName: list):
        
        query = (
            """
            SELECT id, name FROM sections AS sc 
            WHERE sc.section_id = (
                SELECT id FROM sections AS scFltr
                WHERE scFltr.name = (%s)
            );
            """
        )
        
        cursor = self.connection.cursor(buffered=True)
        
        try:
            # Execute the query
            cursor.execute(query, initialSectionName)
            results = {
                "id": [],
                "name": []
            }
            
            # Fetch all the rows
            rows = cursor.fetchall()
            for row in rows:
                results["id"].append(row[0])
                results["name"].append(row[1])
            
            # Close the cursor
            cursor.close()
            return results
        
        except Exception as e:
            # An error occurred while executing the query
            print(f"Error filtering sections connected to '{initialSectionName}': {e}")
            
            cursor.close()
            
        return None
    
    

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