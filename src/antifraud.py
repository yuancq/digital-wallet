
import sys
import Queue

# feature1: check the friendship dict to find if a person is a friend of another person
def feature1(pathIn, pathOut, dict):

    with open(pathIn) as f_in:
        lines = f_in.readlines()

    f_out = open(pathOut, "w")

    for line in lines[1:]:
        flag = False
        data = line.split(", ")
        if len(data) != 5:
            continue
        person1 = data[1]
        person2 = data[2]
        if dict.get(person1):
            s = dict[person1]
            if person2 in s:
                flag = True
        if flag:
            f_out.write("trusted\n")
        else:
            f_out.write("unverified\n")

    f_out.close()

# feature 2: check if a person is in another person's friends set, and if is in the friend's frineds set.
def feature2(pathIn, pathOut, dict):

    with open(pathIn) as f_in:
        lines = f_in.readlines()

    f_out = open(pathOut, "w")

    for line in lines[1:]:
        flag = False
        data = line.split(", ")
        if len(data) != 5:
            continue
        person1 = data[1]
        person2 = data[2]
        if dict.get(person1):
            s = dict[person1]
            if person2 in s:
                flag = True
            else:
                for friend in s:
                    if dict.get(friend):
                        newfriend_set = dict[friend]
                        if person2 in newfriend_set:
                            flag = True
                            break
        if flag:
            f_out.write("trusted\n")
        else:
            f_out.write("unverified\n")

    f_out.close()

# feature3: check if a person is withn 4th degree friendship of another person
def feature3(pathIn, pathOut, dict):

    with open(pathIn) as f_in:
        lines = f_in.readlines()

    f_out = open(pathOut, "w")

    for line in lines[1:]:
        flag = False
        data = line.split(", ")
        if len(data) != 5:
            continue
        person1 = data[1]
        person2 = data[2]
        if friends4th(person1, person2, dict):
            flag = True

        if flag:
            f_out.write("trusted\n")
        else:
            f_out.write("unverified\n")

    f_out.close()

# use breadth first search to find friends with 4th degree
def friends4th(person1, person2, dict):
    if dict.get(person1):
        s = dict[person1]
        if person2 in s:
            return True
        else:
            q = Queue.Queue()
            visited = {}
            q.put(person1)
            visited[person1] = 0
            while not q.empty():
                currentPerson = q.get()
                if dict.get(currentPerson):
                    curP_friends = dict[currentPerson]
                    if person2 in curP_friends:
                        return True
                    else:
                        for friend in curP_friends:
                            if visited.get(friend):
                                continue
                            if visited[currentPerson] < 3:
                                q.put(friend)
                                visited[friend] = visited[currentPerson] + 1

    return False

# build a friendship dict
def readInData(path):
    dict = {}
    with open(path) as f:
        lines = f.readlines()
    for line in lines[1:]:
        data = line.split(", ")
        if len(data) != 5:
            continue
        person1 = data[1]
        person2 = data[2]
        addToDict(person1, person2, dict)
        addToDict(person2, person1, dict)
    return dict

def addToDict(person1, person2, dict):
    if dict.get(person1):
        s = dict[person1]
        s.add(person2)
        dict[person1] = s
    else:
        s = set([person2])
        dict[person1] = s


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print "wrong number of args"
        exit()

    # build a friendship dict, key is person number, value is a set of her friends
    pathIn = sys.argv[1]
    data_dict = readInData(pathIn)

    pathIn = sys.argv[2]
    pathOut = sys.argv[3]
    feature1(pathIn, pathOut, data_dict)

    pathOut = sys.argv[4]
    feature2(pathIn, pathOut, data_dict)

    pathOut = sys.argv[5]
    feature3(pathIn, pathOut, data_dict)