
# python wrapper for package github.com/js061/tsubasa within overall package tsubasa
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy gen -output=tsupy -vm=python3 github.com/js061/tsubasa

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _tsubasa
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from tsubasa import tsubasa
# and then refer to everything using tsubasa. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice []tsubasa.Point
class Slice_tsubasa_Point(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.Slice_tsubasa_Point_CTor()
			_tsubasa.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_tsubasa_Point.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		s = 'tsubasa.Slice_tsubasa_Point len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'tsubasa.Slice_tsubasa_Point([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _tsubasa.Slice_tsubasa_Point_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _tsubasa.Slice_tsubasa_Point_len(self.handle)
				return Slice_tsubasa_Point(handle=_tsubasa.Slice_tsubasa_Point_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Point(handle=_tsubasa.Slice_tsubasa_Point_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_tsubasa.Slice_tsubasa_Point_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_tsubasa_Point.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _tsubasa.Slice_tsubasa_Point_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_tsubasa.Slice_tsubasa_Point_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct tsubasa.DataOfChannel
class DataOfChannel(go.GoClass):
	""" Data stored in channel\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_DataOfChannel_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.DataOfChannel{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.DataOfChannel ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.Pair
class Pair(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_Pair_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.Pair{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.Pair ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.Point
class Point(go.GoClass):
	""" Struct for data point\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_Point_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.Point{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.Point ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.RowBWR
class RowBWR(go.GoClass):
	""" Serialized BasicWindowResult\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_RowBWR_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.RowBWR{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.RowBWR ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.RowBWRDFT
class RowBWRDFT(go.GoClass):
	""" Serialized BasicWindowDFTResult\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_RowBWRDFT_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.RowBWRDFT{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.RowBWRDFT ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.SerializedPair
class SerializedPair(go.GoClass):
	""" Struct for insertion to db, unique to each other\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_SerializedPair_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.SerializedPair{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.SerializedPair ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.BasicWindowDFTResult
class BasicWindowDFTResult(go.GoClass):
	""" Struct to store basic window dft statistics\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_BasicWindowDFTResult_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.BasicWindowDFTResult{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.BasicWindowDFTResult ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tsubasa.BasicWindowResult
class BasicWindowResult(go.GoClass):
	""" Struct to store basic window statistics\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tsubasa.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tsubasa.IncRef(self.handle)
		else:
			self.handle = _tsubasa.tsubasa_BasicWindowResult_CTor()
			_tsubasa.IncRef(self.handle)
	def __del__(self):
		_tsubasa.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.BasicWindowResult{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tsubasa.BasicWindowResult ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def GetLocations():
	"""GetLocations() []int
	
	 Get locations
	"""
	return go.Slice_int(handle=_tsubasa.tsubasa_GetLocations())
def GetMatrix():
	"""GetMatrix() []int"""
	return go.Slice_int(handle=_tsubasa.tsubasa_GetMatrix())
def GetRealMatrix():
	"""GetRealMatrix() []float"""
	return go.Slice_float64(handle=_tsubasa.tsubasa_GetRealMatrix())
def SetBasicWindowSize(size, goRun=False):
	"""SetBasicWindowSize(int size) 
	
	 Set Basic Window Size
	"""
	_tsubasa.tsubasa_SetBasicWindowSize(size, goRun)
def GetLatitudes():
	"""GetLatitudes() []float
	
	 Get the latitudes
	"""
	return go.Slice_float64(handle=_tsubasa.tsubasa_GetLatitudes())
def GetLatitudesIdx():
	"""GetLatitudesIdx() []int
	
	 Get the latitudes
	"""
	return go.Slice_int(handle=_tsubasa.tsubasa_GetLatitudesIdx())
def ReadFileByLocation(filename, locationRangeFile, goRun=False):
	"""ReadFileByLocation(str filename, str locationRangeFile) """
	_tsubasa.tsubasa_ReadFileByLocation(filename, locationRangeFile, goRun)
def ReadFile(filename, goRun=False):
	"""ReadFile(str filename) """
	_tsubasa.tsubasa_ReadFile(filename, goRun)
def ResetSketch(goRun=False):
	"""ResetSketch() """
	_tsubasa.tsubasa_ResetSketch(goRun)
def Sketch():
	"""Sketch() str"""
	return _tsubasa.tsubasa_Sketch()
def AddDataFromFile(filename, locationRangeFile):
	"""AddDataFromFile(str filename, str locationRangeFile) str"""
	return _tsubasa.tsubasa_AddDataFromFile(filename, locationRangeFile)
def GetLongitudesIdx():
	"""GetLongitudesIdx() []int
	
	 Get the longitudes
	"""
	return go.Slice_int(handle=_tsubasa.tsubasa_GetLongitudesIdx())
def Init(goRun=False):
	"""Init() """
	_tsubasa.tsubasa_Init(goRun)
def Query(thres, queryStart, queryEnd):
	"""Query(float thres, int queryStart, int queryEnd) []int"""
	return go.Slice_int(handle=_tsubasa.tsubasa_Query(thres, queryStart, queryEnd))
def QueryInDB(thres, start, end, granularity):
	"""QueryInDB(float thres, int start, int end, int granularity) []int"""
	return go.Slice_int(handle=_tsubasa.tsubasa_QueryInDB(thres, start, end, granularity))
def SketchInDB(goRun=False):
	"""SketchInDB() """
	_tsubasa.tsubasa_SketchInDB(goRun)
def Slide(start, cnt, qsize, bwsize, offset, rho):
	"""Slide(int start, int cnt, int qsize, int bwsize, int offset, float rho) []float"""
	return go.Slice_float64(handle=_tsubasa.tsubasa_Slide(start, cnt, qsize, bwsize, offset, rho))
def DeleteSkecth(isDFT, goRun=False):
	"""DeleteSkecth(bool isDFT) """
	_tsubasa.tsubasa_DeleteSkecth(isDFT, goRun)
def DirectCompute(thres, start, end):
	"""DirectCompute(float thres, int start, int end) []int"""
	return go.Slice_int(handle=_tsubasa.tsubasa_DirectCompute(thres, start, end))
def GetLongitudes():
	"""GetLongitudes() []float
	
	 Get the longitudes
	"""
	return go.Slice_float64(handle=_tsubasa.tsubasa_GetLongitudes())
def GetDataMapInfo():
	"""GetDataMapInfo() int
	
	 Get the information of dataMap
	"""
	return _tsubasa.tsubasa_GetDataMapInfo()
def GetNetworkUnweighted(queryStart, length, thres):
	"""GetNetworkUnweighted(int queryStart, int length, float thres) []int
	
	 Get matrix
	"""
	return go.Slice_int(handle=_tsubasa.tsubasa_GetNetworkUnweighted(queryStart, length, thres))
def InitDB(username, password_, goRun=False):
	"""InitDB(str username, str password_) """
	_tsubasa.tsubasa_InitDB(username, password_, goRun)
def InitMatrix(goRun=False):
	"""InitMatrix() """
	_tsubasa.tsubasa_InitMatrix(goRun)
def ReadFilesByLocation(dirname, locationRangeFile):
	"""ReadFilesByLocation(str dirname, str locationRangeFile) str"""
	return _tsubasa.tsubasa_ReadFilesByLocation(dirname, locationRangeFile)
def CutDataMap(newDataMap, start, end, goRun=False):
	"""CutDataMap(object newDataMap, int start, int end) 
	
	 Get a slice of dataMap
	"""
	_tsubasa.tsubasa_CutDataMap(newDataMap.handle, start, end, goRun)
def GetCorrelationMatrix(queryStart, length):
	"""GetCorrelationMatrix(int queryStart, int length) []float
	
	 Get realMatrix
	"""
	return go.Slice_float64(handle=_tsubasa.tsubasa_GetCorrelationMatrix(queryStart, length))
def GetTransitivity(arr):
	"""GetTransitivity([]float arr) float"""
	return _tsubasa.tsubasa_GetTransitivity(arr.handle)
def GetTimeSeriesNum():
	"""GetTimeSeriesNum() int
	
	 Get the length of dataMap
	"""
	return _tsubasa.tsubasa_GetTimeSeriesNum()
def ReadFiles(dirname):
	"""ReadFiles(str dirname) str"""
	return _tsubasa.tsubasa_ReadFiles(dirname)
def ClearDataMap(goRun=False):
	"""ClearDataMap() 
	
	 Clear dataMap
	"""
	_tsubasa.tsubasa_ClearDataMap(goRun)
def GetBasicWindowSize():
	"""GetBasicWindowSize() int
	
	 Get Basic Window Size
	"""
	return _tsubasa.tsubasa_GetBasicWindowSize()
def GetNetworkWeightedRatio(queryStart, length, rho):
	"""GetNetworkWeightedRatio(int queryStart, int length, float rho) []float"""
	return go.Slice_float64(handle=_tsubasa.tsubasa_GetNetworkWeightedRatio(queryStart, length, rho))
def GetNumberOfBW(granularity):
	"""GetNumberOfBW(int granularity) int
	
	 Get the number of basic windows
	"""
	return _tsubasa.tsubasa_GetNumberOfBW(granularity)
def GetTimeSeriesLength():
	"""GetTimeSeriesLength() int
	
	 Get length of time series
	"""
	return _tsubasa.tsubasa_GetTimeSeriesLength()


