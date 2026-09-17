from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet,CategoryViewSet


router = DefaultRouter()
router.register('vacancies', VacancyViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls

