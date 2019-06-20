from psdi.server import MXServer
from psdi.server import MXServer
mxServer = MXServer.getMXServer()
userInfo = mxServer.getUserInfo('maxadmin')

val = request.getQueryParam('VAL')

valSet = mxServer.getMboSet('WORKORDER', userInfo)
valSet.setWhere('WONUM='+val)
wo = valSet.getMbo(0)
wo.changeStatus(u'ЗАВЕРШЕНО', MXServer.getMXServer().getDate(), u'Работы завершены',4L)
valSet.save()