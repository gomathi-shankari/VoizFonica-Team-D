from rest_framework import routers
from VoizApp.models import number, plan, account, dueamt
from VoizApp.viewsets import numberVS, planVS, accountVS, dueamtVS, prepaidVS, postpaidVS, dongleVS, rechargeVS

router = routers.DefaultRouter()
router.register('number',numberVS)

router = routers.DefaultRouter()
router.register('plan',planVS)

router = routers.DefaultRouter()
router.register('account',accountVS)

router = routers.DefaultRouter()
router.register('dueamt',dueamtVS)

router = routers.DefaultRouter()
router.register('prepaid',prepaidVS)

router = routers.DefaultRouter()
router.register('postpaid',postpaidVS)

router = routers.DefaultRouter()
router.register('dongle',dongleVS)

router = routers.DefaultRouter()
router.register('recharge',rechargeVS)
