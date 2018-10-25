# Python3

# 有限制修改區域
def correctScholarships(bestStudents, scholarships, allStudents):
    return (set(scholarships) != set(allStudents)) and set(scholarships).union(bestStudents).issubset(set(allStudents)) and set(bestStudents).issubset(set(scholarships))
