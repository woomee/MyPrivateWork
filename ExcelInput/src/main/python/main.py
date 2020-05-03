'''
テンプレートとなるExcelから値をコピーする

【前提】
conda install xlwings

【利用方法】
> python main.py [テンプレートファイル] [出力ファイル]

'''

import xlwings as xw
import sys
import logging


if __name__ == '__main__':
    ''' メイン関数 '''
    # ログ設定
    logging.basicConfig(format='%(asctime)s- %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 引数からファイルを取得
    if len(sys.argv) < 3:
        logger.info('Not specified template / out / (write) files')
        sys.exit(1)
    templateFile = sys.argv[1]
    writeFile = outFile = sys.argv[2]
    if len(sys.argv) > 3:
        writeFile = sys.argv[3]       
    
    logger.info(f'template={templateFile}')
    logger.info(f'outFile={outFile}')
    logger.info(f'writeFile={writeFile}')

    # テンプレートからの読み込み
    templateBook = xw.Book(templateFile)
    outBook = xw.Book(outFile)
    for templateSheet in templateBook.sheets:
        try:
            outSheet = outBook.sheets[templateSheet.name]
        except:
            logger.warning(f'Not exist sheet={templateSheet.name}')
            continue

        logger.info(f'Output sheet={outSheet.name}')

        templateRange = templateSheet.used_range
        min_row = templateRange.row
        max_row = templateRange.last_cell.row
        min_col = templateRange.column
        max_col = templateRange.last_cell.column

        for row in range(min_row, max_row):
            for col in range(min_col, max_col):
                cell = templateSheet.range((row, col))
                # None 以外の値をアドレス付きで出力
                if (cell.value != None):
                    logger.info(f'{cell.address} {cell.value}')
                    outSheet.range(cell.address).value = cell.value

    outBook.save(writeFile)
    logger.info(f'Finished!! outFile={writeFile}')
