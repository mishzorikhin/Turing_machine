"""
    q1      q2
0  >> q1

1  0 >> q1

_  << *

q1 q2 State
>> right
<< left
* stop machine

q
[q1],[q2]:

q1 = [A >> q1]



command
1.символ из алфавита A;
2.направление перемещения: >> (вправо), << (влево) или . (на месте);
3.новое состояние автомата

"""

A = ["1", "0", "1", "0", "1", "1", "_"]

alphabet = ['1', '0', '_']

startingPosition = 0

q1 = {
    '1': "0 > q1",
    '0': "0 > q1",
    '_': ". q0"
    }


def parsingState():
    global q1

    for i in alphabet:
        print(q1[i].split(" "))


#command = q1[str(step[1])].split(" ")


def start(Pos):
    for i in range(len(A)):
        print(i,":" , *A)
        command = q1[str(A[Pos])].split(" ")
        A[Pos] = command[0]
        if command[1] == ">":
            Pos += 1


#parsingState()

print("start", *A)
start(startingPosition)
print("end", *A)