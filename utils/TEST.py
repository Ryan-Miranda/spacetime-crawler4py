from simhash import Simhash

print(Simhash('this is a test').distance(Simhash('this is a tas')))
print(Simhash('this is a test').distance(Simhash('fuck you')))
print(Simhash('aa').distance(Simhash('bb')))
print(Simhash('aa').distance(Simhash('aa')))

