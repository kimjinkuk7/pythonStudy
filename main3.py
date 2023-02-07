#    0 1 234 5 678 91011
s = '제 생일은 9월 입니다.'
# print(s.find('생일은 '))

# print(s[6:7])

# pos = s.find('생일은 ')
# pos += 4

# print(s[pos:pos+2])

arr = s.split('생일은 ')
arr2 = arr[1].split('월')
print(arr2)

bd = s.split('생일은 ')[1].split('월')[0]
print(bd)