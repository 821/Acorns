import requests,multiprocessing,os

link = 'http://xiaoxue.iis.sinica.edu.tw/yunshu/PageResult/PageResult'
total = 60069
start = 1
worker = 4

def main(order):
	FileExist = os.path.isfile(str(order) + '.html')
	if FileExist == False:
		payload = {'Guangyun': 'true', 'Hongwu': 'true', 'Jiyun': 'true', 'Libu': 'true', 'Zengyun': 'true', 'Zhongyuan': 'true', 'Zhongzhou': 'true', 'X-Requested-With': 'XMLHttpRequest', 'ZiOrder': str(order)}
		r = requests.post(link, data = payload)
		r.encoding = 'utf-8'
		with open(str(order) + '.html', 'w+', encoding = 'utf-8') as h:
			h.write(r.text)
		print(order)

if __name__ == '__main__':
	with multiprocessing.Pool(worker) as p:
		p.map(main, range(start, total + 1))