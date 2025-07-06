from dataclasses import dataclass

@dataclass
class Patient:
    id: str
    edad: int
    sexo: str
    cat: int
    mmrc: int
    exacerbaciones_12m: int
    fvc_post_bd: float
    fev1_post_bd: float
    fev1_pred: float
    ratio_fev1_fvc_post_bd: float
