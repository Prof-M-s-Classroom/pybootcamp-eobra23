class CrewMember:

    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience  # Years of experience

    def __str__(self):
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"

class CrewRoster:

    def __init__(self):
        self.crew = []  # List of CrewMember objects

    def add_member(self, name, role, experience):
        newmember = CrewMember(name, role, experience)
        self.crew.append(newmember)
        """Creates a new crew member and adds to roster."""


    def remove_member(self, name):
        for name in self.crew:
            if name.name != name:
                self.crew.remove(name)
        """Removes a crew member by name."""


    def list_crew(self):
        for crewmember in self.crew:
            print(crewmember)
        """Prints all crew members."""


# === TEST CODE ===

roster=CrewRoster() #Empty Crew roster created

    # TODO: Uncomment and implement methods
roster.add_member("Alice", "Engineer", 5)
roster.add_member("Bob", "Pilot", 10)
roster.list_crew()

roster.remove_member("Alice")
roster.list_crew()
