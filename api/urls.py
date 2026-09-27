from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, ConsultaViewSet

router = DefaultRouter()
router.register(
    r"medicos",
    MedicoViewSet,
    basename="medico"
)

router.register(
    r"consultas",
    ConsultaViewSet,
    basename="consulta"
)

urlpatterns = router.urls
