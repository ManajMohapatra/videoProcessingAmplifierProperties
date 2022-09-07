from comtypes.client import CreateObject
from comtypes import GUID, COMError
from ctypes import cast
from globalVariables import VideoProcAmpProperty, VideoProcAmpFlags

from api.objects import (
    CaptureGraphBuilder2,
    DeviceEnumerator,
    IID_IAMVideoProcAmp,
    CLSID_VideoInputDeviceCategory,
    POINTER,
    IMoniker,
    IBaseFilter,
    MEDIATYPE_Video,
    PIN_CATEGORY_CAPTURE,
    IBindCtx,
    MEDIATYPE_Interleaved,
    IAMVideoProcAmp
)

class VideoProcAmp:
    def __init__(self):
        self.initialization()
        self.videoProcAmpControl = self.getGraphBuilderInterface(IAMVideoProcAmp)

    def initialization(self):
        self.dev_enum = CreateObject(DeviceEnumerator)
        self.graph_builder = CreateObject(CaptureGraphBuilder2)
        self.class_enum = self.dev_enum.CreateClassEnumerator(CLSID_VideoInputDeviceCategory, 0)
        (self.moniker, fetched) = self.class_enum.RemoteNext(1)
        self.null_context = POINTER(IBindCtx)()
        self.null_moniker = POINTER(IMoniker)()
        self.source = self.moniker.RemoteBindToObject(self.null_context, self.null_moniker, IBaseFilter._iid_)

    def getGraphBuilderInterface(self,interface):
        args = [
            PIN_CATEGORY_CAPTURE,
            MEDIATYPE_Interleaved,
            self.source,
            interface._iid_,
        ]
        try:
            result = self.graph_builder.RemoteFindInterface(*args)
        except COMError:
            args[1] = MEDIATYPE_Video
            result = self.graph_builder.RemoteFindInterface(*args)
        return cast(result, POINTER(interface)).value

    def getRange(self, feature):
        try:
            return self.videoProcAmpControl.GetRange(VideoProcAmpProperty[feature].value)
        except COMError:
            return None

    def getValue(self, feature):
        try:
            return self.videoProcAmpControl.Get(VideoProcAmpProperty[feature].value)
        except COMError:
            return None

    def setValue(self, feature, value, mode):
        if(mode == False):
            self.videoProcAmpControl.Set(VideoProcAmpProperty[feature].value, value, VideoProcAmpFlags['VideoProcAmp_Flags_Manual'].value)
        else:
            self.videoProcAmpControl.Set(VideoProcAmpProperty[feature].value, value, VideoProcAmpFlags['VideoProcAmp_Flags_Auto'].value)


if __name__ == '__main__':
    videoProcAmp = VideoProcAmp()
    print(videoProcAmp.getRange('VideoProcAmp_Brightness'))
    print(videoProcAmp.getRange('VideoProcAmp_Contrast'))
    print(videoProcAmp.getRange('VideoProcAmp_Hue'))
    print(videoProcAmp.getRange('VideoProcAmp_Saturation'))
    print(videoProcAmp.getRange('VideoProcAmp_Sharpness'))
    print(videoProcAmp.getRange('VideoProcAmp_Gamma'))
    print(videoProcAmp.getRange('VideoProcAmp_ColorEnable'))
    print(videoProcAmp.getRange('VideoProcAmp_WhiteBalance'))
    print(videoProcAmp.getRange('VideoProcAmp_BacklightCompensation'))
    print(videoProcAmp.getRange('VideoProcAmp_Gain'))