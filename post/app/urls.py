from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, LikeViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"likes", LikeViewSet)

urlpatterns = router.urls
