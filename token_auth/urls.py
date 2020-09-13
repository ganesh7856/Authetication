from rest_framework.routers import SimpleRouter
from token_auth.views import *


router = SimpleRouter()
router.register('api/v1',EmployeeOps)



urlpatterns = router.urls

