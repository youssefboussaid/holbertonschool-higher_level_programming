#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = []
    for i in range(0, list_length):
        try:
            l.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            l.append(0)
        except ZeroDivisionError:
            print("division by 0")
            l.append(0)
        except IndexError:
            print("out of range")
            l.append(0)
        finally:
            pass
        return l
