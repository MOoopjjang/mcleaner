#!python3
# -*- coding:utf-8 -*-


import os, sys

"""
Make by MOoop

Desc :
  _rootPath로 부터 하위디렉토리를 순회하며 지정된 garbage파일들을 찾아 삭제하는 class

History:
------------------------------------------------------------------------------------------------------
 2019.10.26				create														v0.9

 2019.12.04				확장자 filter코드 endswith 메소드 사용으로 변경.						v0.9.1

 2020.06.11				GUI 연동을 위한 Interface 변경									v0.9.2
 
 2020.06.18				command로 실행할수 있도록 parameter 기능추가						v0.1.0
------------------------------------------------------------------------------------------------------

"""


class MCleaner:
    def __init__(self, _rootPath=None, _exts=None):
        self._rootPath = _rootPath
        self._rootPath = _rootPath
        self._exts = _exts

    def setRootPath(self, _rootPath):
        self._rootPath = _rootPath
        return self

    def setExts(self, _exts):
        self._exts = _exts
        print('{}'.format(self._exts))
        return self

    def run(self):
        if self._rootPath == None or self._exts == None:
            raise Exception('값이 설정되지 않았습니다.')

        # 이전 결과파일 삭제
        if os.path.exists('result.txt'): os.unlink('result.txt')

        with open('result.txt', 'w') as fw:
            count = 0
            for d, s, fs in os.walk(self._rootPath):
                for f in fs:
                    fullPath = os.path.join(d, f)
                    if fullPath.endswith(tuple(self._exts)):
                        fw.write(fullPath + '\n')
                        os.unlink(fullPath)
                        count += 1
                        yield (count, fullPath)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage : {} [Path] [.ext]'.format(os.path.basename(__file__)))
        print('ex) {} {} ".log"'.format(os.path.basename(__file__), os.getcwd()))
        print('ex) {} {} ".log|.tmp"'.format(os.path.basename(__file__), os.getcwd()))
        sys.exit(1)


    exts = sys.argv[2].split('|')
    mc = MCleaner(os.getcwd(), exts)
    for i, t in mc.run():
        print('{}--{}'.format(i, t))
