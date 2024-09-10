# Sample Python code to demonstrate a security vulnerability (hard-coded credentials)

def connect_to_database():
    # Hard-coded credentials for database connection
    username = "admin"
    password = "password123"  # This line is a security vulnerability

    # Simulated database connection code
    print(f"Connecting to the database with username: {username} and password: {password}")

if __name__ == "__main__":
    connect_to_database()
