from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.merchant.merchantCertificateTicketService import MerchantCertificateTicketService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
from steam.user.lottery.lotteryDetailService import LotteryDetailService
from steam.user.lottery.lotteryDrawService import LotteryDrawService
from steam.user.order.userListOrderActivityService import UserListOrderActivityService
from steam.user.order.userDetailOrderService import UserDetailOrderActivityService


class MerchantCertificateTicketTest(SteamTestCase):
    """商户核销券码"""
    __interfaceName__ = "/ticket-service/merchant/certificateTicket"

    @initInputService(
        services=[
            LotteryQueryLotteryListService,
            LotteryDetailService,
            UserDetailOrderActivityService,
            LotteryDrawService,
            UserListOrderActivityService],
        curser=MerchantCertificateTicketService,
        sign="merchant")
    def __init__(self, methodName='runTest',
                 param=None):
        super(MerchantCertificateTicketTest, self).__init__(methodName, param)


if __name__ == "__main__":
    from steam.user.order.userDetailOrderTest import UserDetailOrderActivityTest
    from steam.user.order.userListOrderActivityTest import UserListOrderActivityTest
    from steam.user.lottery.lotteryDrawTest import LotteryDrawTest
    from steam.user.lottery.lotteryDetailTest import LotteryDetailTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    UserDetailOrderActivityTest(methodName="compareRetcodeTest",
                                param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserListOrderActivityTest(methodName="compareRetcodeTest",
                              param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryDrawTest(methodName="compareRetcodeTest",
                    param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryDetailTest(methodName="compareRetcodeTest",
                      param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName="compareRetcodeTest",
                                param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
        casefilepath="\\steamcase\\user\\merchant\\ticket-serviceMerchantCertificateTickets.yml",
        testclse=MerchantCertificateTicketTest,
        basepath="D:\\litaojun\\steamyml")
