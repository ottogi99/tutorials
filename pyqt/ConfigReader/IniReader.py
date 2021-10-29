# 표준 라이브러인 configparser를 사용하면 .ini 파일을 읽고 쓸 수 있다.

import configparser

# config['AAA'] = {}
# config['AAA']['BBB'] = 'CCC'
# config['DEFAULT']['DDD'] = 'EEE'

# with open(ini_file, 'a', encoding='utf8') as iniFile:
#     config.write(iniFile)


class IniReader:
    _sections = {}
    _data = []

    def __init__(self, sections=None, config_file=None):
        self._sections = sections
        self._ini_file = config_file

    def setFile(self, config_file):
        self._ini_file = config_file

    def getFile(self):
        return self._ini_file

    def setSections(self, sections):
        self._sections = sections

    def getSections(self):
        return self._sections

    def read(self, config_file=None):
        if config_file is None:
            if self._ini_file is None:
                print('ini 환경파일이 정의되지 않았습니다.')
                return
                # Exception('ini 환경파일이 정의되지 않았습니다.')
            config_file = self._ini_file

        config = configparser.ConfigParser()
        result = []

        # file 존재 여부 확인
        try:
            config.read(config_file, encoding='utf8')
        except (FileExistsError, FileNotFoundError) as e:
            print(e)

        for section, items in self._sections.items():
            if section in config:
                for item in items:
                    if item in config[section]:
                        values = config[section][item].split('\n')
                        value = [v for v in values]
                        # print("[{0}]{1}={2}".format(section, item, config[section][item]))
                        # print("[{0}]{1}={2}".format(section, item, value))
                        result.append((section, item, value))

        return result


if __name__ == "__main__":
    ini_file = '../ini/yongdam.ini'
    sections = {
        'MANAGER': ['name', 'email', 'contact'],
        'NAC_MANAGER': ['name', 'email', 'contact'],
        'MSMT_SERVER': ['name', 'ip', 'port', 'dns', 'id', 'pwd'],
        'TM_SERVER': ['name', 'ip', 'port', 'id', 'pwd'],
        'SMART_TM': ['name', 'ip', 'port', 'id', 'pwd'],
        'DEVICE_SERVER': ['name', 'default_ip', 'ip', 'model', 'serial', 'id', 'pwd']
    }

    reader = IniReader(sections, ini_file)
    # reader.setFile(ini_file)
    # reader.setSections(sections)
    print(reader.read())
