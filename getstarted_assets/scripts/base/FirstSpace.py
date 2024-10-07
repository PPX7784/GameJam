# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class FirstSpace(KBEngine.Space):
    """
    FirstSpace的base部分，
    注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
    """
    def __init__(self):
        KBEngine.Space.__init__(self)
        # 存储在globalData中，方便获取
        KBEngine.globalData["FirstSpace"] = self

    def onClientEnabled(self):
        """
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体。
        """
        # 客户端一旦连接，就把他放入FirstSpace空间
        INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))
        first_space = KBEngine.globalData["FirstSpace"]
        self.createCellEntity(first_space.cell)
    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        DEBUG_MSG(id, userArg)

    def onLogOnAttempt(self, ip, port, password):
        """
        KBEngine method.
        客户端登陆失败时会回调到这里
        """
        INFO_MSG(ip, port, password)
        return KBEngine.LOG_ON_ACCEPT

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
        self.destroy()


