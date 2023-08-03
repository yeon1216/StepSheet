class Member:
    id: int
    name: str
    state: int
    age: int
    join_date: str

    def __init__(self, id, name, state, join_date, age):
        self.id = id
        self.name = name
        self.state = state
        self.join_date = join_date
        self.age = age

    def print(self):
        # print("name : " + self.name + ", state : " + str(self.state) + ", age : " + str(self.age) + ", join_date : " + self.join_date)
        print(str(self.id) + ". " + self.name + ", 나이 : " + str(self.age) + ", 가입일자 : " + self.join_date)
