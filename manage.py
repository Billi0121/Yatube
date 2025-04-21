global_variable = 'Hello'

def some_fun(passed_variable):
    local_variable = 'Andrey'

    def local_fun_variable():
        locla_inside_variable = 'DOING'
        return(f'{global_variable} '
               f'{local_variable} '
               f'{passed_variable} '
               f'{locla_inside_variable}')
    return local_fun_variable

some = some_fun('HOw ARE YOU')
print(some())

