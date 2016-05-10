class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember: {})'.format(self.name)

	def tell(self):
		print 'Name:"{}" Age:"{}"'.format(self.name, self.age)

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print '(Initialized Teacher: {})'.format(self.name)

	def tell(self):
		print 'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print '(Initialized Student: {})'.format(self.name)

	def tell(self):
		print 'Marks: "{:d}"'.format(self.marks)

t = Teacher('buri',30,3000)
s = Student('yu',10,100)

print

members= [t,s]
for member in members:
	member.tell()

