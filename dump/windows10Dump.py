from __future__ import unicode_literals
from dump import _Dump
from utils.vss import _VSS
import os

class Windows10Dump(_Dump):
    def __init__(self, params):
        super(Windows10Dump, self).__init__(params)
        self.root_reg = os.path.join(_VSS._get_instance(params)._return_root(), 'Windows\System32\config')
