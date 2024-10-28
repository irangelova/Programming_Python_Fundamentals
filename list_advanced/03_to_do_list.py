to_do_list = ['0'] * 10

while True:
    to_dos = input()

    if to_dos == "End":
        break

    importance = int(to_dos.split("-")[0])
    task = to_dos.split("-")[1]

    to_do_list[importance-1] = task

to_do_list = [task for task in to_do_list if task != '0']
print(to_do_list)
