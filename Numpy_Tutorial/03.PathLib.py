# 파일과 경로 처리 모듈 (pathlib 내장 모듈)

from pathlib import Path

# 파일의 경로를 입력해 Path 클래스에서 file_path 객체 생성
# file_path = Path('C:/myPyExcel/modules/car.py')
# file_path = Path('./01.basic.py')
file_path = Path('C:/Repo/python/tutorials/Numpy_Tutorial/01.basic.py')

print(file_path)            # 파일의 전체 경로 출력
print(file_path.parent)     # 파일의 디렉터리 출력
print(file_path.name)       # 파일의 이름
print(file_path.suffix)     # 파일의 확장자
print(file_path.stem)       # 확장자를 제외한 파일명

# 디렉터리 경로를 입력해 dir_path 객체 생성
dir_path = Path('C:/Repo/Python/tutorials/Numpy_Tutorial/asset')

print(dir_path)
print(dir_path.exists())
print(dir_path.is_dir())
print(dir_path.is_file())
print(dir_path.home())

# 현재 작업 디렉터리를 상대 경로로 입력해 r_dir_path 객체를 생성
print('- 현재 작업 디렉터리를 상대 경로로 입력해 r_dir_path 객체를 생성')
r_dir_path = Path('.')

print(r_dir_path)
print(r_dir_path.resolve())     # 상대 경로를 절대 경로로 변경
print(r_dir_path.cwd())         # 현재 작업 디렉터리

# 상위 디렉터리를 상대 경로로 입력해 a_dir_path 객체를 생성
print('- 상위 디렉터리를 상대 경로로 입력해 a_dir_path 객체를 생성')
a_dir_path = Path('..')

print(a_dir_path)
print(a_dir_path.resolve())

# -- 디레터리 생성
print('\n-디렉터리 생성')
dir_path = Path('C:/Repo/Python/tutorials/Numpy_Tutorial/')

# 새로 생성할 디렉터리를 dir_path 객체에 추가. 디렉터리 구분자는 '/'를 사용 (문법 주의 '/')
sub_dir_path = dir_path/'test'

# 새로운 디레터리를 생성 (parents : 상위 디렉터리가 없는 경우 생성(True), exist_ok : 이미 같은 디렉터리가 있는 경우 무시(True)
sub_dir_path.mkdir(parents=True, exist_ok=True)

# 생성한 디렉터리의 존재 여부 확인
print("{0} 존재 여부: {1}".format(sub_dir_path, sub_dir_path.exists()))

# -- 디렉터리 제거
print('\n- 디렉터리 제거')
sub_dir_path.rmdir()
# 생성한 디렉터리의 존재 여부 확인
print("{0} 존재 여부: {1}".format(sub_dir_path, sub_dir_path.exists()))

# -- 하위 디렉터리 이름을 리스트로 지정
print('\n- 여러개의 디렉터리 생성 및 삭제')
sub_dirs = ['test1', 'test2', 'test3']

for sub_dir in sub_dirs:
    sub_dir_path = dir_path/sub_dir
    sub_dir_path.mkdir(parents=True, exist_ok=True)
    print("{0} 존재 여부: {1}".format(sub_dir_path, sub_dir_path.exists()))

for sub_dir in sub_dirs:
    sub_dir_path = dir_path/sub_dir
    sub_dir_path.rmdir()
    print("{0} 존재 여부: {1}".format(sub_dir_path, sub_dir_path.exists()))

# -- touch() 메서드로 파일을 생성
print('\n- touch() 메서드로 파일을 생성')
file_path = Path('C:/Repo/Python/tutorials/Numpy_Tutorial/test_file.txt')
file_path.touch()   # 빈 파일 생성
print(file_path.exists())

print('\n- unlink() 메서드로 파일을 제거')
if file_path.exists():
    file_path.unlink()
print(file_path.exists())

# glob() 메서드 : 패턴에 대응되는 모든 디렉터리와 파일을 반환
print('\n- glob() 메서드로 패턴 지정')
test_dir = Path('C:/Repo/Python/tutorials/Numpy_Tutorial')

# 테스트용 디렉터리 생성
print('\n- 테스트용 디렉터리 생성')
test_dir.mkdir(parents=True, exist_ok=True)

data_files = ['file01.txt', 'file02.txt', 'file10.txt', 'file11.txt', 'file01.csv', 'file02.csv']

for data_file in data_files:
    file_path = test_dir/data_file
    file_path.touch()

sub_dirs = ['sub_dir1', 'sub_dir2', 'sub_dir3']

for sub_dir in sub_dirs:
    sub_dir_path = test_dir/sub_dir
    sub_dir_path.mkdir(parents=True, exist_ok=True)

sub_dir_files = ['data_file01.csv', 'data_file02.csv']

for sub_dir_file in sub_dir_files:
    for sub_dir in sub_dirs:
        file_path = test_dir/sub_dir/sub_dir_file
        file_path.touch()

print('\n- 모든 디렉터리와 파일을 반환')
dir_files = test_dir.glob('*')

for dir_file in dir_files:
    print(dir_file)

