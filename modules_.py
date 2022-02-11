import time
from os import listdir, path


def folders_(folder):
    """

    :param folder:
    :return: list of folders till 10 nested folders
    """
    folders_list = []
    folders_dict = {}

    def listdir_(dir):
        filenames = listdir(dir)
        return filenames

    lis_1 = listdir_(folder)

    for i1 in lis_1:  # 1
        path1 = path.join(folder, i1)
        if path.isdir(path1):
            folders_list.append(i1)
            folders_dict[i1] = path1

            lis_2 = listdir_(path1)  # 2
            for i2 in lis_2:
                path2 = path.join(path1, i2)
                if path.isdir(path2):
                    folders_list.append(i2)
                    folders_dict[i2] = path2

                    lis_3 = listdir_(path2)  # 3
                    for i3 in lis_3:
                        path3 = path.join(path2, i3)
                        if path.isdir(path3):
                            folders_list.append(i3)
                            folders_dict[i3] = path3

                            lis_4 = listdir_(path3)  # 4
                            for i4 in lis_4:
                                path4 = path.join(path3, i4)
                                if path.isdir(path4):
                                    folders_list.append(i4)
                                    folders_dict[i4] = path4

                                    lis_5 = listdir_(path4)  # 5
                                    for i5 in lis_5:
                                        path5 = path.join(path4, i5)
                                        if path.isdir(path5):
                                            folders_list.append(i5)
                                            folders_dict[i5] = path5

                                            lis_6 = listdir_(path5)  # 6
                                            for i6 in lis_6:
                                                path6 = path.join(path5, i6)
                                                if path.isdir(path6):
                                                    folders_list.append(i6)
                                                    folders_dict[i6] = path6

                                                    lis_7 = listdir_(path6)  # 7
                                                    for i7 in lis_7:
                                                        path7 = path.join(path6, i7)
                                                        if path.isdir(path7):
                                                            folders_list.append(i7)
                                                            folders_dict[i7] = path7

                                                            lis_8 = listdir_(path7)  # 8
                                                            for i8 in lis_8:
                                                                path8 = path.join(path7, i8)
                                                                if path.isdir(path8):
                                                                    folders_list.append(i8)
                                                                    folders_dict[i8] = path8

                                                                    lis_9 = listdir_(path8)  # 9
                                                                    for i9 in lis_9:
                                                                        path9 = path.join(path8, i9)
                                                                        if path.isdir(path9):
                                                                            folders_list.append(i9)
                                                                            folders_dict[i9] = path9

                                                                            lis_10 = listdir_(path9)  # 10
                                                                            for i10 in lis_10:
                                                                                path10 = path.join(path9, i10)
                                                                                if path.isdir(path10):
                                                                                    folders_list.append(i10)
                                                                                    folders_dict[i10] = path10

    return folders_list, folders_dict


