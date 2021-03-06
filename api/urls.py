from rest_framework.routers import DefaultRouter

from .views import QuestionViewSet, CategoryViewSet, AnimalViewSet, ChoiceViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'animals', AnimalViewSet, basename='animal')
router.register(r'choices', ChoiceViewSet, basename='choice')

urlpatterns = router.urls
