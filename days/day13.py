'''
进程与线程
'''
'''
使用多进程下载任务
'''
# from multiprocessing import Process
# from os import getpid
# from time import time,sleep
# from random import randint
#
# def download(filename):
#     print('进程号为：%s'% getpid())#获得目前进程的id
#     print('正在下载%s....'% filename)
#     time_to_load = randint(5,10)
#     sleep(time_to_load)
#     print('%s下载完成，共用%s秒'%(filename,time_to_load))
# def main():
#     start = time()#获得目前的时间
#     p1 = Process(target = download,args = ('python教程.pdf',))#设置一个进程，目标函数加任务参数（注意参数间的逗号）
#     p1.start()#p1进程开始
#     p2 = Process(target = download,args = ('复仇者联盟.mp4',))
#     p2.start()
#     p1.join()#等待进程执行结束
#     p2.join()
#     end = time()
#     print('任务下载完成，共用%f秒'%(end - start))#会比最长进程时间多一点（脚本的执行顺序时间差）
# if __name__ == "__main__":
#     main()
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
