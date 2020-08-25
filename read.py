data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

print(data[0])

s = 0
new = []
good = []
# 快寫法 good = [d for d in data if 'good' in d]
for d in data:
	s += len(d)
	if len(d) < 100:
		new.append(d)
	if 'good' in d:
		good.append(d)
print('留言平均長度: ', s/len(data))
print('一共有', len(new), '筆留言小於100')
print('一共有', len(good), '筆留言有包含good')

bad = ['bad' in d for d in data]#'bad' in d ->運算式,
#=
#bad = []
#for d in data:
#	bad.append('bad' in d)

#文字計數
wc = {} #word_count
for d in data:
	words = d.strip().split() 
	#split預設就是空白,如果是預設,連續空白就不會被切成空字串
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] >= 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請輸入要找的字: ')
	if word == 'q':
		print('感謝使用')
		break
	if word in wc:
		print(word, '出現的次數: ',wc[word])
	else:
		print(word, '並不在此')


