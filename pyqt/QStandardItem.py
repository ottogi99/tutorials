# items usually contains text, icons, or checkboxes.
# 각 항목에는 setBackground() 함수로 설정된 고유한 배경 브러시가 있습니다.
# The current brush can be found with background()
# 각 항목의 텍스트 레이블은 자체 글꼴과 브러시로 렌더링할 수 있습니다.
# These are specified with the setFont() and setForeground() functions, and read with font() and foreground().

# setData() 를 호출하여 항목에 애플리케이션별 데이터를 저장할 수 있습니다.

# Each item can have a two-dimensional table of child items.
# 이를 통해 항목의 계층 구조를 구축할 수 있습니다.
# The typical hierarchy is the tree, in which case the child table is a table with a single column (a list)
# (일반적인 계층 구조는 트리이며, 이 경우 하위 테이블은 단일 열(목록)이 있는 테이블입니다.)

# The dimensions of the child table can be set with setRowCount() and setColumnCount().
# setChild()를 사용하여 자식 테이블에 항목을 배치할 수 있습니다.
# New rows and columns of children can also be inserted with insertRow() and insertColumn(),
# or appended with appendRow() and appendColumn().
# 추가 및 삽입 기능을 사용할 때 자식 테이블의 크기는 필요에 따라 커집니다.

# An existing row of children can be removed with removeRow() or takeRow()
# 그에 따라, removeColumn() 또는 takeColumn()을 사용하여 열을 제거 할 수 있습니다.

# An item's children can be sorted by calling sorChildren()

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

