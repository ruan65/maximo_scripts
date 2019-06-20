from psdi.server import MXServer
from psdi.server import MXServer
from psdi.server import MXServer
mxServer = MXServer.getMXServer()
userInfo = mxServer.getUserInfo('maxadmin')

val = request.getQueryParam('VAL')

valSet = mxServer.getMboSet('WORKORDER', userInfo)
valSet.setWhere('WONUM='+val)
wo = valSet.getMbo(0)


wfsr = mxServer.lookup('WORKFLOW')

wfsr.initiateWorkflow('ILCWODIAG',mbo)
wo.changeStatus(u'ОЖИДДИАГ', MXServer.getMXServer().getDate(), u'Ожидается диагностика',4L)
valSet.save()