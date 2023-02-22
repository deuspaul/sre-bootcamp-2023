# These functions need to be implemented
import mysql.connector
import jwt
import hashlib

MYSQL_HOST ="sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com"
MYSQL_USER ="secret"
MYSQL_PASSWORD ="jOdznoyH6swQB9sTGdLUeeSrtejWkcw"
MYSQL_DB = "bootcamp_tht"



class Token:

    def generate_token(self, username, password):
        
        try:
            print("methodsez:"+username)
        
            #dataBase = mysql.connector.connect(
                #host="sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com",
                #user ="secret",
                #password ="jOdznoyH6swQB9sTGdLUeeSrtejWkcw",
                #db = "bootcamp_tht"
                #)
            dataBase = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
            print(dataBase)
            cursorObject = dataBase.cursor()
            #query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            #issue here is that password is encrypted...
            query = f"SELECT * FROM users WHERE username='{username}'"
            #query = f"SELECT * FROM users"
            cursorObject.execute(query)
            results = cursorObject.fetchone()


            print("methodsez:"+password)
            password_salt = password + results[2]
            print("password plus salt: " + password_salt)
            saltedPwd = hashlib.sha512(password_salt.encode()).hexdigest()
            print("hashed salty pwd: " + saltedPwd)


            
            if saltedPwd == results[1] :
                print("User authenticated successfully! " + results[0] + " hash: " + results[1] + " role: " + results[3])
                #create jwt token with role, secret and algorithm
                payload = {'role': results[3]}
                token = jwt.encode(payload, 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW', algorithm='HS256')
                #return ("User authenticated successfully!" + results[0] + results[1] + results[2])
                return token

        except Exception as e:
            return ("Error authenticating user!")
        #return 'test'
        #if username & pwd = correct, 
            #generate a token with the necessary secret and return it
       # else:
            #return ("permission denied")



class Restricted:

    def access_data(self, authorization):
        return 'test'
