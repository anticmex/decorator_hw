import time
import pathlib


def logger(old_function):
    def new_function(*callable_args):

        result = old_function(*callable_args)
        log_start_time = time.strftime("%d-%m-%Y, %H:%M:%S", time.localtime())

        if len(callable_args) == 1:
            old_function_args = callable_args[0]
        else:
            old_function_args = callable_args

        with open('Log.txt', 'a') as f:
            f.write(f'Время вызова - [{log_start_time}] \n')
            f.write(f'Вызываемая функция - [{old_function.__name__}] \n')
            f.write(f'Указанные аргументы - [{old_function_args}]-[{type(old_function_args)}] \n')
            f.write(f'Результат выполнения функции - [{result}]-[{type(result)}] \n')
            f.write(f'Путь к вызванному файлу - [{pathlib.Path.cwd()}] \n')
            f.write('\n')

        return result

    return new_function


@logger
def sting_to_int_convertor(*args):

    if len(args) > 1:

        new_arg_tuple_list = []
        for arg in args:
            new_arg_tuple_list.append(int(arg))
        return tuple(new_arg_tuple_list)
    else:

        return int(args[0])




print(sting_to_int_convertor('5'))
#print(type(sting_to_int_convertor('5', '6')[0]))
