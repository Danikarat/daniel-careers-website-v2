from sqlalchemy import create_engine, text

# Replace these variables with your actual database credentials
username = 'root'
password = 'danXorse24$'
host = 'localhost'
port = '3307'  # usually 3306 for MySQL
database = 'danicareers'

# Create the connection string
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

# Create the engine
engine = create_engine(connection_string)

# Establish the connection
conn = engine.connect()

# Now you can use 'conn' to interact with the database
with conn:
    result = conn.execute(text("select * from jobs"))
    print("type(result):", type(result))
    result_all = result.fetchall()
    print("type(result_all):", type(result_all))
    first_result = result_all[0]
    print("type(first_result):", type(first_result))

    # Convert the first result row to a dictionary using items()
    first_result_dict = {key: value for key, value in first_result.items()}
    print("type(first_result_dict):", type(first_result_dict))
    print(first_result_dict)
