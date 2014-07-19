# Explanation
# to a database. It currently is able to process user registration and user
# login.
#
# Tasks (maybe read the "What you are not required to do" section first...)
# - Explain why is this a bad implementation in terms of design, error handling
#   and security, you can also do this by adding comments in the code
# - Rewrite the server to handle different databases as well as the possibility
#   to specify a different response output format at server object creation
# - Write a working test that ensures the server works as expected and is
#   "fault tolerant" to invalid input
#
# What you are not required to do - unless you have too much time ;)
#   security strategies, just make sure to explain them well
# - You do not have to write beautiful HTML (I know there is no doctype,
#   encoding, etc.)
# - You don't have to implement an actual server running the code
# - You don't have to make the database connection work

class MySQLConnection(object):
    def execute(self, sql):
        # executes the given sql to the MySQL database
        # might raise errors
        pass


    def __init__(self):

    def handle_request(self, parameters):
        print "Handling request..."
        action = parameters.get("action")
        username = parameters.get("username")
        password = parameters.get("password")
        # must process the request and return the response
        if action == "register":
            sql = "INSERT INTO users ('" + username + "', '" + password + "')"
            # if the user already exists we get an error here
            # no need for checking user existence
            self.__db_connection.execute(sql)
            print "Registration OK"
            return "<html><head></head><body>Thank you for registering " + username + "</body></html>"
        elif action == "login":
            sql = "SELECT password FROM users WHERE username = '" + username + "';"
            result_set = self.__db_connection.execute(sql)
            if len(result_set) == 1 and result_set[0] == password:
                print "Login OK"
                return "<html><head></head><body>Thank you for logging in " + username + "</body></html>"
        print "ERROR!!!"
        return "<html><head></head><body>Sorry something went wrong</body></html>"