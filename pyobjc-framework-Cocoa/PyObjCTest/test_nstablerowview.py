import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTableRowView(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSTableRowView.isEmphasized)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setEmphasized_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isGroupRowStyle)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setGroupRowStyle_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isSelected)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setSelected_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isFloating)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setFloating_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isTargetForDropOperation)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setTargetForDropOperation_, 0)
        self.assertResultIsBOOL(AppKit.NSTableRowView.isNextRowSelected)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setNextRowSelected_, 0)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSTableRowView.isPreviousRowSelected)
        self.assertArgIsBOOL(AppKit.NSTableRowView.setPreviousRowSelected_, 0)
