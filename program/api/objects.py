from comtypes import GUID, COMMETHOD
from comtypes.client import GetModule
from comtypes import CoClass, IUnknown
from ctypes import POINTER, Structure, c_longlong, c_long, HRESULT
from ctypes.wintypes import (
    RECT,
    DWORD,
    LONG,
    WORD,
    ULONG,
    HWND,
    UINT,
    LPCOLESTR,
    LCID,
    LPVOID,
)
from ctypes import windll

from comtypes.gen.DirectShowLib import (
    CaptureGraphBuilder2,
    ICreateDevEnum,
    typelib_path,
    IBaseFilter,
    IBindCtx,
    IMoniker,
    IAMStreamConfig,
    IAMVideoControl,
    IAMVideoProcAmp
)


__all__ = [
    'SampleGrabber',
    'tag_AMMediaType',
    'CaptureGraphBuilder2',
    'ICreateDevEnum',
    'typelib_path',
    'IBaseFilter',
    'IBindCtx',
    'IMoniker',
    'IAMStreamConfig',
    'IAMVideoControl',
    'IAMVideoProcAmp'
]


CLSID_VideoInputDeviceCategory = GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}")
CLSID_SystemDeviceEnum = GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
IID_IAMVideoProcAmp = GUID("{C6E13360-30AC-11d0-A18C-00A0C9118956}")

class DeviceEnumerator(CoClass):
    _reg_clsid_ = CLSID_SystemDeviceEnum
    _com_interfaces_ = [ICreateDevEnum]
    _idlflags_ = []  # type: ignore
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)


MEDIATYPE_Video = GUID('{73646976-0000-0010-8000-00AA00389B71}')
MEDIATYPE_Interleaved = GUID('{73766169-0000-0010-8000-00aa00389b71}')

PIN_CATEGORY_CAPTURE = GUID('{fb6c4281-0353-11d1-905f-0000c0cc16ba}')
