temp = {   '추움':'코트',
    '따듯함':'점퍼',
    '더움':'티셔츠',

}
out = {
    '회의':'구두',
    '운동':'운동화',
    '슈퍼':'슬리퍼'
}
spe = {
    '황사':'마스크',
    '햇빛':'선글라스',
    '우천':'우산'
}

a = input('날씨는 어떻습니까?')
b = input('어디에 가십니까?')
c = input('특수 상황은 무엇입니까?')

print(f'{temp[a]} 를 입고, {out[b]} 를 신고, {spe[c]} 를 챙기세요.')
