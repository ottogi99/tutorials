# --- Detailed Description
# QAbstractListModel은 데이터를 단순한 비계층적 항목 시퀀스로 나타내는 모델에 대한 표준 인터페이스를 제공합니다.
# It is not used directly, but must be subclassed.

# 이 모델은 QAbstractItemModel 보다 더 전문화된 인터페이스를 제공하기 때문에 트리 뷰와 함께 사용하기에 적합하지 않습니다.
# You will need to subclass QAbstractItemModel if you want to provide a model for that purpose.
# 데이터를 관리하기 위해 여러 목록 모델을 사용해야 하는 경우 대신 QAbstractTableModel을 하위 클래스로 지정하는 것이 더 적절할 수 있습니다.

# Simple models can be created by subclassing this class and implementing the minimum number of required functions.
# 예를 들어, QListView 위젯에 문자열 목록을 제공하는 간단한 읽기 전용 QStringList 기반 모델을 구현할 수 있습니다.
# In such a case, we only need to implement the rowCount() function to return the number of items in the list,
# and the data() function to retrieve items from the list.
# (이러한 경우 목록의 항목 수를 반환하는 rowCount() 함수와 목록에서 항목을 검색하는 data() 함수만 구현하면 됩니다.

# 모델은 1차원 구조를 나타내므로 rowCount() 함수는 모델의 총 항목 수를 반환합니다.
# The columnCount() function is implemented ofr interoperability with all kinds of view, but by default informs views
# that the model contains only one column
# (columnCount() 함수는 모든 종류의 뷰와의 상호 운용성을 위해 구현되지만 기본적으로 모델에는 한의 열만 포함되어 있음을 뷰에 알립니다.)

# --- Subclassing
# QAbstractListModel을 서브클래싱할 때 rowCount() 및 data() 함수의 구현을 제공해야 합니다.
# Well behaved models also provide a headerData() implementation.

# 모델이 QML 내에서 사용되고 roleNames() 함수에서 제공하는 기본 역할이 아닌 다른 역할이 필요한 경우 이를 재정의해야 합니다.

# For editable list models, you must also provide an implementation of setData(), and implement the flags() function
# so that it returns a value containing ItemIsEditable.

# QAbstractListModel은 이 모델의 항목의 단일 열만 있음을 뷰에 알리는 columnCount() 기본 구현을 제공합니다.

# 크기 조정이 가능항 목록과 같은 데이터 구조에 대한 인터페이스를 제공하는 모델은 insertRow() 및 removeRows() 구현을 제공할 수 있습니다.
# When implementing these functions, it is important to call the appropriate functions so that all connected views are
# aware of any changes:

# insertRow() 구현은 데이터 구조에 새 행을 삽입하기 전에 beginInsertRow() 를 호출해야 하고, 그 직후에 endInsertRows()를 호출해야 합니다.

# A removeRows() implementation must call beginRemoveRows() before the rows are removed from the data structure, and
# it must call endRemoveRows() immediately afterwards.
