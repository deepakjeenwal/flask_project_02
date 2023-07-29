from flask import Flask,request


obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "<h1>Welcome</h1>"

@obj.route('/cal', methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    n1=request.json["n1"]
    n2=request.json["n2"]

    if operation =="add":
        result=int(n1)+int(n2)
    elif operation =="multiply":
        result=int(n1)*int(n2)
    elif operation =="division":
        result=int(n1)/int(n2)
    else:
        result=int(n1)-int(n2)
    return "The operation is {} and the result is {}".format(operation, result)


print(__name__) # not necessary, it give name of the function in terminal

if __name__== "__main__":
    obj.run(debug=True)