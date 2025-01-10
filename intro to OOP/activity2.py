class Employee:
    def __del__(self):
        print('deleted')
    def create_obj():
        obj = Employee()
        return obj
    obj = create_obj()
