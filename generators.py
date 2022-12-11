# Practice writing generators

def course_generator():
    yield 'Computer Science'
    yield 'Art'
    yield 'Business'

# courses = course_generator()
# for course in courses:
#    print(course)

def prize_generator():
    student_info = {
        "Joan Stark": 355,
        "Billy Mars": 45,
        "Tori Rivers": 18,
        "Kyle Newman": 25
    }
    print('starting')

    for student in student_info:
        print('looping..')
        name = student
        id = student_info[name]

        if id % 3 == 0 and id % 5 == 0:
            yield student + " gets prize C"
        elif id % 3 == 0:
            yield student + " gets prize A"
        elif id % 5 == 0:
            yield student + " gets prize B"


# prizes = prize_generator()
# for prize in prizes:
#    print(prize)


def generator():
    count = 0
    print('starting')
    while True:
        print('before yield')
        n = yield count
        print('continuing after yield...')
        if n is not None:
            count = n

        count += 1


my_generator = generator()

print('first iteration')
print(next(my_generator))
print('second iteration')
print(next(my_generator))
print('third iteration')
print(my_generator.send(3))
print('fourth iteration')
print(next(my_generator))