"""
문제에서 언제? 어떻게 써야하는지가 중요함
파이썬 여러줄 주석?

기말고사 시험 성적 저장
리스트[]로 저장하면 수학과 영어 점수인지 알기 쉽지 않다.
따라서 위와 같은 경우에 딕셔너리{} 를 사용한는 것이 유용하다.
"""

score = {
    'math': 97,
    'eng' : 49,
    'kor' : 89,
}
# 값이 중복되는 것은 관계없지만 key값은 유일해야한다

print(score['math'])
score['math'] = 45
print(score['math'])

# key를 추가하여 초기화하면 접근이 가능하다.
score['sci'] = 100
print(score['sci'])

"""
존재하지 않는 key에 접근시 key error 발생한다.
score['music']
in을 통해서 딕셔너리에 key 가 존재하는지 검사 O(1)
위 방법을 통해서 music key가 있는지 없는지 알 수 있다.
탐색이 시간복잡도가 O(1) 이기에 코딩테스트에 많이 활용됨
시간복잡도를 줄이기에 메모리를 사용한다
"""
if 'music' in score:
    print(score['music'])
else:
    score['music'] = 0
    
