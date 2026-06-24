#Path Parameters -> used to chage dynamic values
# it will change values based on values given in the url.Dynamically changing values in the url is called path parameters.
#Real use case of path parameters is when we want to get user details based on user id. In this case user id will be dynamic value which will be passed in the url and based on that we will get user details.
from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int): #Automatic Validation of path parameters is done by fastapi. If we give string value in the url it will give error because we have defined user_id as int.
    return {"user_id": user_id}