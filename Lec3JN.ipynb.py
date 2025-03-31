# coding: utf-8
from matplotlib import pyplot as plt
import numpy as np
# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()
# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()
# print information about the magic commands
get_ipython().run_line_magic('magic', '')
#_ Magic cheat-sheet 
get_ipython().run_line_magic('quickref', '')
#Write the cell’s contents to a file
get_ipython().run_line_magic('%writefile', 'Lec3_VS.py')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('pinfo', '%timeit')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_cell_magic('timeit', '', 'L = []\nfor n in range(1000):\n L.append(n ** 2)\n')
