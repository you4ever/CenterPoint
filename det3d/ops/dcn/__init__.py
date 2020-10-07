# from .deform_conv import (DeformConv, DeformConvPack, ModulatedDeformConv,
#                           ModulatedDeformConvPack, deform_conv,
#                           modulated_deform_conv)
from mmcv.ops import DeformConv2d as DeformConv
from mmcv.ops import DeformConv2dPack as DeformConvPack
from mmcv.ops import ModulatedDeformConv2dPack as ModulatedDeformConvPack
from mmcv.ops import ModulatedDeformConv2d as ModulatedDeformConv
from mmcv.ops import deform_conv2d as deform_conv
from mmcv.ops import modulated_deform_conv2d as modulated_deform_conv

__all__ = [
    'DeformConv', 'DeformConvPack', 'ModulatedDeformConv',
    'ModulatedDeformConvPack', 'deform_conv', 'modulated_deform_conv',
]
