from typing import Dict, Type
from src.entidades.terrenos.registro_forestal import RegistroForestal
from src.servicios.negocio.paquete import Paquete


class FincasService:
    """
    Servicio de negocio que coordina todas las fincas (RegistroForestal).
    Permite fumigar, cosechar y empaquetar cultivos por tipo.
    """

    def __init__(self):
        self._fincas: Dict[int, RegistroForestal] = {}

    # ------------------------------------------------------------------
    # Gestión de Fincas
    # ------------------------------------------------------------------
    def add_finca(self, registro: RegistroForestal):
        """Agrega una nueva finca al registro general."""
        self._fincas[registro.get_id_padron()] = registro
        print(f"✅ Finca agregada (Padrón: {registro.get_id_padron()})")

    def get_finca(self, id_padron: int) -> RegistroForestal | None:
        """Devuelve la finca con el ID indicado, o None si no existe."""
        return self._fincas.get(id_padron)

    # ------------------------------------------------------------------
    # Fumigar
    # ------------------------------------------------------------------
    def fumigar(self, id_padron: int, plaguicida: str):
        """Aplica un plaguicida a la finca indicada."""
        finca = self._fincas.get(id_padron)
        if not finca:
            print(f"⚠️ No existe finca con padrón {id_padron}")
            return

        print(f"🧴 Fumigando finca {id_padron} con plaguicida '{plaguicida}'...")
        plantacion = finca.get_plantacion()
        if plantacion:
            for cultivo in plantacion.get_cultivos():
                cultivo.set_fumigado(True)
        print("✅ Fumigación completada.")

    # ------------------------------------------------------------------
    # Cosechar y Empaquetar
    # ------------------------------------------------------------------
    def cosechar_y_empaquetar(self, tipo_cultivo: Type) -> Paquete:
        """Cosecha todos los cultivos de un tipo específico y los empaqueta."""
        paquete = Paquete(tipo_cultivo)

        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            if not plantacion:
                continue

            cultivos = plantacion.get_cultivos()
            a_cosechar = [c for c in cultivos if isinstance(c, tipo_cultivo)]

            for cultivo in a_cosechar:
                paquete.agregar(cultivo)
                cultivos.remove(cultivo)

        print(f"🌾 COSECHANDO {len(paquete._contenido)} unidades de {tipo_cultivo.__name__}")
        return paquete
