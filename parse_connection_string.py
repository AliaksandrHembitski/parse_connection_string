connection_string ="dialect+driver://username:password@host:port/database"


def parse_connection_string (connection_string):
    result = {"dialect": "", "driver": "", "username": "", "password": "", "host": "", "port": "", "database": ""}
    if ":///" in connection_string:
        connection_string=connection_string.split(":///")
        result["dialect"]=connection_string[0]
        result["database"]=connection_string[1]

    elif "://" in connection_string and "+" in connection_string:
        connection_string=connection_string.split("://")
        for i in range(len(connection_string)):
            if "+" in connection_string[i]:
                result["dialect"]=connection_string[i].split("+")[0]
                result["driver"]= connection_string[i].split("+")[1]
            elif connection_string[i].count(":")==2:
                connection_string=connection_string[i].split("@")
                result["username"]=connection_string[0].split(":")[0]
                result["password"]=connection_string[0].split(":")[1]
                result["host"]=connection_string[1].split(":")[0]
                result["port"]=connection_string[1].split(":")[1].split("/")[0]
                result["database"]=connection_string[1].split(":")[1].split("/")[1]
            elif connection_string[i].count(":")==1:
                connection_string = connection_string[i].split("@")
                result["username"] = connection_string[0].split(":")[0]
                result["password"] = connection_string[0].split(":")[1]
                result["host"] = connection_string[1].split(":")[0].split("/")[0]
                result["database"] = connection_string[1].split(":")[0].split("/")[1]
    elif "://" in connection_string:
        connection_string=connection_string.split("://")
        result["dialect"]=connection_string[0]
        result["username"]=connection_string[1].split("/")[0].split(":")[0]
        result["password"]=connection_string[1].split("/")[0].split(":")[1]
        result["database"]=connection_string[1].split("/")[1]

    return result
print(parse_connection_string(connection_string))

