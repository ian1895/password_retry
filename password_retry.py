# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入三次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有_次機會!"

pwd_real = 'a123456' #正確密碼
i = 3 #剩餘機會

while i > 0: #最多3次機會
	i = i - 1
	password = input('請輸入密碼: ')
	if password == pwd_real:
		print('登入成功!')
		break
	else:
		if i > 0: 
			print('密碼錯誤! 還有', i, '次機會!') 
		else:
			print('你被封鎖了!!')	
