import sys
import argparse
from pathlib import Path as p
import datetime

class ExecInfo():
    def __init__(self) -> None:
        self.cwd = p.cwd().resolve()
        self.execdt = self.now()

    def now(self):
        return datetime.datetime.now().strftime('%Y%m%d-%H%M%S')


def argparser():
    """ argsってクラスに入れておくのとrootに置いておくのとどっちが便利なの??
    """
    parser = argparse.ArgumentParser(description='Nothing')
    parser.add_argument('position_variable', help='位置変数')
    parser.add_argument('position_variable_opt', nargs='?', default=None, help='省略可能な位置変数')
    parser.add_argument('-opt', '--option_variable', type=int, default=999, help='オプション変数')
    parser.add_argument('--choices', choices=['a', 'b', 'c'], help='選択肢以外はエラー')
    parser.add_argument('--multi', nargs='*', help='可変長。数字を入れると固定長')
    parser.add_argument('--must', required=True, help='位置どこでもいい必須変数')


def main(args):

    ei = ExecInfo()
    print(vars(ei))

if __name__ == '__main__':

    args = argparser()
    main(args)
