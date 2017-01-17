##
# @file teacher.py
# @Description
# @author Vikas MK
# @version 1.0
# @date 2017-01-17

class teacher:
  def __init__(self,name,subjectList,weeklyQuota,ClassTeacherOf):
    self.name = name
    self.weeklyQuota = weeklyQuota
    self.ClassTeacherOf = ClassTeacherOf
    self.subjectList = subjectList
