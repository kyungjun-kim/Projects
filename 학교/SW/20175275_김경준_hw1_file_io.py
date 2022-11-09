def process(filename):
    with open(filename, "r") as f : #특정한 파일을 읽기 모드로 읽음
        # 각 문자의 빈도수를 추출하기 위하여 사전 데이터를 만들어주자
        # dict는 key와 value, 키와 값으로 구성되어 있기 때문에
        # 키 : 알파벳, 값 : 빈도수
        dict = {}
        data = f.read()
        
        for i in data : # 각 문자열을 방문하면서 하나씩 체크한다.
            if i in data: #자료형에 키로 문자 알파벳이 포함되어 있다면
                dict[i] += 1 #빈도수를 1씩 증가, 특정한 알파벳이 여러 번 나오는 경우, 1씩 증가
            else :
                dict[i] = 1 #그렇지 않으면 1로 설정, 특정한 알파벳을 처음 발견했을 경우
    return dict
    
    
dict = process("input1.txt")

# 빈도수를 기준으로 내림차순 정렬을 수행

dict = sorted(dict.items(), key=lambda a:a[1], reverse = True)

# a = {'H': 2} a[0]='H', a[1] = 2가 들어가 있는 상황이다.
# dict.items()는 키와 값(빈도수)을 갖는 한 개의 쌍이다.
# 이 때 정렬 기준은 dict.items()에서 얻은 a라는 키와 값의 쌍에서 a[0]는 키를 의미하고
# a[1]은 값(빈도수)을 의미한다.
# reverse = True는 값(빈도수)을 내림차순 정렬

print(dict)

#dict는 가장 많은 빈도수를 가진 문자를 먼저 출력해준다.
