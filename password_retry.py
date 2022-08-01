# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入三次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有_次機會!"

password = input('請輸入密碼: ')
pwd_real = 'a123456' #正確密碼
i = 3 #剩餘機會
x = 0

while x < i: #最多3次機會
	if password == pwd_real:
		print('登入成功!')
		break
	else:
		x = x + 1	
		if x < i: 
			print('密碼錯誤! 還有', i-x, '次機會!') 
			password = input('請輸入密碼: ')
		else:
			print('你被封鎖了!!')
			break	
