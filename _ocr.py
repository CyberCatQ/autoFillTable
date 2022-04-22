import re

from aip import AipOcr


class OCR:
    def __init__(self, file_path, ocr_cfg) -> None:
        self.file_path = file_path
        self.file_type = self._check_type()
        self.data = None
        self.ocr_cfg = ocr_cfg

        app_id = '25890848'
        api_key = '6VGCcSckGdlVgMtXPXrLo47y'
        secret_key = 'i3Xhu52mreGEPhHRXPI97SZGymjtIn0K'
        self.client = AipOcr(app_id, api_key, secret_key)

    def _check_type(self):
        suffix = self.file_path.split('.')[-1]
        support_img_type = ['jpg', 'jpeg', 'png', 'bmp']
        for i in support_img_type:
            if i == suffix:
                return 'img'

        if self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls'):
            return 'excel'
        
        raise TypeError('不支持的文件类型')

    def ocr(self):
        if self.file_type == 'img':
            with open(self.file_path, 'rb') as f:
                img = f.read()
            ocr_result = self.client.form(img)
            words_result = [dic['words'] for dic in ocr_result['forms_result'][0]['body'] if re.match(r'[\u4e00-\u9fa5]', dic['words'])]
            number_result = [dic['words'] for dic in ocr_result['forms_result'][0]['body'] if re.match(r'[0-9]', dic['words'])]
            
            return self.ocr_cfg.parse(words_result, number_result)
