from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit
import objc


class TestWKNavigationDelegateHelper(WebKit.NSObject):
    def webView_decidePolicyForNavigationAction_decisionHandler_(self, w, a, h):
        pass

    def webView_decidePolicyForNavigationResponse_decisionHandler_(self, w, r, h):
        pass

    def webView_didReceiveAuthenticationChallenge_completionHandler_(self, w, c, h):
        pass


class TestWKNavigationDelegate(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(WebKit.WKErrorDomain, str)

        self.assertEqual(WebKit.WKNavigationActionPolicyCancel, 0)
        self.assertEqual(WebKit.WKNavigationActionPolicyAllow, 1)

        self.assertEqual(WebKit.WKNavigationResponsePolicyCancel, 0)
        self.assertEqual(WebKit.WKNavigationResponsePolicyAllow, 1)

    @onlyOn64Bit
    @min_os_level("10.10")
    def testProtocols(self):
        p = objc.protocolNamed("WKNavigationDelegate")
        self.assertIsInstance(p, objc.formal_protocol)

        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_decidePolicyForNavigationAction_decisionHandler_,  # noqa: B950
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_decidePolicyForNavigationResponse_decisionHandler_,  # noqa: B950
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_didReceiveAuthenticationChallenge_completionHandler_,  # noqa: B950
            2,
            objc._C_VOID + objc._C_NSInteger + objc._C_ID,
        )
