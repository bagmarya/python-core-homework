a = (1, 2, 3)
b = (4, 5, 6)

def cross_join(employees, departments):
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """
    return ((emp, dep) for emp in employees for dep in departments)

# if __name__ == '__main__':
#     c = ((x, y) for x in a for y in b)
#     print(next(c))
#     print(next(c))
#     print(next(c))
#     print(next(c))
#     print(next(c))
#     print(list(c))
