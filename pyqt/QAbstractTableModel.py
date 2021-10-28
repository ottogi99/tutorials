# --- Detailed Description
# QAbstractTableModel은 데이터를 항목의 2차원 배열로 나타내는 모델에 대한 표준 인터페이스를 제공합니다.
# It is not used directly, but must be subclassed.

# 모델은 QAbstractItemModel 보다 더 전문화된 인터페이스를 제공하기 때문에 QListView에 데이터를 제공하는 데 사용할 수 있지만 트리 뷰와
# 함께 사용하는 데 적합하지 않습니다. If you need to represent a simple list of items, and only need a model to contain a
# single column of data, subclassing the QAbstractListModel may be more appropriate.

# rowCount() 및 columnCount() 함수는 테이블의 차원을 반환합니다.
# To retrieve a model index corresponding to an item in the model, use index() and provide only the row and column numbers.

# --- Subclassing
# QAbstractTableModel 을 서브클래싱할 때 rowCount(), columnCount() 및 data() 를 구현해야 합니다.
# Default implementations of the index() and parent() functions are provided by QAbstractTAbleMdodel.
# 잘 작동하는 모델은 headerData() 구현합니다.

# Editable models need to implement setData(), and implement flags() to return a value containing ItemIsEditable.

# 크기 조정 가능한 데이터 구조에 대한 인터페이스를 제공하는 모델은 insertRows(), removeRows(), insertColumns() 및 removeColumns() 구현을
# 제공할 수 있습니다. When implementing these functions, it is important to call the appropriate functions so that all connected
# views are aware of any changes:

