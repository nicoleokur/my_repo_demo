from student import Student

s1 = Student("Nicole", "Okur", "02553052", 2)
s2 = Student("Maddy", "Scoblick", "02553080", 9)
s3 = Student("Katelyn", "Baik", "02559087", 8)
s4 = Student("Rita", "Collins", "02556473")

print("Student Info")
print(s1)
print(s2)
print(s3)
print(s4)

print("Greetings")
s1.greeting("Hi!")
s2.greeting("Hola!")
s3.greeting("Sup!")
s4.greeting("GUYS...")

print("Energy Levels")
print(s1.fname, s1.energy_level)
print(s2.fname, s2.energy_level)
print(s3.fname, s3.energy_level)
print(s4.fname, s4.energy_level)

print("Exam Day :(")
s1.take_exam()
s2.take_exam()
s3.take_exam()
s4.take_exam()

print("New Energy Levels")
print(f"{s1.fname}: {s1.get_energy_level()}")
print(f"{s2.fname}: {s2.get_energy_level()}")
print(f"{s3.fname}: {s3.get_energy_level()}")
print(f"{s4.fname}: {s4.get_energy_level()}")