from psdi.server import MXServer
from psdi.server import MXServer
from psdi.server import MXServer
mxServer = MXServer.getMXServer()
userInfo = mxServer.getUserInfo('maxadmin')

val = request.getQueryParam('VAL')

valSet = mxServer.getMboSet('WORKORDER', userInfo)
valSet.setWhere('WONUM='+val)
rltkt = mbo.getMboSet('RELATEDTICKET').getMbo(0)
sr = rltkt.getMboSet('RELATEDRECTK').getMbo(0)
wo = valSet.getMbo(0)
wo.changeStatus(u'В РАБОТЕ', MXServer.getMXServer().getDate(), u'Принято в работу',4L)
if sr != None:
 sr.changeStatus(u'В РЕМОНТЕ', MXServer.getMXServer().getDate(), u'Принято в работу',4L)
valSet.save()