from rest_framework import routers
from .views import PatientViewSet, VisitViewSet, ECGViewSet

router = routers.DefaultRouter()
router.register('patient', PatientViewSet)
router.register('visit', VisitViewSet)
router.register('ecg', ECGViewSet)
