# Encapsulation is the process of making methods and data hidden inside the 
# object they relate to using modifiers such as:
# 1. Public: can be accessed from anywhere
# 2. Protected: can only be accessed from code within the same module
# 3. Private: can only be accessed from code within the same class
# 
# Accessing protected members outside of the module will not cause an error
# It just informs other develpers that they should be careful when accessing them


class Employee():
    new_id = 1
    def __init__(self, name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._id = 3  # Single underscore indicates that a member is protected
        self.__id = 5  # Double underscores indicates the member is private
    
    def say_hi(self):
        print(f"Employee id {self.__id} says Hi!")



e = Employee()
print(e.new_id)
print(e._id)
print(e._Employee__id)
e.say_hi()
print(dir(e))
# print(e.__id)  # Error occurs