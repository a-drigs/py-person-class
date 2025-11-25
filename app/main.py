class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for pers in people:
        person = Person(pers["name"], pers["age"])
        result.append(person)
    for pers in people:
        person = Person.people[pers["name"]]
        if pers.get("wife"):
            person.wife = Person.people[pers["wife"]]
        if pers.get("husband"):
            person.husband = Person.people[pers["husband"]]

    return result
