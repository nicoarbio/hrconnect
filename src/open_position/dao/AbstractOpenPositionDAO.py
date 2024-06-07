from abc import ABC

from src.utils.interfaces.DAO import DAO
from src.open_position.model.OpenPosition import OpenPosition


class AbstractOpenPositionDAO(DAO, ABC):

    def filter_open_positions(self) -> tuple[list[OpenPosition], list[OpenPosition]]:
        all_open_positions = self.get_all()
        positions_to_delete = []
        positions_not_to_delete = []

        for position in all_open_positions:
            # Check if all applicants have been rejected
            all_rejected = True
            for applicant in position.get_applicants():
                if applicant["status"] != "RECHAZADO":
                    all_rejected = False
                    break

            if all_rejected:
                positions_to_delete.append(position)
            else:
                positions_not_to_delete.append(position)

        return positions_to_delete, positions_not_to_delete
    
    def get_positions_with_applicants(self) -> tuple[list[OpenPosition], list[OpenPosition]]:
        """Las posiciones abiertas con aplicantes son aquellas que tienen al menos un aplicante que no ha sido rechazado o aceptado."""
        
        all_open_positions = self.get_all()
        positions_with_applicants = []

        for position in all_open_positions:
            for applicant in position.get_applicants():
                if applicant["status"] == "RECHAZADO" or applicant["status"] == "ACEPTADO":
                    open_position = False
                else:
                    open_position = True
            if open_position:
                positions_with_applicants.append(position)

        return positions_with_applicants