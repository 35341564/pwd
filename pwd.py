password = 'a123456'
test = 0
while test < 3:
    pwd = input('請輸入密碼: ')
    if pwd == 'a123456':
        print('登入成功')
        break
    else:
        print('登入失敗')
        test = test+1
        print('你還能嘗試',3-test,'次')
        if test == 3:
            print('你已經不能再嘗試了')
            break


