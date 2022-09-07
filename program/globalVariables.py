from enum import Enum

class VideoProcAmpProperty(Enum):
  VideoProcAmp_Brightness = 0
  VideoProcAmp_Contrast = 1
  VideoProcAmp_Hue = 2
  VideoProcAmp_Saturation = 3
  VideoProcAmp_Sharpness = 4
  VideoProcAmp_Gamma = 5
  VideoProcAmp_ColorEnable = 6
  VideoProcAmp_WhiteBalance = 7
  VideoProcAmp_BacklightCompensation = 8
  VideoProcAmp_Gain = 9

class VideoProcAmpFlags(Enum):
  VideoProcAmp_Flags_Auto = 1
  VideoProcAmp_Flags_Manual = 2