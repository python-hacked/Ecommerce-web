def my_decorater(func):
    def wrappe():
        print("this is a python")
        func()
        print("this is a java")

    return wrappe    

@my_decorater
def show_detials():
    print("hellow")

show_detials()            