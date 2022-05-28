class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score) :
        self.name = str(name)
        self.age = int(age)
        self.track = track
        self.score = float(score)

        def change_name(self, new_name):
            return new_name

        def change_age(self, new_age):
            return int(new_age)

        def add_tack(self, new_track):
            return new_track

        def get_score(self):
            return self.score
        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print (Bob.change_name("Peter"))
print (Bob.change_age(34))
print (Bob.add_track("UI/UX"))
print (Bob.get_score())
