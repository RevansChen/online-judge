# Python3

# 有限制修改區域
def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)
