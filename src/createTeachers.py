from teacher import teacher

subjectList=[ "Maths","Chemistry","Physics"]

teachers=[]
teachers.append(teacher("Suresh",subjectList,10,10))

print teachers[0].name
print teachers[0].weeklyQuota
print teachers[0].ClassTeacherOf
print teachers[0].subjectList

