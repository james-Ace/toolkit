from lib.PDFtoDocx.pdf2word import main



def run():
    print('Tookit 工具箱：')
    while(True):
        commod = input('输入指令：')
        if commod in ['1']:
            if commod == '1':
                print('工具在运行中..')
                res = main()
                if res == False:
                    print('运行结束')
                    exit()
        elif commod in ['exit', 'out']:
            print('退出工具~')
            exit()


if __name__ == "__main__":
    run()