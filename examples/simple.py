import yuri

@yuri.task
def foo_bar_task(_args):
    """This task lists files in the current working folder
    """
    files = yuri.do.files_list()

    for file in files:
        yuri.do.log_print(file)

@yuri.task
def foo_baz_task(_args):
    """
    Lists images in a given folder
    """

    folder = yuri.do.get_input("Enter a folder to check if there are some pics: ")

    yuri.do.cd(folder)

    pics = yuri.do.filter(yuri.do.files_list(), ['.jpg', '.jpeg', '.png'])

    for pic in pics:
        yuri.do.log_print(pic)

if __name__ == '__main__':
    yuri.run()