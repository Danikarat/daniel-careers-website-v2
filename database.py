from sqlalchemy import create_engine

# Replace these variables with your actual database credentials
username = 'root'
password = 'danXorse24$'
host = 'your_public_ip_or_domain'
port = '3307'
database = 'danicareers'

# Create the connection string
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

# Create the engine
engine = create_engine(connection_string)

# Establish the connection
try:
    conn = engine.connect()
    print("Connection to MySQL DB successful")
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
    print("Connection closed")
