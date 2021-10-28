# --- Detailed Description
# QAbstractItemModel 클래스는 항목 모델이 모델/뷰 아키텍처의 다른 구성 요소와 상홍 운용할 수 있도록 사용해야 하는 표준 인터페이스를 정의합니다.
# It is not supposed to be instantiated directly. (직접 인스턴스화하면 안됩니다.)
# 대신 새 모델을 만들려면 하위 클래스를 지정해야 합니다.

# The QAbstractItemModel class is one of the Model/View Classes and is part of Qt's model/view framework.
# QML의 항목 보기 요소 또는 Qt 위젯 모듈의 항목 보기 클래스에 대한 기본 데이터 모델로 사용할 수 있습니다.

# If you need a model to use with an item view such as OML's List View element or the C++ widgets QListView or QTbale view,
# you should consider subclassing QAbstracListModel or QAbstractTableModel instead of this class.
# (QML의 목록 보기 요소 또는 C++ 위젯 QListView 또는 QTableView 와 같은 항목 보기와 함께 사용할 모델이 필요한 경우 이 클래스 대신
# QAbstactListModel 또는 QAbstractTableModel을 서브클래싱하는 것을 고려해야 합니다.)

# 기본 데이터 모델은 테이브르이 계층 구조로 뷰 및 대리자에 노출됩니다.
# If you do not amke use of the hierarchy, then the model is a simple table of rows and columns.
# 각 항목에는 QModelIndex에 의해 지정된 고유 색인이 있습니다.

# Every item of data that can be accessed via a model has an associated model index.
# index() 함수를 사용하여 이 모델 인덱스를 얻을 수 있습니다.
# Each index may have a sibling() index; child items have a parent() index.

# 각 항목에는 여러 데이터 요소가 연결되어 있으며 모델의 data() 함수에 역할(ItemDataRole 참조)을 지정하여 검색할 수 있습니다.
# Data for all available roles can be obtained at the same time using the itemData() function.

# 각 역할에 대한 데이터는 특정 itemDataRole을 사용하여 설정됩니다.
# Data for individual roles are set individually with setData(), or they can be set foa all roles with setItemData().

# 항목은 flags() (ItemFlag 참조)로 쿼리하여 다른 방법으로 선택, 드래그 또는 조작할 수 있는지 확인할 수 있습니다.

# If an item has child objects, hasChildren() returns true for the corresponding index.

# 모델에는 계층 구조의 각 수준에 대한 rowCount() 및 columnCount()가 있습니다.
# Rows and columns cab be inserted and removed with insertRows(), insertColumns(), removeRows(), and removeColumns().

# 모델은 변경 사항을 나타내는 신호를 내보냅니다.
# For example, dataChanged() is emitted whenever items of data made available by the model are changed.
# 모델에서 제공하는 헤더를 변경하는 headerDataChanged() 가 내보내집니다.
# If the structure of the underlying data changes, the model can emit layoutChanged() to indicate to any attached views
# that the should redisplay any items shown, taking the new structure into account.

# 모델을 통해 사용 가능한 항목은 match() 함수를 사용하여 특정 데이터를 검색할 수 있습니다.

# To sort the model, you can use sort().



