#500원 100원 50원 10원 거슬러줘야 할 동전의 최소 개수
#큰 화폐부터 거슬러 주자

num=int(input())
oh=int(num/500)
beak=int((num-oh*500)/100)
ohsi=int((num-(beak*100+oh*500))/50)
si=int((num-(beak*100+oh*500+ohsi*50))/10)
print(oh+beak+ohsi+si)