# 기본 금액 : balance
# 기본 금액에 돈을 넣어 주세요
# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 버튼이 누르기 전까지 계속해서 노출해 주세요
# 종료를 누르면 서비스를 종료한다는 메세지를 출력하고 현재 잔액을 보여주세요

receipts = [] #[]대괄호는 list / {}중괄호는 dict / ()소괄호는 tuple
balance = 3000 #현재 잔액을 보여주세요

while True :
    print()
    num = input("사용하실 기능을 선택해주세요(1:입금, 2:출금, 3:영수증보기, 4:종료)")
    if num == '4' :  
        break
    if num == "1" :
        deposit_amount = input("입금할 금액을 입력해주세요 : ") # input() : 내장함수 / int : 정수형 데이터로 형변환 해주는 내장함수
        if deposit_amount.isdigit() and int(deposit_amount) > 0 :
            balance = balance + int(deposit_amount)
            receipts.append(("입금", deposit_amount, balance))
            print(f'입금하신 금액은 {deposit_amount}원 이고, 현재 잔액은 {balance}입니다')
        else :
            print('입금한 금액을 숫자 형태와 음수가 아닌값을 입력해 주세요')
    if num == "2" :
        withdraw_amount = int(input("출금할 금액을 입력해 주세요 : "))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        receipts.append(("출금", withdraw_amount, balance))
        print(f'출금하신 금액은 {withdraw_amount}원 이고, 현재 잔액은 {balance}원 입니다')
    if num == "3" :
        if receipts :      
            print("===영수증===")
            for i in receipts :
                print(f'{i[0]}:{i[1]}원 | 잔액 : {i[2]}원')
            
        else : 
            print("영수증 내용이 없습니다.")
print(f'서비스를 종료합니다. 현재 잔액은 {balance}입니다.')
    